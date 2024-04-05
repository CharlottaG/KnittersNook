from django.urls import path
from . import views

urlpatterns = [
    path('profiles/', views.ProfilesList.as_view(), name='profiles_list'),
    path('profiles/profile/', views.user_profile, name='user_profile'),
]