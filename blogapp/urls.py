from django.urls import path
from .views import BlogPageView, BlogDetailView, ProfilePageView

urlpatterns = [
    
    path('', BlogPageView.as_view(), name='blog'),
    path('profile/', ProfilePageView.as_view(), name='profile'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),  

]
