from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Countries)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'comment', 'created', 'linked_to')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'comment', 'email', 'phone', 'created',)

@admin.register(Suscriber)
class SuscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'created',)