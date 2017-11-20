from psycopg2 import sql
from datetime import datetime

from db import Db

class indledger(object):

    @staticmethod
    def create(data):
        
        sqlqry = sql.SQL("""
        insert into indledger(
            user_id,
            full_name ,
            address,
            phoneno ,
            lock,
            panno,
            create_date,
            modify_date
            ) VALUES (
            {user_id},
            {full_name} ,
            {address},
            {phoneno} ,
            {lock},
            {panno},
            {create_date},
            {modify_date}
            )
            RETURNING *
            """).format(
                user_id = sql.Literal(data.get('user_id')),
                full_name = sql.Literal(data.get('full_name')),
                address = sql.Literal(data.get('address')),
                phoneno = sql.Literal(data.get('phoneno')),
                lock = sql.Literal(data.get('lock')),
                panno = sql.Literal(data.get('panno')),
                create_date = sql.Literal(datetime.now()),
                modify_date = sql.Literal(None)
        )

        return Db.exec_query(sqlqry, returning = True)

    @staticmethod
    def update(id,data):
        sqlqry = sql.SQL("""
        update indledger set 
            full_name = {full_name},
            address = {address},
            phoneno = {phoneno},
            modify_date = {modify_date}
        where indledger_id = {indledger_id}
        Returning *    
        """).format(
                full_name = sql.Literal(data.get('full_name')),
                address = sql.Literal(data.get('address')),
                phoneno = sql.Literal(data.get('phoneno')),
                modify_date = sql.Literal(datetime.now()),
                indledger_id=sql.Literal(id)
        )

        return Db.exec_query(sqlqry, returning = True)

    @staticmethod
    def find_by_id(id):
        query = sql.SQL("""
        SELECT
            *
        FROM
            indledger
        WHERE
            indledger_id = {id}
        """).format(
            id = sql.Literal(id)
        )

        return Db.exec_query(query, returning = True)

    @staticmethod
    def query_grp_ind(user_id, grpid):
        query = sql.SQL("""
            SELECT
                il.indledger_id, full_name, address, phoneno, panno
            FROM
                indledger il inner join tblledtag lt on cast(il.indledger_id as VARCHAR) = 
                cast(lt.indledger_id as VARCHAR)
            where 
            il.user_id = {user_id} and
            lt.grpledger_id = {grp_id}
            ORDER BY
            il.indledger_id

        """).format(
            user_id = sql.Literal(str(user_id)),
            grp_id = sql.Literal(str(grpid))
        )
        return Db.exec_query(query, returning_multi = True) 
       
    @staticmethod
    def query(user_id):
        query = sql.SQL("""
            SELECT
                indledger_id, full_name, address, phoneno, panno
            FROM
                indledger 
            where 
            user_id = {user_id}
            ORDER BY
            indledger_id
        """).format(
            user_id = sql.Literal(str(user_id))
        )

        return Db.exec_query(query, returning_multi = True)    
