from django.views.generic import TemplateView
from django.http import Http404
from django.views.generic import TemplateView, DetailView
from .models import Blog

# Create your views here.

class BlogPageView(TemplateView):
    template_name = 'blogapp/blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = Blog.objects.all()
        return context

# Blog Detail Page - shows a single blog using Generic DetailView
class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blogapp/blog_detail.html'
    context_object_name = 'blog'

# Profile Page - static page
class ProfilePageView(TemplateView):
    template_name = 'blogapp/profile.html'

