# Test environment settings

INSTALLED_APPS = (
    'macros',
)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
SECRET_KEY = 'not secret'
