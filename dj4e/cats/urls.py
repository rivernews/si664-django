from django.urls import path, reverse
from . import views

from django.views.generic import RedirectView

urlpatterns = [
    path('', views.CatIndexView.as_view(), name='cats-index'),

    path('cats/', views.CatListView.as_view(), name='cats'),
    path('cats/<int:pk>', views.CatDetailView.as_view(), name='cat'),
    path('cats/<int:pk>/update/', views.CatUpdate.as_view(), name='cat-update'),
    path('cats/<int:pk>/delete/', views.CatDelete.as_view(), name='cat-delete'),
    path('cat/create/', views.CatCreate.as_view(), name='cat-create'),

    path('breeds/', views.BreedListView.as_view(), name='breeds'),
    path('breeds/<int:pk>', views.BreedDetailView.as_view(), name='breed'),
    path('breeds/<int:pk>/update/', views.BreedUpdate.as_view(), name='breed-update'),
    path('breeds/<int:pk>/delete/', views.BreedDelete.as_view(), name='breed-delete'),
    path('breed/create/', views.BreedCreate.as_view(), name='breed-create'),
]