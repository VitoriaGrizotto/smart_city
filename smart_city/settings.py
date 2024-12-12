from pathlib import Path
from datetime import timedelta
 
 
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
 
 
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/
 
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!63c5n!(=pe%*8nlav#om*9^2r1v$qxe)88e4=n@rn(+fg=8h!'
 
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
 
ALLOWED_HOSTS = []
 
 
# Application definition
 
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'app_smart',
    'corsheaders',
    'rest_framework_simplejwt.token_blacklist',
    'django_filters',
    'rest_framework_simplejwt',
]
 
REST_FRAMEWORK ={
 'DEFAULT_AUTHENTICATION_CLASSES': (
 'rest_framework_simplejwt.authentication.JWTAuthentication',
 'rest_framework.authentication.SessionAuthentication',
 ),
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
}
 
SIMPLE_JWT = {
 'ACCESS_TOKEN_LIFETIME': timedelta(minutes=80),
 # Define o tempo de expiração do token JWT
 'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
 # Define o tempo de expiração do refresh token Padrao é 7 dias
}
 
 
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
 
# CORS settings
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # Adicione a origem do seu frontend
]
 
CORS_ALLOW_CREDENTIALS = True  # Se você estiver usando autenticação
 
 
ROOT_URLCONF = 'smart_city.urls'
 
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
 
 
WSGI_APPLICATION = 'smart_city.wsgi.application'
 
 
# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
 
 
# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators
 
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
 
 
# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/
 
LANGUAGE_CODE = 'en-us'
 
TIME_ZONE = 'America/Sao_Paulo'
USE_TZ = True
 
 
USE_I18N = True
 
 
 
 
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/
 
STATIC_URL = 'static/'
 
# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field
 
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'