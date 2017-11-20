from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.utils import redirect
from jinja2 import Environment, FileSystemLoader

from db import Db
from user import User
from api.user_api import UserApi
from api.grpledger_api import GrpLedgerApi
from api.indledger_api import indledgerApi
from api.tblitems_api import tblitemsApi
from api.tblledtag_api import tblledtagApi
from api.tbltrans_api import tbltransApi

class Router(object):

    @staticmethod
    def home_landing(req):
        return req.render('mainpage', title = "Mainpage")

    @staticmethod
    def grpledger_land(req):
        return req.render('grpledger', title = "Group Ledgers")

    @staticmethod
    def indledger_land(req):
        return req.render('indledger', title = "Individual Ledgers")
    
    @staticmethod
    def items_land(req):
        return req.render('items' , title = "Items / Products")

    @staticmethod
    def ledgertag_land(req):
        return req.render('ledgertag' , title = "Ledger Tagging")

    @staticmethod
    def signin_page(req):
        return req.render('signin' )    

    @staticmethod
    def opening_page(req):
        return req.render('openingbal' , title = "Opening Balance")  

    @staticmethod
    def receipts_page(req):
        return req.render('receipts' , title = "Receipts Vouchers")    

    @staticmethod
    def payments_page(req):
        return req.render('payments', title = "Payements Vouchers")   

    @staticmethod
    def sales_page(req):
        return req.render('sales' , title = "Sales Vouchers")  

    @staticmethod
    def purchases_page(req):
        return req.render('purchases', title = "Purchase Vouchers")   

    @staticmethod
    def jv_page(req):
        return req.render('jv', title = "Journal Vouchers")  

    @staticmethod
    def trial(req):
        return req.render('rptfinalac', title = "Trial Balance")  

    @staticmethod
    def pl(req):
        return req.render('rptpl', title = "Profit and Loss")   

    @staticmethod
    def bs(req):
        return req.render('rptbs', title = "Balance Sheet")    

    @staticmethod
    def cashbook(req):
        return req.render('cashbook' , title = "Cash Book")    

    @staticmethod
    def paginationeg(req):
        return req.render('pagination' , title = "Cpage")    

    @staticmethod
    def searchlist(req):
        return req.render('searchresult' , title = "Cpage")    

def qstteset(req):
    print req.args.get('a')
    return Response('Hey', mimetype='text/plain')

