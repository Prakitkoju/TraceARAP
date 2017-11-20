from werkzeug.wrappers import Response
from werkzeug.exceptions import BadRequest, NotAcceptable, MethodNotAllowed, NotFound
from lib.indledger import indledger
from json import dumps

class indledgerApi(object):
    user_idvar = 21
    @staticmethod
    def create(req):
        # print req.form
        form_data = {key: req.form[key] for key in req.form}

        if not form_data['full_name']:
            raise BadRequest('Name is requried')

        user = indledger.create(form_data)
        
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

        user = indledger.update(req.params['user_id'], form_data)

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
       
        user = indledger.find_by_id(req.params['user_id'])
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
        user = [dict(iuser) for iuser in indledger.query(indledgerApi.user_idvar)]
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
    def query_grp_ind(req):
        grpid = req.params['user_id']
        print grpid
        user = [dict(iuser) for iuser in indledger.query_grp_ind(indledgerApi.user_idvar, grpid)]
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
        
