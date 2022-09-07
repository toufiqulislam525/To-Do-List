from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tasks',views.show_tasks,name = 'show_tasks')
]