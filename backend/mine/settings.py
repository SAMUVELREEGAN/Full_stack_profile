

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent


CSRF_TRUSTED_ORIGINS = [
    "http://localhost:5173",
    # Add other trusted origins here if needed
]


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'



SECRET_KEY = 'django-insecure-)+q%v1+xb$d&i0$3ss=gii-3ar=s+s(umnn93fmnjddji8$zp_'


DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']




INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
     'landing',
    'rest_framework',
    'about',
    'detail',
    'education',
    'experience',
    'contact',
     'project',
     'questions',
        'scroll',
        'services',
        'myskill',
         'corsheaders',
         'visitors',
         'feedback',
          'projesturl',

]
CSRF_COOKIE_SECURE = False 
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOWED_ORIGINS=["http://localhost:5173"]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', 
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mine.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mine.wsgi.application'




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'sam',
        'USER':'root',
        'PASSWORD':'ree007@mas',
        'HOST':'localhost',
        'PORT':3306
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'samuelreegan372@gmail.com'
EMAIL_HOST_PASSWORD = 'uvrosezsejqaajco'




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



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



STATIC_URL = 'static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
