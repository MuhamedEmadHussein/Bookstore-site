from django.contrib import admin
from .models import Books,Reviews
# Register your models here.

class reviewInLine(admin.TabularInline):
    model = Reviews

class BooksAdmin(admin.ModelAdmin):
    inlines = [reviewInLine]
    list_display = ('title','author','price',)
    
admin.site.register(Books,BooksAdmin)