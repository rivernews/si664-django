from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.IndexView.as_view(), name='index'),
    path('', views.IndexView.as_view(), name='index')
]