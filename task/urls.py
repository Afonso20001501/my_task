from django.urls import path
from . import views

app_name = "task"

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('task/slug:/<slug:slug>/', views.TaskView.as_view(), name='task-view'),
]
