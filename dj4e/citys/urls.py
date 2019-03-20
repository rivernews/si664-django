from django.urls import path, reverse
from . import views

from django.views.generic import RedirectView

urlpatterns = [
    path('', views.CityIndexView.as_view(), name='citys-index'),

    path('citys/', views.CityListView.as_view(), name='citys'),
    path('citys/<int:pk>', views.CityDetailView.as_view(), name='city'),
    path('citys/<int:pk>/update/', views.CityUpdate.as_view(), name='city-update'),
    path('citys/<int:pk>/delete/', views.CityDelete.as_view(), name='city-delete'),
    path('city/create/', views.CityCreate.as_view(), name='city-create'),

    path('states/', views.StateListView.as_view(), name='states'),
    path('states/<int:pk>', views.StateDetailView.as_view(), name='state'),
    path('states/<int:pk>/update/', views.StateUpdate.as_view(), name='state-update'),
    path('states/<int:pk>/delete/', views.StateDelete.as_view(), name='state-delete'),
    path('state/create/', views.StateCreate.as_view(), name='state-create'),
]