from werkzeug.wrappers import Response
from werkzeug.exceptions import BadRequest, NotAcceptable, MethodNotAllowed, NotFound
from lib.grpLedger import GrpLedger
from json import dumps

class GrpLedgerApi(object):
    user_idvar = 21
    @staticmethod
    def create(req):
        # print req.form
        form_data = {key: req.form[key] for key in req.form}
        
        if not form_data['name']:
            raise BadRequest('Name is requried')

        user = GrpLedger.create(form_data)
        
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
    def update(req):
        form_data = {key: req.form[key] for key in req.form}

        user = GrpLedger.update(req.params['user_id'], form_data)

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
    def get_by_id(req):
       
        user = GrpLedger.find_by_id(req.params['user_id'])
        if not user:
            raise NotFound('Not found')

        if req.headers['Accept'] != 'application/json':
            raise NotAcceptable()

        print req.headers['Accept']
        result = dumps(dict(user), default=str)

        return Response(result,
            mimetype='application/json',
            status=200,
        )

    @staticmethod
    def query(req):
        GrpLedger.insertDefault(GrpLedgerApi.user_idvar)
        user = [dict(iuser) for iuser in GrpLedger.query(GrpLedgerApi.user_idvar)]
        # user = GrpLedger.query(GrpLedgerApi.user_idvar)
        if not user:
            raise NotFound('Not found')

        if req.headers['Accept'] != 'application/json':
            raise NotAcceptable()
        # print 'res'
        result = dumps(user, default=str)
        # print result

        return Response(result,
            mimetype='application/json',
            status=200,
        )

    @staticmethod
    def query_for_bs(req):
        user = [dict(iuser) for iuser in GrpLedger.query_for_bs(GrpLedgerApi.user_idvar)]
        # user = GrpLedger.query(GrpLedgerApi.user_idvar)
        if not user:
            raise NotFound('Not found')

        if req.headers['Accept'] != 'application/json':
            raise NotAcceptable()
        # print 'res'
        result = dumps(user, default=str)
        # print result

        return Response(result,
            mimetype='application/json',
            status=200,
        )

    @staticmethod
    def query_for_trans(req):
        print 'query_for_trans'
        user = [dict(iuser) for iuser in GrpLedger.query_for_trans(GrpLedgerApi.user_idvar)]
        # user = GrpLedger.query(GrpLedgerApi.user_idvar)
        if not user:
            raise NotFound('Not found')

        if req.headers['Accept'] != 'application/json':
            raise NotAcceptable()
        # print 'res'
        result = dumps(user, default=str)
        # print result

        return Response(result,
            mimetype='application/json',
            status=200,
        )

        
