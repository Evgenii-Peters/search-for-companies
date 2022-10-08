from django.db import models


# @author EPeters

class firm1(models.Model):
    inn = models.CharField('ИНН', max_length=20, blank=False)
    ogrn = models.CharField('ОГРН', max_length=20, blank=True)
    address = models.CharField('Адрес', max_length=100, blank=True)
    name = models.CharField('Наименование', max_length=100, blank=True)
