# from api.wsgi import application

# # This is the important part for Vercel
# app = application

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')

app = get_wsgi_application()