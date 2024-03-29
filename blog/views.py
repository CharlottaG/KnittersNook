from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.contrib import messages
from .models import Pattern
from .forms import CommentForm


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
    comments = pattern.comments.all().order_by("-created_on")
    comment_count = pattern.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.pattern = pattern
            comment.save()
            messages.add_message(
            request, messages.SUCCESS,
            'Comment submitted'
    )

    comment_form = CommentForm()

    return render(
        request,
        "blog/pattern_details.html",
        {
            "pattern": pattern,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )
