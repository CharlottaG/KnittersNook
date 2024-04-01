from django.urls import path
from . import views



urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('add_patterns/', views.add_pattern, name='add_pattern'),
    path('patterns/', views.PatternList.as_view(), name='pattern_list'),
    path('<slug:slug>/', views.pattern_details, name="pattern_details"),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
     
]
