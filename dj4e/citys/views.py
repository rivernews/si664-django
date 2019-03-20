from django.shortcuts import render

from django.urls import reverse, reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.views import generic

from citys.models import City, State

class CityIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'citys/index.html'

# Create your views here.
class CityListView(LoginRequiredMixin, generic.ListView):
    model = City
    paginate_by = 99

    # template_name = 'catalog/book_list.html' # by default will find this template
    # context_object_name = 'books' # by default will use `book_list` as variable name in template (<model>_list)

    def get_queryset(self):
        # import ipdb; ipdb.set_trace()
        query_result = City.objects.all().order_by('pk')
        return query_result # this is the default behavior; you can change this to filter 
    
    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(*args, object_list=object_list, **kwargs)
        # add new keys to context here
        return context

class CityDetailView(LoginRequiredMixin, generic.DetailView):
    model = City

class CityCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ('citys.CityFullAccess',)
    model = City
    fields = '__all__'
    initial = {}

class CityUpdate(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = ('citys.CityFullAccess',)
    model = City
    fields = [
        'nickname', 
        'state',
        'slogan',
        'population',
    ]

class CityDelete(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    permission_required = ('citys.CityFullAccess',)
    model = City
    success_url = reverse_lazy('citys')




# States
class StateListView(LoginRequiredMixin, generic.ListView):
    model = State
    paginate_by = 99

    # template_name = 'catalog/book_list.html' # by default will find this template
    # context_object_name = 'books' # by default will use `book_list` as variable name in template (<model>_list)

    def get_queryset(self):
        # import ipdb; ipdb.set_trace()
        query_result = State.objects.all().order_by('pk')
        return query_result # this is the default behavior; you can change this to filter 
    
    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(*args, object_list=object_list, **kwargs)
        # add new keys to context here
        return context

class StateDetailView(LoginRequiredMixin, generic.DetailView):
    model = State

class StateCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ('citys.StateFullAccess',)
    model = State
    fields = '__all__'
    initial = {}

class StateUpdate(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = ('citys.StateFullAccess',)
    model = State
    fields = [
        'name'
    ]

class StateDelete(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    permission_required = ('citys.StateFullAccess',)
    model = State
    success_url = reverse_lazy('states')