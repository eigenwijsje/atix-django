# encoding: utf-8
from django.contrib.auth.models import User
from django.db import models

from datetime import datetime

class Category(models.Model):
    name = models.CharField(u'nombre', max_length=32)
    slug = models.SlugField(u'slug', unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = u'categoría'
        verbose_name_plural = u'categorías'

    def __unicode__(self):
        return self.slug

    @models.permalink
    def get_absolute_url(self):
        return ('category-detail', [self.slug])

class Article(models.Model):
    author = models.ForeignKey(User, related_name='articles',
        verbose_name=u'autor')
    title = models.CharField(u'título', max_length=256, unique=True)
    slug = models.SlugField(u'slug', unique_for_month='published')
    intro = models.TextField(u'introducción')
    body = models.TextField(u'cuerpo')
    categories = models.ManyToManyField(Category, related_name='articles',
        verbose_name=u'categorías')
    published = models.DateTimeField(editable=False, default=datetime.now)
    last_updated = models.DateTimeField(editable=False, blank=True, null=True)
    
    class Meta:
        ordering = ('-published',)
        get_latest_by = 'published'
        verbose_name = u'artículo'
        verbose_name_plural = u'artículos'

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('article-detail', None,
            {'year': self.published.year,
                'month': self.published.month,
                'slug': self.slug})

    def save(self):
        if self.pk:
            self.last_updated = datetime.now()
        
        super(Article, self).save()
