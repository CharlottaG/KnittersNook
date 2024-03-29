from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from .models import Pattern

# Create your views here.

class HomePage(TemplateView):
    template_name = "blog/index.html"

class Profile(TemplateView):
    template_name = "blog/user_profile.html"

class PatternList(generic.ListView):
    queryset = Pattern.objects.filter(status=1)
    template_name = "blog/pattern_list.html"
    paginate_by = 6


def pattern_details(request, slug):
    queryset = Pattern.objects.filter(status=1)
    pattern = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/pattern_details.html",
        {
            "pattern": pattern,
          
        },
    )
