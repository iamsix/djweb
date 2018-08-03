from django.db import models
from django.urls import reverse
from django.core.files.storage import FileSystemStorage

# I may change how this works as it doesn't necessarily need to be an entire db entry
# maybe change it to something like a wp_options model with 'setting name' and 'setting value'
# another option is to just use settings.py 
class SiteSettings(models.Model):
    site_title=models.CharField(max_length=255)
    site_slogan=models.CharField(max_length=255)
    

class SitePage(models.Model):
    page_name=models.CharField(max_length=20)
    title=models.CharField(max_length=255, blank=True)
    body=models.TextField(blank=True)

    def __str__(self):
        return self.page_name


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)
    # tags marked hidden will not show up on unauthenticated user-facing  website interface
    # hidden = models.BooleanField()
    def __str__(self):
        return self.name


class PostImage(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images/')

        
class BlogPost(models.Model):
    post_date=models.DateTimeField()
    slug=models.SlugField(unique=True)
    title=models.CharField(max_length=255)
    blurb=models.CharField(max_length=255, blank=True)
    author=models.CharField(max_length=100)
    body=models.TextField()
    is_published=models.BooleanField()
    tags=models.ManyToManyField(Tag)
    # modifield fields ?
    def get_absolute_url(self):
        return reverse('mainsite:blog', args=[self.slug])

class Project(models.Model):
    slug=models.SlugField(unique=True)
    name=models.CharField(max_length=100)
    short_description=models.CharField(max_length=255, blank=True)
    description=models.TextField()
    source_url=models.URLField(blank=True)
    language=models.ManyToManyField(Tag, blank=True)
    # project_logo ?
