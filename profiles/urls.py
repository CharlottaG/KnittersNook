from django.urls import path
from . import views


urlpatterns = [
    path('blog/profiles/',views.ProfilesList.as_view(), name='profiles_list'),
    path('blog/add_profile/', views.add_profile, name='add_profile'),
]