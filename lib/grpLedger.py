from psycopg2 import sql
from datetime import datetime

from db import Db

class GrpLedger(object):

    @staticmethod
    def create(data):
        
        sqlqry = sql.SQL("""
        insert into grpledger(
            user_id,
            name ,
            type,            
            have_subledger,
            create_date,
            modify_date
            ) VALUES (
            {user_id},
            {name} ,
            {type},
            {have_subledger},
            {create_date},
            {modify_date}
            )
            RETURNING *
            """).format(
                user_id = sql.Literal(data.get('user_id')),
                name = sql.Literal(data.get('name')),
                type = sql.Literal(data.get('type')),
                have_subledger = sql.Literal(data.get('have_subledger')),
                create_date = sql.Literal(datetime.now()),
                modify_date = sql.Literal(None)
        )

        return Db.exec_query(sqlqry, returning = True)

    @staticmethod
    def insertDefault(user_id):
        sqlqry = "select count(*) as cnt from grpledger where user_id = '{}' ".format(user_id)
        cnt = Db.exec_query(sqlqry, returning = True)
        cnt = dict(cnt)
        # print cnt
        # print "insert start"
        if cnt['cnt'] == 0:
            # print "inserting"
            sqlqry = sql.SQL("""insert into grpledger(user_id, name , type, liquidity, 
                cashbank , is_system, have_subledger,
                create_date ) VALUES (
                {user_id}, {name}, {type}, {liquidity}, {cashbank}, {is_system},
                {have_subledger}, {create_date}
                ),
                (
                {user_id2}, {name2}, {type2}, {liquidity2}, {cashbank2}, {is_system2},
                {have_subledger2}, {create_date2}
                ),
                (
                {user_id3}, {name3}, {type3}, {liquidity3}, {cashbank3}, {is_system3},
                {have_subledger3}, {create_date3}
                ),
                (
                {user_id4}, {name4}, {type4}, {liquidity4}, {cashbank4}, {is_system4},
                {have_subledger4}, {create_date4}
                ),
                (
                {user_id5}, {name5}, {type5}, {liquidity5}, {cashbank5}, {is_system5},
                {have_subledger5}, {create_date5}
                ),
                (
                {user_id6}, {name6}, {type6}, {liquidity6}, {cashbank6}, {is_system6},
                {have_subledger6}, {create_date6}
                )
                RETURNING *
            """).format(
            user_id = sql.Literal(user_id),
            name = sql.Literal("Cash Balance"),
            type = sql.Literal("A"),
            liquidity = sql.Literal("Y"),
            cashbank = sql.Literal("C"),
            is_system = sql.Literal("Y"),
            have_subledger = sql.Literal("N"),
            create_date = sql.Literal(datetime.now()),

            user_id2 = sql.Literal(user_id),
            name2 = sql.Literal("Sales Account"),
            type2 = sql.Literal("I"),
            liquidity2 = sql.Literal("N"),
            cashbank2 = sql.Literal("S"),
            is_system2 = sql.Literal("Y"),
            have_subledger2 = sql.Literal("N"),
            create_date2 = sql.Literal(datetime.now()),

            user_id3 = sql.Literal(user_id),
            name3 = sql.Literal("Purchase Account"),
            type3 = sql.Literal("E"),
            liquidity3 = sql.Literal("N"),
            cashbank3 = sql.Literal("P"),
            is_system3 = sql.Literal("Y"),
            have_subledger3 = sql.Literal("N"),
            create_date3 = sql.Literal(datetime.now()),

            user_id4 = sql.Literal(user_id),
            name4 = sql.Literal("Bank Balance"),
            type4 = sql.Literal("A"),
            liquidity4 = sql.Literal("Y"),
            cashbank4 = sql.Literal("B"),
            is_system4 = sql.Literal("Y"),
            have_subledger4 = sql.Literal("Y"),
            create_date4 = sql.Literal(datetime.now()),

            user_id5 = sql.Literal(user_id),
            name5 = sql.Literal("Vendors"),
            type5 = sql.Literal("L"),
            liquidity5 = sql.Literal("N"),
            cashbank5 = sql.Literal("V"),
            is_system5 = sql.Literal("Y"),
            have_subledger5 = sql.Literal("Y"),
            create_date5 = sql.Literal(datetime.now()),

            user_id6 = sql.Literal(user_id),
            name6 = sql.Literal("Clients"),
            type6 = sql.Literal("L"),
            liquidity6 = sql.Literal("N"),
            cashbank6 = sql.Literal("G"),
            is_system6 = sql.Literal("Y"),
            have_subledger6 = sql.Literal("Y"),
            create_date6 = sql.Literal(datetime.now())
            )

            Db.exec_query(sqlqry)

            # sqlqry = sql.SQL("""insert into grpledger(user_id, name , type, liquidity, 
            #     cashbank , is_system, have_subledger,
            #     create_date, modify_date ) VALUES (
            #     {user_id},
            #     {name} ,
            #     {type},
            #     {liquidity} ,
            #     {cashbank} ,
            #     {is_system} ,
            #     {have_subledger},
            #     {create_date},
            #     {modify_date}
            #     )
            #     RETURNING *
            # """).format(
            # user_id = sql.Literal(user_id),
            # name = sql.Literal("Sales Account"),
            # type = sql.Literal("I"),
            # liquidity = sql.Literal("N"),
            # cashbank = sql.Literal("N"),
            # is_system = sql.Literal("Y"),
            # have_subledger = sql.Literal("N"),
            # create_date = sql.Literal(datetime.now()),
            # modify_date = sql.Literal(None)
            # )

            # Db.exec_query(sqlqry)

        return True

    @staticmethod
    def update(id,data):
        sqlqry = sql.SQL("""
        update grpledger set 
            name = {name},
            modify_date = {modify_date}
        where grpledger_id = {grpledger_id}
        Returning *    
        """).format(
                name = sql.Literal(data.get('name')),
                modify_date = sql.Literal(datetime.now()),
                grpledger_id=sql.Literal(id)
        )

        return Db.exec_query(sqlqry, returning = True)

    @staticmethod
    def find_by_id(id):
        query = sql.SQL("""
        SELECT
            *
        FROM
            grpledger
        WHERE
            grpledger_id = {id}
        """).format(
            id = sql.Literal(id)
        )

        return Db.exec_query(query, returning = True)

    @staticmethod
    def query(user_id):
      
        query = sql.SQL("""
        SELECT
          GrpLedger_id, name, type, liquidity, cashbank, is_system, have_subledger
        FROM
            grpledger
            where user_id = {user_id} 
            ORDER BY
            GrpLedger_id
        """).format(
           
            user_id = sql.Literal(str(user_id))
        )
        return Db.exec_query(query, returning_multi = True)    

    @staticmethod
    def query_for_trans(user_id):
      
        query = sql.SQL("""
        SELECT
          GrpLedger_id, name, type, liquidity, cashbank, is_system
        FROM
            grpledger
            where user_id = {user_id} and
            (cashbank <> 'N' or (is_system <> 'Y' or is_system is null) or liquidity<> 'N')
            ORDER BY
            GrpLedger_id
        """).format(
           
            user_id = sql.Literal(str(user_id))
        )

        ###### union for subledger getting also
        #  UNION ALL
        #     SELECT
        #   '0' as GrpLedger_id,  indledger_id, full_name as name, 'A' as type, 'Y' as liquidity,
        #    'B' as cashbank, 'Y' as is_system
        # FROM
        #     indledger
        #     where user_id = {user_id} and 
        #     cast(indledger_id as VARCHAR) in (select DISTINCT indledger_id from tblledtag as lt 
        #     INNER JOIN grpledger as gl 
        #     ON cast(lt.GrpLedger_id as VARCHAR) = cast(gl.GrpLedger_id as VARCHAR) 
        #     where gl.cashbank = 'B' 
        #     and gl.liquidity = 'Y')

        return Db.exec_query(query, returning_multi = True)    

    @staticmethod
    def query_for_bs(user_id):
      
        query = sql.SQL("""
        SELECT
          GrpLedger_id, name, type, liquidity, cashbank, is_system
        FROM
            grpledger
            where user_id = {user_id} 
            and type in ('A', 'L')
            ORDER BY
            GrpLedger_id
        """).format(
           
            user_id = sql.Literal(str(user_id))
        )
        return Db.exec_query(query, returning_multi = True)    
