import Record as Record
from djang.dispatch import receiver
from django.db.models.signals import post_save
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from .models import *
from .tasks import send_email_task

@receiver(post_save, sender=Record)
def notify_about_new_post(sender, instance, created, **kwargs):
    if created:
        send_email_task.delay(instance.pk)