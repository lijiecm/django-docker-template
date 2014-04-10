from .base import *

import dj_database_url
from redisify import redisify

DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = []

DATABASES['default'] = dj_database_url.config()

CACHE_TIME = 60 * 60
CACHES = redisify(default=os.getenv('REDISCLOUD_URL', None))