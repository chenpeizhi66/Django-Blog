from django.db import models
from django.contrib.auth.models import User
from django.utils.functional import cached_property  # cache decorator
from django.template.loader import render_to_string  # render template
from mdeditor.fields import MDTextField # import markdown editor

# Create your models here.

class Category(models.Model):
    """ The category model of the blog """
    name = models.CharField(max_length=32, verbose_name="category name")
    desc = models.TextField(max_length=200, blank=True, default='', verbose_name="category description")
    add_date = models.DateTimeField(auto_now_add=True, verbose_name="creating date")
    pub_date = models.DateTimeField(auto_now=True, verbose_name="modified date")
    
    class Meta:
        verbose_name = "blog category"
        verbose_name_plural = verbose_name
        
        
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    """ tags """
    name = models.CharField(max_length=32, verbose_name="blog tag")
    add_date = models.DateTimeField(auto_now_add=True, verbose_name="creating date")
    pub_date = models.DateTimeField(auto_now=True, verbose_name="modified date")
    
    class Meta:
        verbose_name = "blog tag"
        verbose_name_plural = verbose_name
        
    def __str__(self):
        return self.name
    
class Post(models.Model):
    """ post """
    title = models.CharField(max_length=61, verbose_name="Title")
    desc = models.TextField(max_length=200, blank=True, default='', verbose_name="Description")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="category")
    # content = models.TextField(verbose_name="Content")
    content = MDTextField(verbose_name="Content")
    tags = models.ForeignKey(Tag, blank=True, on_delete=models.CASCADE, verbose_name="blog tag") # a post can have multiple tags -> foreign key
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="author")
    add_date = models.DateTimeField(auto_now_add=True, verbose_name="creating date")
    pub_date = models.DateTimeField(auto_now=True, verbose_name="modified date")
    pv = models.IntegerField(default=0, verbose_name='Views') # the views of the post
    
    class Meta:
        verbose_name = "post"
        verbose_name_plural = verbose_name
        
    def __str__(self):
        return self.title
    
class Sidebar(models.Model):
    # data for the sidebar
    STATUS = (
        (1, 'Hide'),
        (2, 'Show')
    )

    DISPLAY_TYPE = (
        (1, 'Search'),
        (2, 'New post'),
        (3, 'Hot post'),
        (4, 'Latest comment'),
        (5, 'Post archives'),
        (6, 'HTML')
    )
    
    title = models.CharField(max_length=50, verbose_name="Module name") # Module name
    display_type = models.PositiveIntegerField(default=1, choices=DISPLAY_TYPE, verbose_name="Display type") # Sidebar, search box popular, articles
    content = models.CharField(max_length=500, blank=True, default='', verbose_name="Content",
                               help_text="If the setting is not HTML type, it can be empty") # This field is specially used for HTML type, other types can be empty
    sort = models.PositiveIntegerField(default=1,  verbose_name="Sort", help_text='The larger the serial number, the higher the order.')
    status = models.PositiveIntegerField(default=2, choices=STATUS, verbose_name="Status") # Hide/show status
    add_date = models.DateTimeField(auto_now_add=True, verbose_name="Creation time")  # creation time
    
    class Meta:
        verbose_name = "Sidebar"
        verbose_name_plural = verbose_name
        ordering = ['-sort'] # sort in descending order

    def __str__(self):
        return self.title
    
    @classmethod # make it a callable function for the sidebar class
    def get_sidebar(cls):
        return cls.objects.filter(status=2)   # Query all modules that are displayed
    
    @property # make it as a property of the class, only readable
    def get_content(self):
        if self.display_type == 1:
            context = {
                
            }
            return render_to_string('blog/sidebar/search.html', context=context)
        elif self.display_type == 2:
            context = {
                
            }
            return render_to_string('blog/sidebar/new_post.html', context=context)
        elif self.display_type == 3:
            context = {
                
            }
            return render_to_string('blog/sidebar/hot_post.html', context=context)
        elif self.display_type == 4:
            context = {
                
            }
            return render_to_string('blog/sidebar/comment.html', context=context)
        elif self.display_type == 5:
            context = {
                
            }
            return render_to_string('blog/sidebar/archives.html', context=context)
        elif self.display_type == 6:
            return self.content