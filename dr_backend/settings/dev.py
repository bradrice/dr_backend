from .base import *
import json

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: define the correct hosts in production!/message
ALLOWED_HOSTS = [
    '*'
]

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

try:
    from .local import *
except ImportError:
    pass


# BASE_DIR = root()
# MEDIA_ROOT = root('media')
# STATIC_ROOT = root('static_root')linux permissions drwxrwxr-x
# STATICFILES_DIRS = [root('static')]
