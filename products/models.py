from unittest.mock import DEFAULT

from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    parent = models.ForeignKey('self', verbose_name= _('parent') , blank= True , null= True, on_delete=models.CASCADE) # to handle sub_category, null for root category

    title = models.CharField(_('title') ,max_length=50) #verbose_name show in database
    description = models.TextField(_('description'), blank=True)
    avatar = models.ImageField(_('avatar'), blank=True, upload_to='categories/')
    is_enable = models.BooleanField(_('is_enable'), default = True)
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)

    class Meta:
        db_table = 'categories'
        verbose_name = _('Category') # show in admin
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.title

class Product(models.Model):
    categories = models.ManyToManyField('Category', verbose_name=_('categories'), blank=True)

    title = models.CharField(_('title'), max_length=50)
    description = models.TextField(_('description'), blank=True)
    avatar = models.ImageField(_('avatar'), blank=True, upload_to='products/')
    is_enable = models.BooleanField(_('is_enable'), default=True)
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)

    class Meta:
        db_table = 'products'
        verbose_name = _('Product') # show in admin
        verbose_name_plural = _('Products')



class File(models.Model):

    product = models.ForeignKey('Product', verbose_name=_('product'), blank=True, on_delete=models.CASCADE)

    title = models.CharField(_('title'), max_length=50)
    is_enable = models.BooleanField(_('is_enable'), default=True)
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)
    file = models.FileField(_('file'), upload_to='files/%Y/%m/%d/') # can be uploaded to files too

    class Meta:
        db_table = 'files'
        verbose_name = _('File') # show in admin
        verbose_name_plural = _('Files')