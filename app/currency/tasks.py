from celery import shared_task
from django.conf import settings


@shared_task
def send_mail(subject, message):
    recipient = settings.DEFAULT_FROM_EMAIL
    from django.core.mail import send_mail
    send_mail(
        subject,
        message,
        recipient,
        [recipient],
        fail_silently=False,
    )
