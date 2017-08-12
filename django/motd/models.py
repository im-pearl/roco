from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.core.urlresolvers import reverse
from tagging.fields import TagField

# Create your models here.

@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField('TITLE', max_length=50)
    content = models.TextField('CONTENT')
    create_date = models.DateTimeField('Create Date', auto_now_add=True)
    modify_date = models.DateTimeField('Modify Date', auto_now=True)
    tag = TagField()

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ('-create_date',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('motd:post_detail', args=(self.id,))