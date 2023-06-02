from django.db import models

class Ombor(models.Model):
    ombor_nomi = models.CharField(max_length=128)
    ombor_manzili = models.CharField(max_length=128)
    ishchilar = models.CharField(max_length=128)
    mahsulotlar = models.CharField(max_length=128)

