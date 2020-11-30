from .base import *
import json 
DEBUG = True

ALLOWED_HOSTS = [
        '45.56.110.221',
        '45.56.110.221:8080',
        'static.dianarice.art',
        'media.dianarice.art'
        'dianarice.art',
        'admin.dianarice.art',
        ]

try:
    from .local import *
except ImportError:
    pass
