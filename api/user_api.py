from werkzeug.wrappers import Response
from werkzeug.exceptions import BadRequest, NotAcceptable, MethodNotAllowed, NotFound
from uuid import uuid4
from hashlib import sha256

from lib.user import User
from json import dumps

class UserApi(object):

    @staticmethod
    def hash_password(password):
        salt = uuid4().hex
        return sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

    @staticmethod
    def create(req):
        # print req.form
        form_data = {key: req.form[key] for key in req.form}

        if not form_data['password']:
            raise BadRequest('Password is requried')

        if form_data['password'] != form_data['confirm_password']:
            raise BadRequest('Password mismatched')

        user = User.createuser(form_data)
        
        if not user:
            raise BadRequest('Cannot create user')

        if req.headers['Accept'] != 'application/json':
            raise NotAcceptable()

        result = dumps(dict(user))
       
        return Response(result,
            mimetype='application/json',
            status=201,
        )

    @staticmethod
    def update(req):
        form_data = {key: req.form[key] for key in req.form}

        user = User.update(req.params['user_id'], form_data)

        if not user:
            raise NotFound('User not found')

        if req.headers['Accept'] != 'application/json':
            raise NotAcceptable()

        result = dumps(dict(user))

        return Response(result,
            mimetype='application/json',
            status=200,
        )

    @staticmethod
    def get_by_id(req):
        
        user = User.find_by_id(req.params['user_id'])
 
        if not user:
            raise NotFound('User not found')

        if req.headers['Accept'] != 'application/json':
            raise NotAcceptable()

        # print req.headers['Accept']
        result = dumps(dict(user), default=str)
        # print result
        return Response(result,
            mimetype='application/json',
            status=200,
        )

    @staticmethod
    def searchby(req):
        
        user = User.searchby(req.params['user_id'])
 
        if not user:
            raise NotFound('User not found')

        if req.headers['Accept'] != 'application/json':
            raise NotAcceptable()

        # print req.headers['Accept']
        result = dumps(dict(user), default=str)
        # print result
        return Response(result,
            mimetype='application/json',
            status=200,
        )

    @staticmethod
    def upload(req):
        print req
        user = req.files.get('user_photo')
        print 'user'
        print user
        User.save_uploaded_file(user, '/home/prakit/pdf')
      

    # @staticmethod
    # def get_by_email(req):
    #     form_data = {key: req.form[key] for key in req.form}
    #     print 'form_data'
    #     print form_data
    #     user = User.query_for_login_email(form_data['email'])
    #     if not user:
    #         raise NotFound('User not found')
    #     user_pass = User.query_for_login_emailmpwd(form_data['email'], UserApi.hash_password(form_data['password']))
    #     if not ususer_passer:
    #         raise NotFound('User password not correct')

    #     if req.headers['Accept'] != 'application/json':
    #         raise NotAcceptable()

    #     print req.headers['Accept']
    #     result = dumps(dict(user))

    #     return Response(result,
    #         mimetype='application/json',
    #         status=200,
    #     )
