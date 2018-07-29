from django.urls import path, include

from . import views

app_name = 'mainsite'
urlpatterns = [
    # path('blog/', include('blog.urls')),
    path('', views.indexpage),
    path('blog/', views.BlogListView.as_view()),
    path('blog/<slug:slug>', views.Blog.as_view(), name='blog'),
    path('<str:page>', views.sitepage),
]
