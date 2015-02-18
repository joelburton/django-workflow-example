from .base import *

SHOW_ADMIN = False

MIDDLEWARE_CLASSES = (
    ('django.middleware.cache.UpdateCacheMiddleware',) +
    MIDDLEWARE_CLASSES +
    ('django.middleware.cache.FetchFromCacheMiddleware',)
)

CACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_SECONDS = 600
CACHE_MIDDLEWARE_KEY_PREFIX = 'workflow-site'