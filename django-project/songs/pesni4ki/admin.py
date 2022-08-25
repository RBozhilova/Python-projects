from django.contrib import admin
from .models import *
from tinymce.widgets import TinyMCE
# Register your models here.

class GenreAdmin(admin.ModelAdmin):
    list_display = ("genre_name",)
    search_fields = ("genre_name",)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("author_name",)
    search_fields = ("author_name",)

class SingerAdmin(admin.ModelAdmin):
    list_display = ("singer_name",)
    search_fields = ("singer_name",)


class SongAdmin(admin.ModelAdmin):
    list_display = ("song_title", "song_author",)
    search_fields = ("song_title", "song_text",)
    filter_horizontal = ["song_singer", "song_genre"]
    list_filter = ("song_singer", "song_genre")

admin.site.register(Genre, GenreAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Singer, SingerAdmin)
admin.site.register(Songs, SongAdmin)
