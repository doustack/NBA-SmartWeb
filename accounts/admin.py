from django.contrib import admin
from accounts.models import User,Profile

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['username','email','is_active','date_joined']
    search_fields=['username','email']
    
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=['user','first_name','last_name','phone']