paths = [
    Rule('/', endpoint=Router.signin_page, methods=['GET']),
    Rule('/mainpage', endpoint=Router.home_landing, methods=['GET']),
    Rule('/grpledger', endpoint=Router.grpledger_land, methods=['GET']),
    Rule('/indledger', endpoint=Router.indledger_land, methods=['GET']),
    Rule('/items', endpoint=Router.items_land, methods=['GET']),
    Rule('/ledgertag', endpoint=Router.ledgertag_land, methods=['GET']),
    Rule('/openingbal', endpoint=Router.opening_page, methods=['GET']),
    Rule('/receipts', endpoint=Router.receipts_page, methods=['GET']),
    Rule('/payments', endpoint=Router.payments_page, methods=['GET']),
    Rule('/sales', endpoint=Router.sales_page, methods=['GET']),
    Rule('/purchases', endpoint=Router.purchases_page, methods=['GET']),
    Rule('/jvdoc', endpoint=Router.jv_page, methods=['GET']),
    Rule('/trial', endpoint=Router.trial, methods=['GET']),
    Rule('/pl', endpoint=Router.pl, methods=['GET']),
    Rule('/bs', endpoint=Router.bs, methods=['GET']),
    Rule('/cashbook', endpoint=Router.cashbook, methods=['GET']),
    Rule('/pagination', endpoint=Router.paginationeg, methods=['GET']),
    Rule('/search', endpoint=Router.searchlist, methods=['GET']),
       
    Rule('/api/upload', endpoint=UserApi.upload, methods=['POST']),
    Rule('/api/users', endpoint=UserApi.create, methods=['POST']),
    Rule('/api/users/<user_id>', endpoint=UserApi.get_by_id, methods=['GET']),
    Rule('/api/search/<user_id>', endpoint=UserApi.searchby, methods=['GET']),
    Rule('/api/users/<user_id>', endpoint=UserApi.update, methods=['PUT']),

    Rule('/api/ledfortrans', endpoint=GrpLedgerApi.query_for_trans, methods=['GET']),
    Rule('/api/bsledger', endpoint=GrpLedgerApi.query_for_bs, methods=['GET']),
    Rule('/api/grpledger', endpoint=GrpLedgerApi.query, methods=['GET']),
    Rule('/api/grpledger', endpoint=GrpLedgerApi.create, methods=['POST']),
    Rule('/api/grpledger/<user_id>', endpoint=GrpLedgerApi.get_by_id, methods=['GET']),
    Rule('/api/grpledger/<user_id>', endpoint=GrpLedgerApi.update, methods=['PUT']),

    Rule('/api/grpindled/<user_id>', endpoint=indledgerApi.query_grp_ind, methods=['GET']),
    Rule('/api/indledger', endpoint=indledgerApi.query, methods=['GET']),
    Rule('/api/indledger', endpoint=indledgerApi.create, methods=['POST']),
    Rule('/api/indledger/<user_id>', endpoint=indledgerApi.get_by_id, methods=['GET']),
    Rule('/api/indledger/<user_id>', endpoint=indledgerApi.update, methods=['PUT']),

    Rule('/api/items', endpoint=tblitemsApi.query, methods=['GET']),
    Rule('/api/items', endpoint=tblitemsApi.create, methods=['POST']),
    Rule('/api/items/<user_id>', endpoint=tblitemsApi.get_by_id, methods=['GET']),
    Rule('/api/items/<user_id>', endpoint=tblitemsApi.update, methods=['PUT']),

    Rule('/api/ledgertag', endpoint=tblledtagApi.insert, methods=['POST']),
    Rule('/api/ledgertag/<user_id>', endpoint=tblledtagApi.delete, methods=['DELETE']),
    
    Rule('/api/cashbankbalance', endpoint=tbltransApi.query_cashbankbalance, methods=['GET']),
    Rule('/api/purchases', endpoint=tbltransApi.query_purchases, methods=['GET']),
    Rule('/api/sales', endpoint=tbltransApi.query_sales, methods=['GET']),
    Rule('/api/payments', endpoint=tbltransApi.query_payments, methods=['GET']),
    Rule('/api/jvdoc', endpoint=tbltransApi.query_jv, methods=['GET']),
    Rule('/api/receipts', endpoint=tbltransApi.query_receipts, methods=['GET']),
    Rule('/api/openingbal', endpoint=tbltransApi.query_opb, methods=['GET']),
    Rule('/api/trans', endpoint=tbltransApi.query, methods=['GET']),
    Rule('/api/transmaxid', endpoint=tbltransApi.query_maxid, methods=['GET']),
    Rule('/api/transsingle', endpoint=tbltransApi.insert_single, methods=['POST']),
    Rule('/api/transdouble', endpoint=tbltransApi.insert_dr_cr, methods=['POST']),
    Rule('/api/trans/<user_id>', endpoint=tbltransApi.cancel, methods=['PUT']),

    Rule('/api/report/trial', endpoint=tbltransApi.query_trial, methods=['GET']),
    Rule('/api/report/pl', endpoint=tbltransApi.query_pl, methods=['GET']),
    Rule('/api/report/bs', endpoint=tbltransApi.query_bs, methods=['GET']),
    Rule('/api/report/cashbook/<code>', endpoint=tbltransApi.query_cashbook, methods=['GET']),
    Rule('/api/report/bankbook/<code>', endpoint=tbltransApi.query_opb, methods=['GET']),
    Rule('/api/report/gl/<code>', endpoint=tbltransApi.query_opb, methods=['GET']),
    Rule('/api/report/gl/sub/<code>', endpoint=tbltransApi.query_opb, methods=['GET']),

    Rule('/api/test', endpoint=qstteset)
]

class App(object):
    def __init__(self, config):
        self.config = config
        self.url_map = Map(paths)
        self.jinja_env = Environment(
            loader=FileSystemLoader(config['template_path']),
            autoescape=True
        )
        Db.connect(config['db'])

    def render_template(self, template_name, **context):
        tpl = self.jinja_env.get_template(template_name+ '.html')
        return Response(tpl.render(context), mimetype='text/html')
    
    def dispatch_req(self, req):
        adapter = self.url_map.bind_to_environ(req.environ)
        try:
            endpoint, values = adapter.match()
            req.params = values
            return endpoint(req)
        except NotFound as e:
            print e.message
            return e            
        except HTTPException, e:
            return e

    
    def wsgi_app(self, environ, start_response):
        req = Request(environ)
        req.render = self.render_template
        res = self.dispatch_req(req)
        return res(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)




