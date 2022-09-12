from django.urls import path, include
from . import views
from django.views.i18n import JavaScriptCatalog

urlpatterns = [
    path('', views.home, name='home'),
    path('jsi18n',JavaScriptCatalog.as_view(),name='js-catlog')
]
