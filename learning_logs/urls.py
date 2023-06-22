"""Defines URL patterns for learning_logs"""
from . import views
from django.urls import path

app_name = 'learning_logs'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('topics', views.topics, name = 'topics'),
    path('topics/<int:topic_id>/', views.topic, name = 'topic'),
    # Page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),
]

