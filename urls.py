from django.urls import path, include

from . import views

app_name = 'mainsite'
urlpatterns = [
    # path('blog/', include('blog.urls')),
    path('', views.indexpage, name='index'),
    path('blog/', views.BlogListView.as_view(), name='bloglist'),
    path('blog/post', views.PostBlog.as_view(), name='blogpost'),
    path('blog/<slug:slug>/edit', views.EditBlog.as_view(), name='blogedit'),
    path('blog/<slug:slug>', views.Blog.as_view(), name='blog'),
    path('projects/<slug:slug>', views.ProjectPage.as_view(), name='project'),
    path('<str:page>', views.sitepage),
]
