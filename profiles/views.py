from django.shortcuts import render, get_object_or_404, reverse, redirect
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView, View
from django.contrib import messages
from .models import Profile

# Create your views here.

# @login_required

class ProfilesList(TemplateView):
    template_name = "profiles/profiles_list.html"

def add_profile(request):
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, 'Your profile was added successfully!')
        return redirect('user_profile')
    else:
        profile_form = UserProfileForm()
    return render(request, 'profiles/add_user_profile.html', {'profile_form': profile_form})


def user_profile(request):
    return render(request, 'profiles/user_profile.html')

