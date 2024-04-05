from django.urls import path
from . import views

urlpatterns = [
    path('blog/profiles/',views.ProfilesList.as_view(), name='profiles_list'),
]