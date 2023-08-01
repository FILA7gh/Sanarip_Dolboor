DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

PROJECT_APPS = [
    'server.apps.Product',
    'server.apps.User',
]

OTHER_APPS = [
    'jazzmin',
    'rest_framework',
    'rest_framework_simplejwt',
    'drf_yasg',
    'corsheaders',
]


INSTALLED_APPS = [
    *OTHER_APPS,
    *DJANGO_APPS,
    *PROJECT_APPS
]
