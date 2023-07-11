from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings


class Contact(models.Model):
    first_name = models.CharField(max_length=235)
    last_name = models.CharField(max_length=235)
    subject = models.CharField(max_length=235)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'


@receiver(post_save, sender=Contact)
def contact_profile(sender, instance, created, **kwargs):
    # send_mail('New Book Request', message, 'hello.laaddu@gmail.com', [instance.owner_user.email], fail_silently=False)
    pass