from autos.models import Auto, Comment, FavAuto

from django.views import View
from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404

from owner.util import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from . import forms
from django.http import HttpResponse

from .forms import CommentForm

class AutoListView(OwnerListView):
    model = Auto
    template_name = "autos/auto_list.html"

    def get(self, request, *args, **kwargs):
        auto_list = Auto.objects.all()
        favorites = list()
        if request.user.is_authenticated:
            # rows = [{'id': 2}]  (A list of rows)
            rows = request.user.favorite_autos.values('id')
            favorites = [ row['id'] for row in rows ]
        ctx = {'auto_list' : auto_list, 'favorites': favorites}
        return render(request, self.template_name, ctx)


class AutoDetailView(LoginRequiredMixin, OwnerDetailView):
    model = Auto
    template_name = "autos/auto_detail.html"

    def get(self, request, pk):
        # inject autoditional fields for comments
        auto = Auto.objects.get(id=pk)
        comments = Comment.objects.filter(auto=auto).order_by('-updated_at')
        comment_form = CommentForm()
        context = { 'auto' : auto, 'comments': comments, 'comment_form': comment_form }
        return render(request, self.template_name, context)

class AutoCreateView(OwnerCreateView):
    model = Auto
    fields = ['title', 'text', 'price']
    template_name = "autos/auto_form.html"

class AutoUpdateView(OwnerUpdateView):
    model = Auto
    fields = ['title', 'text', 'price']
    template_name = "autos/auto_form.html"

def stream_file(request, pk) :
    auto = get_object_or_404(Auto, id=pk)
    response = HttpResponse()
    response['Content-Type'] = auto.content_type
    response['Content-Length'] = len(auto.picture)
    response.write(auto.picture)
    return response

class AutoFormView(LoginRequiredMixin, View):
    template = 'autos/auto_form.html'
    success_url = reverse_lazy('pics')
    def get(self, request, pk=None) :
        if not pk : 
            form = forms.CreateAutoForm()
        else: 
            auto = get_object_or_404(Auto, id=pk, owner=self.request.user)
            form = forms.CreateAutoForm(instance=auto)
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request, pk=None) :
        if not pk:
            form = forms.CreateAutoForm(request.POST, request.FILES or None)
        else:
            pic = get_object_or_404(Auto, id=pk, owner=self.request.user)
            form = forms.CreateAutoForm(request.POST, request.FILES or None, instance=pic)

        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template, ctx)

        # Autojust the model owner before saving
        pic = form.save(commit=False)
        pic.owner = self.request.user
        pic.save()
        return redirect(self.success_url)

class AutoDeleteView(OwnerDeleteView):
    model = Auto
    template_name = "autos/auto_delete.html"



class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk) :
        auto = get_object_or_404(Auto, id=pk)
        comment_form = CommentForm(request.POST)

        comment = Comment(text=request.POST['comment'], owner=request.user, auto=auto)
        comment.save()
        return redirect(reverse_lazy('auto_detail', args=[pk]))

class CommentDeleteView(OwnerDeleteView):
    model = Comment
    template_name = "autos/comment_delete.html"

    # https://stackoverflow.com/questions/26290415/deleteview-with-a-dynamic-success-url-dependent-on-id
    def get_success_url(self):
        auto = self.object.auto
        return reverse_lazy('auto_detail', args=[auto.id])


"""
Favorite
"""

# https://stackoverflow.com/questions/16458166/how-to-disable-djangos-csrf-validation
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.utils import IntegrityError

@method_decorator(csrf_exempt, name='dispatch')
class AddFavoriteView(LoginRequiredMixin, View):
    def post(self, request, pk) :
        print("Autod PK",pk)
        auto = get_object_or_404(Auto, id=pk)
        fav = FavAuto(user=request.user, auto=auto)
        try:
            fav.save()  # In case of duplicate key
        except IntegrityError as e:
            pass
        return HttpResponse()

@method_decorator(csrf_exempt, name='dispatch')
class DeleteFavoriteView(LoginRequiredMixin, View):
    def post(self, request, pk) :
        print("Delete PK",pk)
        auto = get_object_or_404(Auto, id=pk)
        try:
            fav = FavAuto.objects.get(user=request.user, auto=auto).delete()
        except FavAuto.DoesNotExist as e:
            pass

        return HttpResponse()