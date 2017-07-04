from django.contrib import admin

from models import Article


class ArticleAdmin(admin.ModelAdmin):
    # list_display = ('id', 'title', 'content')
    list_display = ('id','title','content','pub_time')




admin.site.register(Article,ArticleAdmin)