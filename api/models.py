from django.db import models

# Create your models here.


class Codes(models.Model):
    link = models.CharField(max_length=255)
    holder_status = models.CharField(max_length=105)
    link_from = models.CharField(max_length=255)
    image = models.ImageField(default='./static/background.jpg')


class Code(models.Model):
    qrcode = models.ImageField(default='./static/background.jpg')

