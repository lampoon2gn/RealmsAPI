from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

# Create your models here.
class ClientMsg(models.Model):
  name = models.CharField(max_length = 32)
  email = models.EmailField()
  message = models.TextField(max_length = 1024)
  date_posted = models.DateTimeField(default = timezone.now)

  def __str__(self):
    return self.name



@receiver(post_save, sender=ClientMsg)
def _send_email(sender,instance, **kwargs):

  subject = 'myRealms Customer Message from: '+ instance.name
  msg = instance.email + ":\n" +instance.message
  client_email = instance.email
  send_mail(
    subject,
    msg,
    client_email,
    ['maohan.sun@outlook.com'],
    fail_silently=False,
  )
  

  