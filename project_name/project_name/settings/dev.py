from .base import *

import os
import dj_database_url
from .utils import get_caches


DEBUG = True
TEMPLATE_DEBUG = True

REDIS_URL = os.getenv('REDIS_1_PORT', '')
CACHE_TIME = 0
CACHES = get_caches(REDIS_URL)

DATABASE_URL = 'postgres://%s:%s@%s:%s/%s' % (
    'docker',
    'docker',
    os.environ.get('DB_1_PORT_5432_TCP_ADDR'),
    os.environ.get('DB_1_PORT_5432_TCP_PORT'),
    'docker',
)

DATABASES['default'] = dj_database_url.config(default=DATABASE_URL)

ALLOWED_HOSTS = []
