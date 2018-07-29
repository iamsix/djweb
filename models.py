from django.db import models

class SiteSettings(models.Model):
    site_title=models.CharField(max_length=255)
    site_slogan=models.CharField(max_length=255)
    

class MenuItem(models.Model):
    link_text=models.CharField(max_length=100)
    link_to=models.TextField()
    # subitem_of=models.ForiegnKey('self', on_delete=models.CASCADE, null=True) #or possibly OneToOne of another menuitem? I'm not sure if this is possible..

class SitePage(models.Model):
    page_name=models.CharField(max_length=20)
    title=models.CharField(max_length=255, blank=True)
    body=models.TextField()

    def __str__(self):
        return self.page_name
# Create your models here.
