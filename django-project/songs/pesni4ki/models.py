from django.db import models
from tinymce.models import HTMLField
# Create your models here.


class Genre(models.Model):
    genre_name = models.CharField(max_length=100, verbose_name="Жарн")


    def __str__(self):
        return self.genre_name

    class Meta:
        verbose_name = "Жарн"
        verbose_name_plural = "Жарнове на Песни"
        ordering=("genre_name",)


class Author(models.Model):
    author_name = models.CharField(max_length=100, verbose_name="Автор")

    def __str__(self):
        return self.author_name


    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Автори на песни"
        ordering =("author_name",)


class Singer(models.Model):
    singer_name = models.CharField(max_length=100, verbose_name = "Изпълнител")

    def __str__(self):
        return self.singer_name

    class Meta:
        verbose_name = "Изпълнител"
        verbose_name_plural = "Изпълнители"
        ordering = ("singer_name",)


class Songs(models.Model):
    song_title = models.CharField(max_length=200, verbose_name="Заглавие")
    song_text = HTMLField(verbose_name="Текст на Песен")
    song_author = models.ForeignKey(Author, on_delete=models.DO_NOTHING, verbose_name="Автор ")
    song_genre = models.ManyToManyField(Genre, verbose_name = "Жарн")
    song_singer = models.ManyToManyField(Singer, verbose_name="Изпълнител")

    def __str__(self):
        return self.song_title

    class Meta:
        verbose_name = "Песен"
        verbose_name_plural = "Песни"
        ordering = ("song_title",)


