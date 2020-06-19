from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Blog


# Create your views here.

class BlogList(ListView):
    model = Blog
    paginate_by = 1


class BlogDetail(DetailView):
    model = Blog
