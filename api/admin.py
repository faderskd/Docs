from django.contrib import admin
from .models import *

from django.contrib import admin

class AuthorBookInline(admin.TabularInline):
    model = Book.authors.through

class AuthorAdmin(admin.ModelAdmin):
    inlines = [
        AuthorBookInline,
    ]
    exclude = ('authors',)

admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book)
admin.site.register(BookImage)
# Register your models here.
