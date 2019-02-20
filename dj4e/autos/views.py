from django.shortcuts import render

from django.urls import reverse, reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.views import generic

from autos.models import Auto, Make

class AutoIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'autos/index.html'

# Create your views here.
class AutoListView(LoginRequiredMixin, generic.ListView):
    model = Auto
    paginate_by = 99

    # template_name = 'catalog/book_list.html' # by default will find this template
    # context_object_name = 'books' # by default will use `book_list` as variable name in template (<model>_list)

    def get_queryset(self):
        # import ipdb; ipdb.set_trace()
        query_result = Auto.objects.all().order_by('pk')
        return query_result # this is the default behavior; you can change this to filter 
    
    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(*args, object_list=object_list, **kwargs)
        # add new keys to context here
        return context

class AutoDetailView(LoginRequiredMixin, generic.DetailView):
    model = Auto

class AutoCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ('autos.AutoFullAccess',)
    model = Auto
    fields = '__all__'
    initial = {}

class AutoUpdate(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = ('autos.AutoFullAccess',)
    model = Auto
    fields = [
        'nickname', 
        'make',
        'mileage',
        'comments',
    ]

class AutoDelete(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    permission_required = ('autos.AutoFullAccess',)
    model = Auto
    success_url = reverse_lazy('autos')

class MakeListView(LoginRequiredMixin, generic.ListView):
    model = Make
    paginate_by = 99

class MakeDetailView(LoginRequiredMixin, generic.DetailView):
    model = Make

class MakeCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ('autos.MakeFullAccess',)
    model = Make
    fields = '__all__'
    initial = {}

class MakeUpdate(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = ('autos.MakeFullAccess',)
    model = Make
    fields = [
        'name',
    ]

class MakeDelete(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    permission_required = ('autos.MakeFullAccess',)
    model = Make
    success_url = reverse_lazy('makes')