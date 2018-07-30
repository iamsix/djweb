from django.contrib import admin

from .models import SitePage
from .models import BlogPost
from .models import Tag
from .models import Project
from .models import SiteSettings

admin.site.register(SiteSettings)
admin.site.register(Tag)
admin.site.register(BlogPost)
admin.site.register(SitePage)
admin.site.register(Project)
# Register your models here.
