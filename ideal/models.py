from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from uuid import uuid4
from django.urls import reverse
from matplotlib import image



class Category(models.Model):
    title = models.CharField(null=True, blank=True, max_length=200)

    #Utility Variable
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.title, self.uniqueId)


    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.title, self.uniqueId))


        self.slug = slugify('{} {}'.format(self.title, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())
        super(Category, self).save(*args, **kwargs)



class galleryImage(models.Model):
    description = models.TextField(null=True, blank=True)
    altText = models.TextField(null=True, blank=True)
    hashtags = models.CharField(null=True, blank=True, max_length=300)

    ##ImageFields
    Image = models.ImageField ( default='default_land.jpg', upload_to='landscape')

    ##Related Fiels
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)

    #Utility Variable
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.category.title, self.uniqueId)


    def get_absolute_url(self):
        return reverse('image-detail', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.category.title, self.uniqueId))


        self.slug = slugify('{} {}'.format(self.category.title, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())
        super(galleryImage, self).save(*args, **kwargs)

class idealimages (models.Model):
    compayprofile = models.ImageField( upload_to='company')
    firstslide =models.ImageField (  upload_to='company')
    secondslide = models.ImageField(   upload_to='company')
    thridslide =models.ImageField (   upload_to='company')
    forthslide = models.ImageField (   upload_to='company')