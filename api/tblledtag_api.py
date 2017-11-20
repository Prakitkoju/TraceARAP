from werkzeug.wrappers import Response
from werkzeug.exceptions import BadRequest, NotAcceptable, MethodNotAllowed, NotFound
from lib.tblledtag import tblledtag
from json import dumps

class tblledtagApi(object):

    @staticmethod
    def insert(req):
        # print req.form
        form_data = {key: req.form[key] for key in req.form}
        print "aaaa", form_data 
        user = tblledtag.insert_all(form_data)
        
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
    def delete(req):
        form_data = {key: req.form[key] for key in req.form}

        user = tblledtag.del_all(req.params['user_id'], form_data)

        if not user:
            raise NotFound('Not found')

        if req.headers['Accept'] != 'application/json':
            raise NotAcceptable()

        result = dumps(dict(user), default=str)

        return Response(result,
            mimetype='application/json',
            status=200,
        )
