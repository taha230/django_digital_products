from unittest.mock import DEFAULT

from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    parent = models.ForeignKey('self', verbose_name= _('parent') , blank= True , null= True, on_delete=models.CASCADE) # to handle sub_category, null for root category

    title = models.CharField(_('title') ,max_length=50) #verbose_name show in database
    description = models.TextField(_('description'), blank=True)
    avatar = models.ImageField(_('avatar'), blank=True, upload_to='categories')
    is_enable = models.BooleanField(_('is_enable'), default = True)
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)

    class Meta:
        db_table = 'categories'
        verbos_name = _('Category') # show in admin
        verbos_name_plural = _('Categories')


class Product(models.Model):
    title = models.CharField(_('title'), max_length=50)
    description = models.TextField(_('description'), blank=True)
    avatar = models.ImageField(_('avatar'), blank=True, upload_to='categories')
    is_enable = models.BooleanField(_('is_enable'), default=True)
    categories = models.ManyToManyField('Category', verbose_name=_('categories'), blank=True)
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)

    class Meta:
        db_table = 'products'
        verbos_name = _('Product') # show in admin
        verbos_name_plural = _('Products')


class File(models.Model):

    product = models.ForeignKey('Product', verbose_name=_('product'), blank=True)
    title = models.CharField(_('title'), max_length=50)
    is_enable = models.BooleanField(_('is_enable'), default=True)
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)
    file = models.FileField(_('file'), upload_to='files/%Y/%m/%d/')

    class Meta:
        db_table = 'files'
        verbos_name = _('File') # show in admin
        verbos_name_plural = _('Files')