from .models import SiteSettings
from .models import Project
from django.urls import reverse, reverse_lazy

def add_site_data(request):
    # this file will need to be modified if sitesettings changes
    context = {'site_title': SiteSettings.objects.get(pk=1).site_title,}
    project_links = {}
    for prj in Project.objects.all():
        project_links[prj.name] = reverse('mainsite:project', args=[prj.slug])

    context['project_links'] = project_links
    return context

