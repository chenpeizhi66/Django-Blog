# define the template tags here
from django import template
from blog.models import Category, Sidebar, Post

# to make it show in all pages, a simple_tag must be defined!
# reference1: https://docs.djangoproject.com/en/4.2/howto/custom-template-tags/ 
# reference2: https://github.com/1500256797/blog_django1.10/blob/master/blog/templatetags/paginate_tags.py
register = template.Library()

@register.simple_tag # after adding this decoration, it will be a qualified template tag!
def get_category_list():
    return Category.objects.all()

@register.simple_tag
def get_sidebar_list():
    return Sidebar.get_sidebar()

@register.simple_tag
def get_new_post():
    return Post.objects.order_by('-pub_date')[:8] # only show 8 posts in descending order by time

@register.simple_tag
def get_hot_post():
    return Post.objects.order_by('-pv')[:8] # only show 8 posts in descending order by time

@register.simple_tag
def get_archives():
    return Post.objects.dates('add_date', 'month', order='DESC')[:8] # only show 8 posts in descending order by time