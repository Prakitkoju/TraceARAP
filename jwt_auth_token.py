import jwt
from config import config

token = jwt.encode({'uid':1}, config.get('jwt', 'secret'))
data = jwt.decode(token, config.get('jwt', 'secret'))

# print token, data['uid']