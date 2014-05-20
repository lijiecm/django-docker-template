from .base import *

import os
import dj_database_url
from .utils import get_caches


DEBUG = False
TEMPLATE_DEBUG = False

REDIS_URL = os.getenv('REDISCLOUD_URL', '')
CACHE_TIME = 60 * 60
CACHES = get_caches(REDIS_URL)

DATABASE_URL = os.getenv('DATABASE_URL', '')
DATABASES['default'] = dj_database_url.config(default=DATABASE_URL)

ALLOWED_HOSTS = []
