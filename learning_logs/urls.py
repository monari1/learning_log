"""Defines URL patterns for learning_logs"""
from . import views
from django.urls import path

app_name = 'learning_logs'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('topics', views.topics, name = 'topics')
]

