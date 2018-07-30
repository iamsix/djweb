import markdown2

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.utils import timezone
from django.urls import reverse, reverse_lazy

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
            "projects": Project.objects.all(),
            # TODO I feel like hardcoding this tag here is a bad idea.. maybe I'll do it with template filters instead
            "recent_blogs": BlogPost.objects.filter(post_date__lte=timezone.now(), is_published=True, tags__name="programming").order_by('-post_date')[:5]
            }
    return render(request, 'mainsite/indexpage.html', context=context)

class BlogListView(generic.ListView):
    model = BlogPost
    context_object_name = "blog_list"
    def get_queryset(self):
        if self.request.user.is_authenticated:
            queryset = BlogPost.objects.order_by('-post_date')
        else:
            queryset = BlogPost.objects.filter(post_date__lte=timezone.now(), is_published=True).order_by('-post_date')
        return queryset


class Blog(generic.DetailView):
    model = BlogPost
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'].body = markdown2.markdown(context['post'].body)
        # do the markdown stuff here
        return context



class PostBlog(LoginRequiredMixin, generic.CreateView):
    login_url = '/' #TODO this needs to be changed
    model = BlogPost
    fields = '__all__'

class EditBlog(LoginRequiredMixin, generic.UpdateView):
    login_url = '/' #TODO this needs to be changed
    model = BlogPost
    fields = '__all__'

class ProjectPage(generic.DetailView):
    model = Project
    context_object_name = "project"



#TODO A json ajax interface for tag autocompletes
