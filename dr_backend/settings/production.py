from .base import *
import json 
DEBUG = False

ALLOWED_HOSTS = [
        '45.56.110.221',
        '45.56.110.221:8080',
        'static.dianarice.art',
        'media.dianarice.art'
        'dianarice.art',
        'bradriceadmin.oh-joy.org',
        'stage.dianarice.art',
        ]

try:
    from .local import *
except ImportError:
    pass