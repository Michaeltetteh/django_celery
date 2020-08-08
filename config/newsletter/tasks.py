from __future__ import absolute_import, unicode_literals

from celery import shared_task
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER


@shared_task
def send_message(email):
    send_mail(
        'Subscription To Our Newsletter',
        'Thank you for subscribing to our news letter',
        EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )
