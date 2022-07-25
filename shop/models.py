from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = _('Shop')
        verbose_name_plural = _('Shops')