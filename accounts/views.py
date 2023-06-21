from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site

# Create your views here.
def landingpage(request):
    current_site = get_current_site(request)
    context = {
        'current_site': current_site,
    }

    return render(request, 'landingpage.html', context)