import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DATABASE_NAME'),  #get_env_variable('DATABASE_NAME'),
        'USER': os.environ.get('USER_NAME'),   #get_env_variable('DATABASE_USER'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),      #get_env_variable('DATABASE_PASSWORD'),
        'HOST': '',
        'PORT': '',
    }
}

DEBUG = True