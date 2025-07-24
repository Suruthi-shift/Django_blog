from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import BlogPost  # Make sure this import matches your model
def home(request):
      posts = BlogPost.objects.all()  
      return render(request, 'blog/home.html', {'posts': posts})
      
def post_detail(request, post_id):    
    post = get_object_or_404(BlogPost, id=post_id)  
    return render(request, 'blog/post_detail.html', {'post': post})
# Create your views here.
