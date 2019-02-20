from django.urls import path, reverse
from . import views

from django.views.generic import RedirectView

urlpatterns = [
    path('', views.AutoIndexView.as_view(), name='autos-index'),
    path('autos/', views.AutoListView.as_view(), name='autos'),
    path('autos/<int:pk>', views.AutoDetailView.as_view(), name='auto'),
    path('autos/<int:pk>/update/', views.AutoUpdate.as_view(), name='auto-update'),
    path('autos/<int:pk>/delete/', views.AutoDelete.as_view(), name='auto-delete'),
    path('auto/create/', views.AutoCreate.as_view(), name='auto-create'),

    path('makes/', views.MakeListView.as_view(), name='makes'),
    path('makes/<int:pk>', views.MakeDetailView.as_view(), name='make'),
    path('makes/<int:pk>/update/', views.MakeUpdate.as_view(), name='make-update'),
    path('makes/<int:pk>/delete/', views.MakeDelete.as_view(), name='make-delete'),
    path('make/create/', views.MakeCreate.as_view(), name='make-create'),
]