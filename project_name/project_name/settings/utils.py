import os
import urlparse
from storages.backends.s3boto import S3BotoStorage


class MediaS3BotoStorage(S3BotoStorage):
    location = 'media'


def get_caches(url):
    parts = urlparse.urlparse(url)

    caches = {}
    caches['default'] = {
        'BACKEND': 'redis_cache.cache.RedisCache',
        'LOCATION': '%s:%s:1' % (parts.hostname, parts.port),
        'OPTIONS': {
            'CLIENT_CLASS': 'redis_cache.client.DefaultClient'
        }
    }

    if parts.password:
        caches['default']['OPTIONS']['PASSWORD'] = parts.password

    return caches
