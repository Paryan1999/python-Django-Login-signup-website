from django.contrib import admin
from .models import Blog,Profile

# Register your models here.

@admin.register(Blog)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['blog_heading','blog_image','blog_desc','pub_date','publicer_name']

admin.site.register(Profile)