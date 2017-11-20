from ConfigParser import ConfigParser
from os import path

config = ConfigParser()
config.read(path.abspath('config.conf'))
# print config.get('jwt', 'secret')
