from django.contrib import admin

from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    raw_id_fields = ['user']


admin.site.register(Article, ArticleAdmin)
