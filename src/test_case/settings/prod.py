from .base import *  # pylint: disable=W0614,W0401


DEBUG = False

SECRET_KEY = os.getenv('SECRET_KEY')

_hosts = os.getenv('ALLOWED_HOSTS', '')#  # pylint: disable=invalid-name
ALLOWED_HOSTS = _hosts.split(',') if _hosts else ['*']
