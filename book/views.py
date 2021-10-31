from django.shortcuts import render
from .models import Site

# Create your views here.
def site(request):
    s = Site.objects.all()
    context = {
        'site' : s
    }
    return render(request, 'bm/site.html', context)