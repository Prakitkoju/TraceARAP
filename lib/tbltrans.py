from psycopg2 import sql
from datetime import datetime

from db import Db

class tbltrans(object):

    @staticmethod
    def max_id():
        getmax = Db.exec_query("select max(trans_id) + 1 as maxno from tbltrans", returning = True)
        if getmax == None:
            getmax = 1
        return getmax

    @staticmethod
    def insert_single(data):
        # transidvar = tbltrans.max_id()
        sqlqry = sql.SQL("""
        insert into tbltrans(
            trans_id,
            user_id,
            trans_date ,
            doc_no,
            doc_type,
            particulars ,
            indledger_id,
            grpledger_id,
            item_id,
            dr_amt,
            cr_amt,
            is_cancel,
            create_date,
            modify_date
            ) VALUES (
            {trans_id},
            {user_id},
            {trans_date} ,
            {doc_no},
            {doc_type},
            {particulars} ,
            {indledger_id},
            {grpledger_id},
            {item_id},
            {dr_amt},
            {cr_amt},
            {is_cancel},
            {create_date},
            {modify_date}
            )
            RETURNING *
            """).format(
                trans_id = sql.Literal(data.get('trans_id')),
                user_id = sql.Literal(data.get('user_id')),
                trans_date = sql.Literal(data.get('trans_date')),
                doc_no = sql.Literal(data.get('doc_no')),
                doc_type = sql.Literal(data.get('doc_type')),
                particulars = sql.Literal(data.get('particulars')),
                indledger_id = sql.Literal(data.get('indledger_id')),
                grpledger_id = sql.Literal(data.get('grpledger_id')),
                item_id = sql.Literal(data.get('item_id')),
                dr_amt = sql.Literal(data.get('dr_amt')),
                cr_amt = sql.Literal(data.get('cr_amt')),
                is_cancel = sql.Literal(False),
                create_date = sql.Literal(datetime.now()),
                modify_date = sql.Literal(None)
        )
        return Db.exec_query(sqlqry, returning = True)

    @staticmethod
    def insert_dr_cr(data):
        # transidvar = tbltrans.max_id()
        sqlqry = sql.SQL("""
        insert into tbltrans(
            trans_id,
            user_id,
            trans_date ,
            doc_no,
            doc_type,
            particulars ,
            indledger_id,
            grpledger_id,
            dindledger_id,
            dgrpledger_id,
            item_id,
            dr_amt,
            cr_amt,
            is_cancel,
            create_date,
            modify_date
            ) VALUES (
            {trans_id},
            {user_id},
            {trans_date} ,
            {doc_no},
            {doc_type},
            {particulars} ,
            {indledger_id},
            {grpledger_id},
            {dindledger_id},
            {dgrpledger_id},
            {item_id},
            {dr_amt},
            {cr_amt},
            {is_cancel},
            {create_date},
            {modify_date}
            ),
            (
            {trans_id2},
            {user_id2},
            {trans_date2} ,
            {doc_no2},
            {doc_type2},
            {particulars2} ,
            {indledger_id2},
            {grpledger_id2},
            {dindledger_id2},
            {dgrpledger_id2},
            {item_id2},
            {dr_amt2},
            {cr_amt2},
            {is_cancel2},
            {create_date2},
            {modify_date2}
            )
            RETURNING *
            """).format(
                trans_id = sql.Literal(data.get('trans_id')),
                user_id = sql.Literal(data.get('user_id')),
                trans_date = sql.Literal(data.get('trans_date')),
                doc_no = sql.Literal(data.get('doc_no')),
                doc_type = sql.Literal(data.get('doc_type')),
                particulars = sql.Literal(data.get('particulars')),
                indledger_id = sql.Literal(data.get('indledger_id')),
                grpledger_id = sql.Literal(data.get('grpledger_id')),
                dindledger_id = sql.Literal(data.get('dindledger_id')),
                dgrpledger_id = sql.Literal(data.get('dgrpledger_id')),
                item_id = sql.Literal(data.get('item_id')),
                dr_amt = sql.Literal(data.get('dr_amt')),
                cr_amt = sql.Literal(data.get('cr_amt')),
                is_cancel = sql.Literal(False),
                create_date = sql.Literal(datetime.now()),
                modify_date = sql.Literal(None),

                trans_id2 = sql.Literal(data.get('trans_id')),
                user_id2 = sql.Literal(data.get('user_id')),
                trans_date2 = sql.Literal(data.get('trans_date')),
                doc_no2 = sql.Literal(data.get('doc_no')),
                doc_type2 = sql.Literal(data.get('doc_type')),
                particulars2 = sql.Literal(data.get('particulars')),
                indledger_id2 = sql.Literal(data.get('dindledger_id')),
                grpledger_id2 = sql.Literal(data.get('dgrpledger_id')),
                dindledger_id2 = sql.Literal(data.get('indledger_id')),
                dgrpledger_id2 = sql.Literal(data.get('grpledger_id')),
                item_id2 = sql.Literal(data.get('item_id')),
                dr_amt2 = sql.Literal(data.get('cr_amt')),
                cr_amt2 = sql.Literal(data.get('dr_amt')),
                is_cancel2 = sql.Literal(False),
                create_date2 = sql.Literal(datetime.now()),
                modify_date2 = sql.Literal(None)
        )

        return Db.exec_query(sqlqry, returning_multi = True)

    @staticmethod
    def cancel(id, data):
        sqlqry = sql.SQL("""
        update tbltrans set 
            is_cancel = {is_cancel},
            cancel_by = {cancel_by},
            modify_date = {modify_date}
        where tbltrans_id = {tbltrans_id}
        Returning *    
        """).format(
                is_cancel = sql.Literal(data.get('is_cancel')),
                cancel_by = sql.Literal(data.get('cancel_by')),
                modify_date = sql.Literal(datetime.now()),
                tbltrans_id=sql.Literal(id)
        )

        return Db.exec_query(sqlqry,  returning_multi = True)

    @staticmethod
    def find_by_id(id):
        query = sql.SQL("""
        SELECT
            *
        FROM
            tbltrans
        WHERE
            tbltrans_id = {id}
        """).format(
            id = sql.Literal(id)
        )

        return Db.exec_query(query, returning_multi = True)

    @staticmethod
    def query(user_id):
        query = sql.SQL("""
        SELECT
            *
        FROM
            tbltrans
            WHERE
            user_id = {user_id}
            and is_cancel = false
        """).format(
            user_id = sql.Literal(str(user_id))
        )

        return Db.exec_query(query,returning_multi = True)    

    @staticmethod
    def query_for_opb(user_id, doc_type):
        query = sql.SQL("""
        SELECT  
            cast(t.trans_id as varchar) as trans_id, t.trans_date, t.doc_no, gl.name as grpledger, il.full_name as indledger, 
            cast(t.dr_amt as varchar) as dr_amt, cast(t.cr_amt as varchar) as cr_amt
        FROM
            tbltrans t inner join grpledger gl on cast(t.grpledger_id as VARCHAR) = 
            cast(gl.grpledger_id as VARCHAR)
            left join indledger il on cast(t.indledger_id as VARCHAR)
            = cast(il.indledger_id as VARCHAR)
            WHERE
            t.user_id = {user_id}
            and t.doc_type = {doctype}
            and t.is_cancel = false
        """).format(
            user_id = sql.Literal(str(user_id)),
            doctype = sql.Literal(doc_type)
        )
        return Db.exec_query(query, returning_multi = True) 

    @staticmethod
    def query_for_cashbook(user_id, cashid):
        query = sql.SQL("""
        SELECT  
            cast(t.trans_id as varchar) as trans_id, t.trans_date, t.doc_no, gl.name as grpledger, il.full_name as indledger, 
            cast(t.dr_amt as varchar) as dr_amt, cast(t.cr_amt as varchar) as cr_amt
        FROM
            tbltrans t left join grpledger gl on cast(t.dgrpledger_id as VARCHAR) = 
            cast(gl.grpledger_id as VARCHAR)
            left join indledger il on cast(t.dindledger_id as VARCHAR)
            = cast(il.indledger_id as VARCHAR)
            WHERE
            t.user_id = {user_id}
            and t.grpledger_id = {cash_id}
            and t.is_cancel = false
            ORDER by trans_date
        """).format(
            user_id = sql.Literal(str(user_id)),
            cash_id = sql.Literal(str(cashid))
        )
        return Db.exec_query(query, returning_multi = True)    

    @staticmethod
    def query_dr_side(user_id, doc_type):
        query = sql.SQL("""
        SELECT  
            cast(t.trans_id as varchar) as trans_id, t.trans_date, t.doc_no, gl.name as grpledger, il.full_name as indledger, 
            cast(t.dr_amt as varchar) as dr_amt, cast(t.cr_amt as varchar) as cr_amt
        FROM
            tbltrans t inner join grpledger gl on cast(t.grpledger_id as VARCHAR) = 
            cast(gl.grpledger_id as VARCHAR)
            left join indledger il on cast(t.indledger_id as VARCHAR)
            = cast(il.indledger_id as VARCHAR)
            WHERE
            t.user_id = {user_id}
            and t.doc_type = {doctype}
            and t.cr_amt = 0
            and t.is_cancel = false
        """).format(
            user_id = sql.Literal(str(user_id)),
            doctype = sql.Literal(doc_type)
        )
        return Db.exec_query(query, returning_multi = True)    

    @staticmethod
    def query_cr_side(user_id, doc_type):
        query = sql.SQL("""
        SELECT  
            cast(t.trans_id as varchar) as trans_id, t.trans_date, t.doc_no, gl.name as grpledger, il.full_name as indledger, 
            cast(t.dr_amt as varchar) as dr_amt, cast(t.cr_amt as varchar) as cr_amt
        FROM
            tbltrans t inner join grpledger gl on cast(t.grpledger_id as VARCHAR) = 
            cast(gl.grpledger_id as VARCHAR)
            left join indledger il on cast(t.indledger_id as VARCHAR)
            = cast(il.indledger_id as VARCHAR)
            WHERE
            t.user_id = {user_id}
            and t.doc_type = {doctype}
            and t.dr_amt = 0
            and t.is_cancel = false
        """).format(
            user_id = sql.Literal(str(user_id)),
            doctype = sql.Literal(doc_type)
        )
        
        return Db.exec_query(query, returning_multi = True)    

    @staticmethod
    def query_for_jv(user_id, doc_type):
        query = sql.SQL("""
        SELECT  
            cast(t.trans_id as varchar) as trans_id, t.trans_date, t.doc_no, gl.name as grpledger, il.full_name as indledger, 
            cast(t.dr_amt as varchar) as dr_amt, cast(t.cr_amt as varchar) as cr_amt
        FROM
            tbltrans t inner join grpledger gl on cast(t.grpledger_id as VARCHAR) = 
            cast(gl.grpledger_id as VARCHAR)
            left join indledger il on cast(t.indledger_id as VARCHAR)
            = cast(il.indledger_id as VARCHAR)
            WHERE
            t.user_id = {user_id}
            and t.doc_type = {doctype}
            and t.is_cancel = false
        """).format(
            user_id = sql.Literal(str(user_id)),
            doctype = sql.Literal(doc_type)
        )
        return Db.exec_query(query, returning_multi = True)    

    @staticmethod
    def query_cashbankbal(user_id):
        query = sql.SQL("""
        SELECT 'company' as company,  org_name as grpledger, org_address as cashbank, '0' as dr_amt
        FROM users
        where 
        user_id = {tbluserid}
        UNION ALL
        SELECT  
            'balances' as company, gl.name as grpledger,  gl.cashbank, 
            cast(sum(t.dr_amt-t.cr_amt) as varchar) as dr_amt
        FROM
            tbltrans t inner join grpledger gl on cast(t.grpledger_id as VARCHAR) = 
            cast(gl.grpledger_id as VARCHAR)
            WHERE
            t.user_id = {user_id}
            and gl.is_system = 'Y'
            and gl.liquidity = 'Y'
            and t.is_cancel = false
            GROUP BY gl.name, gl.cashbank
        """).format(
            tbluserid = sql.Literal(str(user_id)),
            user_id = sql.Literal(str(user_id))
        )
        return Db.exec_query(query, returning_multi = True)    

    @staticmethod
    def query_trial(user_id, todate):
        query = sql.SQL("""
        WITH mytbl as (
        SELECT  
            gl.name as grpledger,  
            sum(t.dr_amt - t.cr_amt) as dr_amt, 
            0 as cr_amt 
        FROM
            tbltrans t inner join grpledger gl on cast(t.grpledger_id as VARCHAR) = 
            cast(gl.grpledger_id as VARCHAR)
            WHERE
            t.user_id = {user_id}
            and gl.type in ('A') 
            and t.is_cancel = false
            and t.trans_date <= {to_date}
            GROUP BY gl.name
        UNION ALL
        SELECT  
            gl.name as grpledger,  
            0 as dr_amt, 
            sum(t.cr_amt - t.dr_amt) as cr_amt 
        FROM
            tbltrans t inner join grpledger gl on cast(t.grpledger_id as VARCHAR) = 
            cast(gl.grpledger_id as VARCHAR)
            WHERE
            t.user_id = {user_id}
            and gl.type in ('L') 
            and t.is_cancel = false
            and t.trans_date <= {to_date}
            GROUP BY gl.name
        UNION ALL
        SELECT  
            gl.name as grpledger,  
            0 as dr_amt, 
            sum(t.cr_amt - t.dr_amt) as cr_amt 
        FROM
            tbltrans t inner join grpledger gl on cast(t.grpledger_id as VARCHAR) = 
            cast(gl.grpledger_id as VARCHAR)
            WHERE
            t.user_id = {user_id}
            and gl.type in ('I') 
            and t.is_cancel = false
            and t.trans_date <= {to_date}
            GROUP BY gl.name
        UNION ALL
        SELECT  
            gl.name as grpledger,  
            sum(t.dr_amt - t.cr_amt) as dr_amt,
            0 as cr_amt
        FROM
            tbltrans t inner join grpledger gl on cast(t.grpledger_id as VARCHAR) = 
            cast(gl.grpledger_id as VARCHAR)
            WHERE
            t.user_id = {user_id}
            and gl.type in ('E') 
            and t.is_cancel = false
            and t.trans_date <= {to_date}
            GROUP BY gl.name
            
            )
            select grpledger, cast(case when (dr_amt = 0) Then null else dr_amt end as VARCHAR) as dr_amt,
             cast(case when (cr_amt = 0) Then null else cr_amt end as VARCHAR) as cr_amt from mytbl
            UNION ALL
            select 'TOTAL' as grpledger, cast(sum(dr_amt) as VARCHAR) as dr_amt,
            cast(sum(cr_amt) as VARCHAR) as cr_amt from
            mytbl
            UNION ALL
            select 'Difference' as grpledger, cast(sum(cr_amt - dr_amt) as VARCHAR) as dr_amt,
            null as cr_amt from
            mytbl
        """).format(
            tbluserid = sql.Literal(str(user_id)),
            to_date = sql.Literal(todate),
            user_id = sql.Literal(str(user_id))
        )
        return Db.exec_query(query, returning_multi = True)    

    @staticmethod
    def query_pl(user_id, todate):
        query = sql.SQL("""
        WITH mytbl as (
        SELECT  
            gl.name as grpledger,  
            sum(t.dr_amt) as dr_amt, 
            sum(t.cr_amt) as cr_amt 
        FROM
            tbltrans t inner join grpledger gl on cast(t.grpledger_id as VARCHAR) = 
            cast(gl.grpledger_id as VARCHAR)
            WHERE
            t.user_id = {user_id}
            and gl.type in ('I', 'E') 
            and t.is_cancel = false
            and t.trans_date <= {to_date}
            GROUP BY gl.name)
            select grpledger, cast(case when (dr_amt = 0) Then null else dr_amt end as VARCHAR) as dr_amt,
             cast(case when (cr_amt = 0) Then null else cr_amt end as VARCHAR) as cr_amt from mytbl
            UNION ALL
            select 'TOTAL' as grpledger, cast(sum(dr_amt) as VARCHAR) as dr_amt,
            cast(sum(cr_amt) as VARCHAR) as cr_amt from
            mytbl
            UNION ALL
            select 'Profit/Loss' as grpledger, cast(sum(cr_amt - dr_amt) as VARCHAR) as dr_amt,
            null as cr_amt from
            mytbl

        """).format(
            tbluserid = sql.Literal(str(user_id)),
            to_date = sql.Literal(todate),
            user_id = sql.Literal(str(user_id))
        )
        return Db.exec_query(query, returning_multi = True)    

    @staticmethod
    def query_bs(user_id, todate):
        query = sql.SQL("""
        WITH mytbl as (
        SELECT  
            gl.name as grpledger,  
            sum(t.dr_amt - t.cr_amt) as dr_amt, 
            0 as cr_amt 
        FROM
            tbltrans t inner join grpledger gl on cast(t.grpledger_id as VARCHAR) = 
            cast(gl.grpledger_id as VARCHAR)
            WHERE
            t.user_id = {user_id}
            and gl.type in ('A') 
            and t.is_cancel = false
            and t.trans_date <= {to_date}
            GROUP BY gl.name
        UNION ALL
        SELECT  
            gl.name as grpledger,  
            0 as dr_amt, 
            sum(t.cr_amt - t.dr_amt) as cr_amt 
        FROM
            tbltrans t inner join grpledger gl on cast(t.grpledger_id as VARCHAR) = 
            cast(gl.grpledger_id as VARCHAR)
            WHERE
            t.user_id = {user_id}
            and gl.type in ('L') 
            and t.is_cancel = false
            and t.trans_date <= {to_date}
            GROUP BY gl.name
            
            )
            select grpledger, cast(case when (dr_amt = 0) Then null else dr_amt end as VARCHAR) as dr_amt,
             cast(case when (cr_amt = 0) Then null else cr_amt end as VARCHAR) as cr_amt from mytbl
            UNION ALL
            select 'TOTAL' as grpledger, cast(sum(dr_amt) as VARCHAR) as dr_amt,
            cast(sum(cr_amt) as VARCHAR) as cr_amt from
            mytbl
            UNION ALL
            select 'Profit/Loss -C/D' as grpledger, null as dr_amt,
            cast(sum(cr_amt - dr_amt) as VARCHAR) as cr_amt from
            mytbl
        """).format(
            tbluserid = sql.Literal(str(user_id)),
            to_date = sql.Literal(todate),
            user_id = sql.Literal(str(user_id))
        )
        return Db.exec_query(query, returning_multi = True)    
