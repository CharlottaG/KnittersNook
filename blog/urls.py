from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('patterns/', views.PatternList.as_view(), name='pattern_list'),
    path('<slug:slug>/', views.pattern_details, name="pattern_details"),
    path('profile/', views.Profile.as_view(), name='profile'),
]