from werkzeug.wrappers import Response
from werkzeug.exceptions import BadRequest, NotAcceptable, MethodNotAllowed, NotFound
from lib.tbltrans import tbltrans
from json import dumps
from datetime import datetime

class tbltransApi(object):
    user_idvar = 21
    @staticmethod
    def insert_dr_cr(req):
        # print req.form
        form_data = {key: req.form[key] for key in req.form}

        if form_data['dr_amt'] == "0" and form_data['cr_amt'] == "0":
            raise BadRequest('Debit and Credit both Zero')

        if form_data['dr_amt'] != "0" and form_data['cr_amt'] != "0":
            raise BadRequest('Debit and Credit both value is given')

        if not form_data['doc_type']:
            raise BadRequest('Document type not provided.')

        if not form_data['grpledger_id']:
            raise BadRequest('Group Ledger not provided.')

        user = tbltrans.insert_dr_cr(form_data)
        
        if not user:
            raise BadRequest('Cannot create')

        if req.headers['Accept'] != 'application/json':
            raise NotAcceptable()

        result = dumps(user, default=str)
       
        return Response(result,
            mimetype='application/json',
            status=201,
        )

    @staticmethod
    def insert_single(req):
        # print req.form
        form_data = {key: req.form[key] for key in req.form}

        if form_data['dr_amt'] == "0" and form_data['cr_amt'] == "0":
            raise BadRequest('Debit and Credit both Zero')

        if form_data['dr_amt'] != "0" and form_data['cr_amt'] != "0":
            raise BadRequest('Debit and Credit both value is given')

        if not form_data['doc_type']:
            raise BadRequest('Document type not provided.')

        if not form_data['grpledger_id']:
            raise BadRequest('Group Ledger not provided.')

        user = tbltrans.insert_single(form_data)
        
        if not user:
            raise BadRequest('Cannot create')

        if req.headers['Accept'] != 'application/json':
            raise NotAcceptable()

        result = dumps(dict(user), default=str)
       
        return Response(result,
            mimetype='application/json',
            status=201,
        )

    @staticmethod
    def cancel(req):
        form_data = {key: req.form[key] for key in req.form}

        user = tbltrans.cancel(req.params['user_id'], form_data)

        if not user:
            raise NotFound('Not found')

        if req.headers['Accept'] != 'application/json':
            raise NotAcceptable()

        result = dumps(dict(user), default=str)

        return Response(result,
            mimetype='application/json',
            status=200,
        )

    @staticmethod
    def query(req):
        user = [dict(iuser) for iuser in tbltrans.query(tbltransApi.user_idvar)]
        # user = GrpLedger.query(GrpLedgerApi.user_idvar)
        if not user:
            raise NotFound('Not found')

        if req.headers['Accept'] != 'application/json':
            raise NotAcceptable()
        result = dumps(user, default=str)

        return Response(result,
            mimetype='application/json',
            status=200,
        )       

    @staticmethod
    def query_opb(req):
        user = [dict(iuser) for iuser in tbltrans.query_for_opb(tbltransApi.user_idvar, 'OPB')]
        # user = GrpLedger.query(GrpLedgerApi.user_idvar)
        if not user:
            raise NotFound('Not found')

        if req.headers['Accept'] != 'application/json':
            raise NotAcceptable()
        result = dumps(user, default=str)

        return Response(result,
            mimetype='application/json',
            status=200,
        )       

    @staticmethod
    def query_cashbook(req):
        
        user = [dict(iuser) for iuser in tbltrans.query_for_cashbook(tbltransApi.user_idvar, req.params['code'])]
        # user = GrpLedger.query(GrpLedgerApi.user_idvar)
        if not user:
            raise NotFound('Not found')

        if req.headers['Accept'] != 'application/json':
            raise NotAcceptable()
        result = dumps(user, default=str)

        return Response(result,
            mimetype='application/json',
            status=200,
        )       

    @staticmethod
    def query_receipts(req):
        user = [dict(iuser) for iuser in tbltrans.query_cr_side(tbltransApi.user_idvar, 'CIN')]
        # user = GrpLedger.query(GrpLedgerApi.user_idvar)
        if not user:
            raise NotFound('Not found')

        if req.headers['Accept'] != 'application/json':
            raise NotAcceptable()
        result = dumps(user, default=str)

        return Response(result,
            mimetype='application/json',
            status=200,
        )   

    @staticmethod
    def query_payments(req):
        user = [dict(iuser) for iuser in tbltrans.query_dr_side(tbltransApi.user_idvar, 'COG')]
        # user = GrpLedger.query(GrpLedgerApi.user_idvar)
        if not user:
            raise NotFound('Not found')

        if req.headers['Accept'] != 'application/json':
            raise NotAcceptable()
        result = dumps(user, default=str)

        return Response(result,
            mimetype='application/json',
            status=200,
        )   

    @staticmethod
    def query_sales(req):
        user = [dict(iuser) for iuser in tbltrans.query_dr_side(tbltransApi.user_idvar, 'SEL')]
        # user = GrpLedger.query(GrpLedgerApi.user_idvar)
        if not user:
            raise NotFound('Not found')

        if req.headers['Accept'] != 'application/json':
            raise NotAcceptable()
        result = dumps(user, default=str)

        return Response(result,
            mimetype='application/json',
            status=200,
        )   

    @staticmethod
    def query_purchases(req):
        user = [dict(iuser) for iuser in tbltrans.query_cr_side(tbltransApi.user_idvar, 'PUR')]
        # user = GrpLedger.query(GrpLedgerApi.user_idvar)
        if not user:
            raise NotFound('Not found')

        if req.headers['Accept'] != 'application/json':
            raise NotAcceptable()
        result = dumps(user, default=str)

        return Response(result,
            mimetype='application/json',
            status=200,
        )   

    @staticmethod
    def query_cashbankbalance(req):
        user = [dict(iuser) for iuser in tbltrans.query_cashbankbal(tbltransApi.user_idvar)]
        # user = GrpLedger.query(GrpLedgerApi.user_idvar)
        if not user:
            raise NotFound('Not found')

        if req.headers['Accept'] != 'application/json':
            raise NotAcceptable()
        result = dumps(user, default=str)

        return Response(result,
            mimetype='application/json',
            status=200,
        )    

    @staticmethod
    def query_jv(req):
        user = [dict(iuser) for iuser in tbltrans.query_for_jv(tbltransApi.user_idvar, 'JNT')]
        # user = GrpLedger.query(GrpLedgerApi.user_idvar)
        if not user:
            raise NotFound('Not found')

        if req.headers['Accept'] != 'application/json':
            raise NotAcceptable()
        result = dumps(user, default=str)

        return Response(result,
            mimetype='application/json',
            status=200,
        )       

    @staticmethod
    def query_maxid(req):
        user = tbltrans.max_id()
        # user = GrpLedger.query(GrpLedgerApi.user_idvar)
        if not user:
            raise NotFound('Not found')

        if req.headers['Accept'] != 'application/json':
            raise NotAcceptable()
        result = dumps(user, default=str)

        return Response(result,
            mimetype='application/json',
            status=200,
        )    

    @staticmethod
    def query_trial(req):
        user = [dict(iuser) for iuser in tbltrans.query_trial(tbltransApi.user_idvar, datetime.now())]
        # user = GrpLedger.query(GrpLedgerApi.user_idvar)
        if not user:
            raise NotFound('Not found')

        if req.headers['Accept'] != 'application/json':
            raise NotAcceptable()
        result = dumps(user, default=str)

        return Response(result,
            mimetype='application/json',
            status=200,
        )             

    @staticmethod
    def query_pl(req):
        user = [dict(iuser) for iuser in tbltrans.query_pl(tbltransApi.user_idvar, datetime.now())]
        # user = GrpLedger.query(GrpLedgerApi.user_idvar)
        if not user:
            raise NotFound('Not found')

        if req.headers['Accept'] != 'application/json':
            raise NotAcceptable()
        result = dumps(user, default=str)

        return Response(result,
            mimetype='application/json',
            status=200,
        )             

    @staticmethod
    def query_bs(req):
        user = [dict(iuser) for iuser in tbltrans.query_bs(tbltransApi.user_idvar, datetime.now())]
        # user = GrpLedger.query(GrpLedgerApi.user_idvar)
        if not user:
            raise NotFound('Not found')

        if req.headers['Accept'] != 'application/json':
            raise NotAcceptable()
        result = dumps(user, default=str)

        return Response(result,
            mimetype='application/json',
            status=200,
        )             
