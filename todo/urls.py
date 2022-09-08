from django.urls import path, include
from . import views
from django.views.i18n import JavaScriptCatalog

urlpatterns = [
    path('', views.home, name='home'),
    path('tasks/',views.show_tasks,name = 'show_tasks'),
    path('create-task/',views.create_task, name = 'create_task'),
    path('task/<int:id>',views.show_task,name = 'show_task'),
    path('jsi18n',JavaScriptCatalog.as_view(),name='js-catlog')
]
