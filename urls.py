from django.urls import path, include

from . import views

app_name = 'mainsite'
urlpatterns = [
    # path('blog/', include('blog.urls')),
    path('<str:page>', views.sitepage),
    path('', views.sitepage, {'page': 'index'}),
]
