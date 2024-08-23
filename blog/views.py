from django.shortcuts import render, get_object_or_404

from .models import Post

# Create your views here.

def post_list(request) :
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})

# def post_detail(request,id):
#     post = get_object_or_404(Post, id=id, status = Post.Status.PUBLISHED) 
#     return render(request, 'blog/post/detail.html', {'post': post})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)  # 해당 id의 Post가 없으면 404를 반환
    return render(request, 'blog/post/detail.html', {'post': post})