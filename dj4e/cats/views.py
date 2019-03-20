from django.shortcuts import render

from django.urls import reverse, reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.views import generic

from cats.models import Cat, Breed

class CatIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'cats/index.html'

# Create your views here.
class CatListView(LoginRequiredMixin, generic.ListView):
    model = Cat
    paginate_by = 99

    # template_name = 'catalog/book_list.html' # by default will find this template
    # context_object_name = 'books' # by default will use `book_list` as variable name in template (<model>_list)

    def get_queryset(self):
        # import ipdb; ipdb.set_trace()
        query_result = Cat.objects.all().order_by('pk')
        return query_result # this is the default behavior; you can change this to filter 
    
    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(*args, object_list=object_list, **kwargs)
        # add new keys to context here
        return context

class CatDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cat

class CatCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ('cats.CatFullAccess',)
    model = Cat
    fields = '__all__'
    initial = {}

class CatUpdate(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = ('cats.CatFullAccess',)
    model = Cat
    fields = [
        'nickname', 
        'breed',
        'foods',
        'weight',
    ]

class CatDelete(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    permission_required = ('cats.CatFullAccess',)
    model = Cat
    success_url = reverse_lazy('cats')




# Breeds
class BreedListView(LoginRequiredMixin, generic.ListView):
    model = Breed
    paginate_by = 99

    # template_name = 'catalog/book_list.html' # by default will find this template
    # context_object_name = 'books' # by default will use `book_list` as variable name in template (<model>_list)

    def get_queryset(self):
        # import ipdb; ipdb.set_trace()
        query_result = Breed.objects.all().order_by('pk')
        return query_result # this is the default behavior; you can change this to filter 
    
    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(*args, object_list=object_list, **kwargs)
        # add new keys to context here
        return context

class BreedDetailView(LoginRequiredMixin, generic.DetailView):
    model = Breed

class BreedCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ('cats.BreedFullAccess',)
    model = Breed
    fields = '__all__'
    initial = {}

class BreedUpdate(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = ('cats.BreedFullAccess',)
    model = Breed
    fields = [
        'name'
    ]

class BreedDelete(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    permission_required = ('cats.BreedFullAccess',)
    model = Breed
    success_url = reverse_lazy('breeds')