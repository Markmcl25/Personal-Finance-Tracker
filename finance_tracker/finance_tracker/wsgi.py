import os
from django.core.wsgi import get_wsgi_application

# Make sure this points to the correct settings module path
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'finance_tracker.finance_tracker.settings')


application = get_wsgi_application()
