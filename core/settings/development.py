# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-i8oz2nydc!hl(8s&88eadluwh1wt#4x$pml@7gf8o9k37+-lw$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CREATE_APPS = [
    'apps.watch',
    'apps.users',
]
INSTALLED_LIBRARY = [
    'jazzmin',
    'rest_framework',
    'django_filters',
    'drf_yasg',
    'rest_framework_simplejwt',
    'rest_framework.authtoken',
    'corsheaders',
    'phonenumbers',
]

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
INSTALLED_APPS = INSTALLED_LIBRARY + CREATE_APPS + DJANGO_APPS
