from django.db import models

class SiteSettings(models.Model):
    site_title=models.CharField(max_length=255)
    site_slogan=models.CharField(max_length=255)
    

# I may not use this menuitem thing.... it's going to be quite static I think
# probably easier to just put it in the base html
# was going to use for populating submenu of project item but not necessary when I can just use projecs directly
class MenuItem(models.Model):
    link_text=models.CharField(max_length=100)
    link_to=models.TextField()
    # subitem_of=models.ForiegnKey('self', on_delete=models.CASCADE, null=True) #or possibly OneToOne of another menuitem? I'm not sure if this is possible..

class SitePage(models.Model):
    page_name=models.CharField(max_length=20)
    title=models.CharField(max_length=255, blank=True)
    body=models.TextField(blank=True)

    def __str__(self):
        return self.page_name


class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

        
class BlogPost(models.Model):
    post_date=models.DateTimeField()
    slug=models.SlugField()
    title=models.CharField(max_length=255)
    blurb=models.CharField(max_length=255, blank=True)
    author=models.CharField(max_length=100)
    body=models.TextField()
    is_published=models.BooleanField()
    tags=models.ManyToManyField(Tag)
    # modifield fields ?

class Project(models.Model):
    slug=models.SlugField()
    name=models.CharField(max_length=100)
    short_description=models.CharField(max_length=255, blank=True)
    description=models.TextField()
    source_url=models.URLField(blank=True)
    langauge=models.ManyToManyField(Tag, blank=True)
    # project_logo ?
