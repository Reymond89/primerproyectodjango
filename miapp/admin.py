from ast import Return
from turtle import update
from django.contrib import admin
from .models import Article, Category


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    
    readonly_fields = ["create_at", "update_at"]
    
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)

# configuracion del titulo del panel
title =  "Master en Python - Caceres Reymond 5"
admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = "Panel de gestion"