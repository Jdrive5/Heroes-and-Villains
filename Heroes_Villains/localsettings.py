# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-c55%1ozjr1)r1-a49n#ln=7$l^*&9$u1vj%0i3(tloph3+f+)@'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'heroes_villains_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'Elkton2009!'
    }
}