from .base import *

from redisify import redisify

DEBUG = True
TEMPLATE_DEBUG = True

DATABASES['default'] = {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'docker',
    'USER': 'docker',
    'PASSWORD': 'docker',
    'HOST': os.environ.get('DB_1_PORT_5432_TCP_ADDR'),
    'PORT': os.environ.get('DB_1_PORT_5432_TCP_PORT'),
}

CACHE_TIME = 0
CACHES = redisify(default=os.getenv('REDIS_1_PORT', None))