from django.contrib import admin
from .models import Product
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.utils.safestring import mark_safe 
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff', 'is_active', 'get_profile_picture')
    list_filter = ('is_staff', 'is_active') 
    ordering = ('email',)
    search_fields = ('email', 'username', 'first_name', 'last_name')  
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_active','otp'),
        }),
    )
    fieldsets = (
        (None, {
            'fields': ('email', 'username', 'first_name', 'last_name', 'profile_picture', 'password','otp'),
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )
    def get_profile_picture(self, obj):
        if obj.profile_picture:
            return mark_safe(f'<img src="{obj.profile_picture.url}" style="width: 50px; height: 50px; border-radius: 50%;" />')
        return "No picture"
    
    get_profile_picture.short_description = 'Profile Picture'

admin.site.register(CustomUser, CustomUserAdmin)



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image','category')
    list_filter = ['category']
    search_fields = ('name', 'description','category') 
