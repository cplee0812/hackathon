from django.db import models
from django import forms
# Create your models here.
class ContactForm(models.Model):
    from_email = models.CharField(max_length=20, blank=False, default=None)
    subject = models.CharField(max_length=20, blank=False, default=None)
    message = models.CharField(max_length=20, blank=False, default=None)
