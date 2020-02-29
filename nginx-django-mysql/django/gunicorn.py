import multiprocessing
from os import environ

def max_workers():
    return cpu_count()


bind = '0.0.0.0:' + environ.get('PORT', '80')
max_requests = 1000
workers = multiprocessing.cpu_count() * 2 + 1

env = {
    'DJANGO_SETTINGS_MODULE': 'app.settings'
}

reload = True
name = 'app'
loglevel = 'info'
errorlog = '-'
accesslog = '-'
