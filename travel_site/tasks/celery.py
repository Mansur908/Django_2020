import logging
import os

from celery import Celery
from django.core.mail import send_mail

from travel_site import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel_site.settings')

app = Celery('travel_site')

app.config_from_object('django.conf.settings',namespace='CELERY')

app.autodiscover_tasks()

logger = logging.getLogger(__name__)

@app.task()
def debug_task(email):
    logger.info(f"Request: {email}")

    send_mail(
        'You are registered',
        'Thank you for registration on own website',
        settings.EMAIL_HOST,
        [email],
        fail_silently=False,
    )

