# utils.py (ou script d’insertion)
import django
from django.conf import settings

settings.configure(
    DEBUG=True,
    SECRET_KEY='votre_cle_secrete_très_sécurisée',
    INSTALLED_APPS=[
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.admin',
    ],
    PASSWORD_HASHERS=[
        'django.contrib.auth.hashers.Argon2PasswordHasher',
        'django.contrib.auth.hashers.PBKDF2PasswordHasher',
        'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
        'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    ],
)

django.setup()

from django.contrib.auth.hashers import make_password
from db import admins_collection

admin_data = {
    'id': 1,
    'username': 'admin123',
    'password': make_password('password1'),
    'image': '2.jpg',
    'email': 'admin@gmail.com'
}

result = admins_collection.insert_one(admin_data)
print("Admin ajouté avec l'ID :", result.inserted_id)
