from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from . import models



class PostCreateView(CreateView):
    model = models.Request
    template_name = 'request_new.html'
    fields = ['message', 'author']


class PostListView(ListView):
    model = models.Request
    template_name = 'request_list.html'

class PostDetailView(DetailView):
    model = models.Request
    template_name = 'request_detail.html'

class PostUpdateView(UpdateView):
    model = models.Request
    fields = ['message']
    template_name = 'request_edit.html'

class PostDeleteView(DeleteView):
    model = models.Request
    template_name = 'request_delete.html'
    success_url = reverse_lazy('request_list')
