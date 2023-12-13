from django.shortcuts import render, get_object_or_404
from .models import Category, Tag, Post
from django.db.models import Q, F # https://docs.djangoproject.com/en/5.0/ref/models/querysets/

# Create your views here.

def index(request):
    # home page
    post_list = Post.objects.all() # query all the posts from the db
    context = {'post_list': post_list} # call these two objects in the template
    return render(request, 'blog/index.html', context)

def category_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    # get all the posts under current category
    posts = category.post_set.all()
    
    context = {'category':category, 'post_list':posts}
    return render(request, 'blog/list.html', context)


def post_detail(request, post_id):
    # post details page
    post = get_object_or_404(Post, id=post_id)
    
    # Use post id to implement previous and next post
    prev_post = Post.objects.filter(id__lt=post_id).last() # the id of previous post
    # print(prev_post)
    next_post = Post.objects.filter(id__gt=post_id).first() # the id of bext post
    # print(next_post)
    
    Post.objects.filter(id=post_id).update(pv = F('pv')+1)
    # print(post.pv)
    
    context = {'post': post, 'prev_post':prev_post, 'next_post':next_post} # call these two objects in the template
    return render(request, 'blog/detail.html', context)

def search(request):
    keyword = request.GET.get('keyword') # get keywords from the form
    
    if not keyword:
        # if can't find the post, give all the posts
        post_list = Post.objects.all()
    else:
        # search the keyword from the title, description and content
        post_list = Post.objects.filter(Q(title__icontains=keyword) | Q(desc__icontains=keyword) | Q(content__icontains=keyword)) # case sensitive
        
    context = {
        'post_list': post_list
    }
    return render(request, 'blog/index.html', context)
    
    
def archives(request, year, month):
    # post archives
    post_list = Post.objects.filter(add_date__year=year, add_date__month=month)
    context = {'post_list': post_list, 'year': year, 'month': month}
    return render(request, 'blog/archives_list.html', context)