from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import UserProfile

admin.site.unregister(User) # unregister the user, we need to inherit the user from the UserAdmin

class UserProfileInline(admin.StackedInline):
    model = UserProfile # associated model
    
# associate UserProfile
class UserProfileAdmin(UserAdmin):
    inlines = [UserProfileInline]
    
# register User model
admin.site.register(User, UserProfileAdmin)
