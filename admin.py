from django.contrib import admin

from .models import SitePage
from .models import BlogPost
from .models import Tag


admin.site.register(Tag)
admin.site.register(BlogPost)
admin.site.register(SitePage)
# Register your models here.
