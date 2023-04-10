from django.shortcuts import render

from django.views.generic import TemplateView
# Create your views here.

class HomePage(TemplateView):
    template_name = 'home.html'
    
class BlogListPage(TemplateView):
    template_name = './blogs/blogList.html'