from employees.settings.base import *
from dotenv import load_dotenv
import datetime
import os
load_dotenv(os.path.join(BASE_DIR.resolve().parent,'.env-prod'))

REST_FRAMEWORK['JWT_EXPIRATION_DELTA']= datetime.timedelta(seconds=300)
SECRET_KEY = os.environ.get('SECRET_KEY')

DATABASES['default']['NAME']=os.environ.get('DATABASE_NAME')
DATABASES['default']['ENGINE']='django.db.backends.postgresql_psycopg2'
DATABASES['default']['USER']=os.environ.get('DATABASE_USER')
DATABASES['default']['PASSWORD']=os.environ.get('DATABASE_PASSWORD')
DATABASES['default']['HOST']=os.environ.get('DATABASE_HOST')
DATABASES['default']['PORT']=os.environ.get('DATABASE_PORT')

ALLOWED_HOSTS = ['93.188.161.11','*']

DEBUG=True