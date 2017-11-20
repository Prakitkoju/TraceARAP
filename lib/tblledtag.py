from psycopg2 import sql
from datetime import datetime

from db import Db

class tblledtag(object):

    @staticmethod
    def insert_all(data):
        
        sqlqry = sql.SQL("""
        insert into tblledtag(
            user_id,
            indledger_id ,
            grpledger_id
            ) VALUES (
            {user_id},
            {indledger_id} ,
            {grpledger_id}
            )
            RETURNING *
            """).format(
                user_id = sql.Literal(data.get('user_id')),
                indledger_id = sql.Literal(data.get('indledger_id')),
                grpledger_id = sql.Literal(data.get('grpledger_id'))
        )

        return Db.exec_query(sqlqry, returning = True)

    @staticmethod
    def del_all(user_id):
        query = sql.SQL("""
        DELETE
        FROM
            tblledtag
            where 
            user_id = {user_id}
        """).format(
            user_id = sql.Literal(user_id)
        )

        return Db.exec_query(query)    
    

    @staticmethod
    def query(user_id):
        query = sql.SQL("""
        SELECT
            *
        FROM
            tblledtag
            where 
            user_id = {user_id}
        """).format(
            user_id = sql.Literal(str(user_id))
        )
        return Db.exec_query(query, returning_multi = True)    

