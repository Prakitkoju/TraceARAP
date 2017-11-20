from psycopg2 import sql
from datetime import datetime

from db import Db

class tblitems(object):

    @staticmethod
    def create(data):
        
        sqlqry = sql.SQL("""
        insert into tblitems(
            user_id,
            name ,
            type,
            sales_rate ,
            purchase_rate,
            lock,
            create_date,
            modify_date
            ) VALUES (
            {user_id},
            {name} ,
            {type},
            {sales_rate} ,
            {purchase_rate},
            {lock},
            {create_date},
            {modify_date}
            )
            RETURNING *
            """).format(
                user_id = sql.Literal(data.get('user_id')),
                name = sql.Literal(data.get('name')),
                type = sql.Literal(data.get('type')),
                sales_rate = sql.Literal(data.get('sales_rate')),
                purchase_rate = sql.Literal(data.get('purchase_rate')),
                lock = sql.Literal(False),
                create_date = sql.Literal(datetime.now()),
                modify_date = sql.Literal(None)
        )

        return Db.exec_query(sqlqry, returning = True)

    @staticmethod
    def update(id,data):
        print "reach update func"
        sqlqry = sql.SQL("""
        update tblitems set 
            name = {name},
            sales_rate = {sales_rate},
            modify_date = {modify_date}
        where item_id = {item_id}
        Returning *    
        """).format(
                name = sql.Literal(data.get('name')),
                sales_rate = sql.Literal(data.get('sales_rate')),
                modify_date = sql.Literal(datetime.now()),
                item_id=sql.Literal(id)
        )
        print sqlqry    
        return Db.exec_query(sqlqry, returning = True)

    @staticmethod
    def find_by_id(id):
        query = sql.SQL("""
        SELECT
            *
        FROM
            tblitems
        WHERE
            item_id = {id}
        """).format(
            id = sql.Literal(id)
        )

        return Db.exec_query(query, returning = True)

    @staticmethod
    def query(user_id):
        query = sql.SQL("""
        SELECT
            *
        FROM
            tblitems
            where 
            user_id = {user_id}
        """).format(
            user_id = sql.Literal(str(user_id))
        )

        return Db.exec_query(query, returning_multi = True)    
