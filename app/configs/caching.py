# coding: utf-8
from flask_caching import Cache

cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})
def init_cache(app):
    cache.init_app(app)

def get_cache():
    return cache