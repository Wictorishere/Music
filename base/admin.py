# admin.py

from django.contrib import admin
from .models import Artist, Song, Playlist, Genre

# ثبت مدل‌ها با تنظیمات سفارشی
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'image')
    search_fields = ('name',)
    list_filter = ('genres',)
    filter_horizontal = ('genres',)  # برای نمایش افقی فیلد ManyToMany

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'rating', 'created_at')
    search_fields = ('title', 'artists__name')  # جستجو بر اساس عنوان آهنگ و نام هنرمند
    list_filter = ('genres',)
    filter_horizontal = ('artists','genres')  # برای نمایش افقی فیلد ManyToMany برای انتخاب هنرمند

@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'created_at')
    search_fields = ('name', 'songs__title')
    list_filter = ('songs',)
    filter_horizontal = ('songs',)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
