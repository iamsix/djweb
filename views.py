import markdown2

from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone

from .models import SitePage
from .models import BlogPost
from .models import Project

def sitepage(request, page='index'):
    data = get_object_or_404(SitePage, page_name=page)
    pagebody = markdown2.markdown(data.body)
    context = {
            "page" : data,
            "site_title" : page,
            "page_body": pagebody,
            }
    return render(request, 'mainsite/sitepage.html', context=context)


def indexpage(request):
    data = get_object_or_404(SitePage, page_name='index')
    pagebody = markdown2.markdown(data.body, extras=['fenced-code-blocks'])
    context = {
            "page" : data,
            "site_title" : data.title,
            "page_body": pagebody,
            "recent_blogs": BlogPost.objects.filter(post_date__lte=timezone.now(), is_published=True, tags__name="programming").order_by('-post_date')
            }
    return render(request, 'mainsite/indexpage.html', context=context)

class BlogListView(generic.ListView):
    model = BlogPost
    def get_context_data(self, **kwargs):
        context = {'blog_list': BlogPost.objects.filter(post_date__lte=timezone.now(), is_published=True).order_by('-post_date')}
        return context


class Blog(generic.DetailView):
    model = BlogPost

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # pull the slug here
        return context

class ProjectPage(generic.DetailView):
    model = Project
