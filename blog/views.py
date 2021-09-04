from django.shortcuts import render
from .models import Post

# 여러 포스트를 나열할 때 ListView 활용
from django.views.generic import ListView, DetailView

# Create your views here.
class PostList(ListView):
    model = Post
    ordering = '-pk'
    # template_name = 'blog/index.html'


# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)

#     return render(request, "blog/single_post_page.html", context={"post": post,},)

class PostDetail(DetailView):
    model = Post