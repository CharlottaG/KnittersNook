from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView, View
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Pattern, Comment
from .forms import CommentForm, PatternForm

# Create your views here.

class HomePage(TemplateView):
    template_name = "blog/index.html"


class PatternList(generic.ListView):
    queryset = Pattern.objects.filter(status=1)
    template_name = "blog/pattern_list.html"
    paginate_by = 6


def pattern_details(request, slug):
    """
    Display an individual :model:`blog.Pattern`.

    **Context**

    ``pattern``
        An instance of :model:`blog.Pattern`.

    **Template:**

    :template:`blog/pattern_details.html`
    """
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
                'Comment submitted and awaiting approval'
            )
    
    comment_form = CommentForm()

    return render(
        request,
        "blog/pattern_details.html",
        {
            "pattern": pattern,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form
        },
    )


def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Pattern.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating comment!')

    return HttpResponseRedirect(reverse('pattern_details', args=[slug]))


def comment_delete(request, slug, comment_id):

    """
    view to delete comment
    """
    queryset = Pattern.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('pattern_details', args=[slug]))


def add_pattern(request):
    if request.method == 'POST':
        form = PatternForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pattern added successfully!') 
            return redirect('pattern_list')
        else:
            messages.error(request, 'Form submission failed. Please correct the errors.')
    else:
        form = PatternForm()
    return render(request, 'blog/add_pattern.html', {'form': form})