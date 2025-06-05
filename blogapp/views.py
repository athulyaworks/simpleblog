from django.views.generic import TemplateView, DetailView, CreateView, UpdateView  
from django.urls import reverse_lazy
from .models import Blog
from .forms import BlogForm

class BlogPageView(TemplateView):
    template_name = 'blogapp/blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = Blog.objects.all()
        return context

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blogapp/blog_detail.html'
    context_object_name = 'blog'

class ProfilePageView(TemplateView):
    template_name = 'blogapp/profile.html'

class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blogapp/add_blog.html'
    success_url = reverse_lazy('blog')

class BlogUpdateView(UpdateView):  
    model = Blog
    form_class = BlogForm
    template_name = 'blogapp/edit_blog.html'
    success_url = reverse_lazy('blog')
