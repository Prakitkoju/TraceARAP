from werkzeug.wrappers import Response
from werkzeug.exceptions import BadRequest, NotAcceptable, MethodNotAllowed, NotFound
from lib.tblitems import tblitems
from json import dumps

class tblitemsApi(object):
    user_idvar = 21
    @staticmethod
    def create(req):
        # print req.form
        form_data = {key: req.form[key] for key in req.form}

        if not form_data['name']:
            raise BadRequest('Name is requried')
        print "form_data"
        print form_data
        user = tblitems.create(form_data)
        
        if not user:
            raise BadRequest('Cannot create')

        if req.headers['Accept'] != 'application/json':
            raise NotAcceptable()
        print 'user'
        print user
        result = dumps(dict(user), default=str)
        print 'result'
        print result

        return Response(result,
            mimetype='application/json',
            status=201,
        )

    @staticmethod
    def update(req):
        form_data = {key: req.form[key] for key in req.form}

        user = tblitems.update(req.params['user_id'], form_data)

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
        # print 'ttt'
        # print req.params
        # print req.params['user_id']
        user = tblitems.find_by_id(req.params['user_id'])
        # print 'user'
        # print user
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
        user = [dict(iuser) for iuser in tblitems.query(tblitemsApi.user_idvar)]
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
        
