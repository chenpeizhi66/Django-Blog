from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    USER_GENDER_TYPE = (
        ('male','male'),
        ('female','female'),
    )
    owner = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='user') # ont to one field to make a relationship with db
    nickname = models.CharField('name', max_length=30, blank=True, default='') # blank -> when we fill in the form, it can be empty, cause the defalut is ''
    birthday = models.DateField('birthday', max_length=20, null=True, blank=True)
    gender = models.CharField('gender', max_length=10,choices=USER_GENDER_TYPE, default='male')
    address = models.CharField('address', max_length=100, blank=True, default='')
    image = models.ImageField(upload_to='images/%Y/%m', default='images/Default.jpg', max_length=100,verbose_name='user_pic')
    desc = models.TextField('Personal Description', max_length=200, blank=True, default='')
    
    class Meta:
        verbose_name = 'User Data'
        verbose_name_plural = verbose_name
        
    def __str__(self):
        return self.owner.username