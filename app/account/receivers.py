import re

from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save
from django.dispatch import receiver

User = get_user_model()


@receiver(pre_save, sender=User)
def user_fix_phone(sender, instance, **kwargs):
    if instance.phone:
        instance.phone = re.sub('[^0-9]', '', instance.phone)
