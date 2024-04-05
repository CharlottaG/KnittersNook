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