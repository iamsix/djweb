from django.shortcuts import render, get_object_or_404
from .models import SitePage

def sitepage(request, page='index'):
    data = get_object_or_404(SitePage, page_name=page)
    context = {
            "page" : data,
            "site_title" : page 
            }
    return render(request, 'mainsite/sitepage.html', context=context)
# Create your views here.
