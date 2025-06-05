from django.urls import path
from .views import *

urlpatterns = [
    
    path('', BlogPageView.as_view(), name='blog'),
    path('profile/', ProfilePageView.as_view(), name='profile'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),  
    path('add/',BlogCreateView.as_view(), name='add_blog'),
    path('edit/<int:pk>/', BlogUpdateView.as_view(), name='edit_blog')
]
