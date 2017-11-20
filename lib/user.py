from psycopg2 import sql
from uuid import uuid4
from hashlib import sha256
from datetime import datetime
import cgi
# import cgitb; cgitb.enable()
import os

from db import Db

class User(object):

    @staticmethod
    def hash_password(password):
        salt = uuid4().hex
        return sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

    @staticmethod
    def compare_password(hash_password, user_password):
        password, salt = hash_password.split(':')
        return password == sha256(salt.encode() + user_password.encode() ).hexdigest()

    @staticmethod
    def createuser(data):
        
        sqlqry = sql.SQL("""
        insert into users(
            user_name,
            org_name ,
            org_address,
            email ,
            password,
            create_date,
            modify_date,
            lock 
            ) VALUES (
            {user_name},
            {org_name} ,
            {org_address},
            {email} ,
            {password},
            {create_date},
            {modify_date},
            {lock}
            )
            RETURNING *
            """).format(
                user_name = sql.Literal(data.get('user_name')),
                org_name = sql.Literal(data.get('org_name')),
                org_address = sql.Literal(data.get('org_address')),
                email = sql.Literal(data.get('email')),
                password = sql.Literal( User.hash_password( data.get('password'))),
                create_date = sql.Literal(datetime.now()),
                modify_date = sql.Literal(None),
                lock = sql.Literal(False)
        )

        return Db.exec_query(sqlqry, returning = True)

    @staticmethod
    def updateuser(id,data):
        sqlqry = sql.SQL("""
        update users set 
            user_name = {user_name},
            org_name = {org_name},
            org_address = {org_address},
            modify_date = {modify_date}
        where user_id = {user_id}
        Returning *    
        """).format(
                username = sql.Literal(data.get('user_name')),
                orgname = sql.Literal(data.get('org_name')),
                orgaddress = sql.Literal(data.get('org_address')),
                moddate = sql.Literal(datetime.now()),
                user_id=sql.Literal(id)
        )

        return Db.exec_query(sqlqry, returning = True)

    @staticmethod
    def find_by_id(id):
        query = sql.SQL("""
        SELECT
            *
        FROM
            users
        WHERE
            user_id = {id}
        """).format(
            id = sql.Literal(id)
        )
        # print query
        return Db.exec_query(query, returning = True)

    @staticmethod
    def searchby(id):
        query = sql.SQL("""
        SELECT
            il.full_name as indledger, gl.name as grpledger, 
            cast(sum(t.dr_amt) as VARCHAR) as dr_amt,
           cast(sum(t.cr_amt) as VARCHAR) as cr_amt
        FROM
            indledger il INNER JOIN tblledtag lt
            ON 
            cast(il.indledger_id as VARCHAR) = 
                cast(lt.indledger_id as VARCHAR)
            INNER JOIN grpledger gl
            ON 
            cast(lt.grpledger_id as VARCHAR) = 
                cast(gl.grpledger_id as VARCHAR)    
            INNER JOIN tbltrans t
            ON 
            cast(il.indledger_id as VARCHAR) = 
                cast(t.indledger_id as VARCHAR)    
        WHERE
            UPPER(il.full_name) SIMILAR TO UPPER({id})
            GROUP BY
            il.full_name, gl.name
        """).format(
            id = sql.Literal('%'+id+'%')
        )
        # print query
        return Db.exec_query(query, returning = True)

    @staticmethod
    def query():
        query = sql.SQL("""
        SELECT
            *
        FROM
            users
        """)

        return Db.exec_query(query, returning_multi = True)   

    def save_uploaded_file (form_field, upload_dir):
        """This saves a file uploaded by an HTML form.
        The form_field is the name of the file input field from the form.
        For example, the following form_field would be "file_1":
            <input name="file_1" type="file">
        The upload_dir is the directory where the file will be written.
        If no file was uploaded or if the field does not exist then
        this does nothing.
        """
        form = cgi.FieldStorage()
        if not form.has_key(form_field): return
        fileitem = form[form_field]
        if not fileitem.file: return
        fout = file (os.path.join(upload_dir, fileitem.filename), 'wb')
        while 1:
            chunk = fileitem.file.read(100000)
            if not chunk: break
            fout.write (chunk)
        fout.close() 

    # @staticmethod
    # def query_for_login_email(email):
    #     query = sql.SQL("""
    #     SELECT
    #         *
    #     FROM
    #         users where
    #         email = {email}
    #     """).format(
    #         email = sql.Literal(email)
    #     )

    #     return Db.exec_query(query, returning = True)     

    # @staticmethod
    # def query_for_login_emailmpwd(email, mpassword):
    #     query = sql.SQL("""
    #     SELECT
    #         *
    #     FROM
    #        users where
    #         email = {email}
    #         and
    #         password = {password}
    #     returning user_id
    #     """
    #     ).format(
    #         email = sql.Literal(email),
    #         password = sql.Literal(mpassword)
    #     )

    #     return Db.exec_query(query, returning = True)       
