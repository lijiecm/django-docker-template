from .base import *

import dj_database_url
from redisify import redisify

DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = []

DATABASES['default'] = dj_database_url.config()

REDIS_URL = os.getenv('REDISCLOUD_URL', '')

CACHE_TIME = 60 * 60
CACHES = redisify(default=REDIS_URL)