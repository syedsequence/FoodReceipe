"""
WSGI config for FoodReceipe project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Added imports
import django
from django.core.management import call_command
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FoodReceipe.settings')

# Setup Django
django.setup()
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'adminpass123')
    print("Superuser created.")

# Run migrations automatically on startup
try:
    call_command('migrate', interactive=False)
except Exception as e:
    # Log the exception or pass if you want to ignore errors here
    print(f"Migration error: {e}")

application = get_wsgi_application()
