from base import DATABASES

DEBUG = False

DATABASES['default'] = {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'ca_academy',
    'USER': 'canopus',
    'PASSWORD': 'abacate',
    'HOST': 'db.postgresql',
    'PORT': 5432
}
