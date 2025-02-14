from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length=100)
    genres = models.ManyToManyField(Genre, related_name="artists")  
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)  
    image = models.ImageField(upload_to='artists/', null=True, blank=True)  

    class Meta:
        ordering = ['-rating']

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=150)
    artists = models.ManyToManyField(Artist, related_name="songs")  # ارتباط Many-to-Many با هنرمندان
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)  # امتیاز آهنگ (از 1 تا 10)
    genres = models.ManyToManyField(Genre, related_name="songs")  # ارتباط Many-to-Many با ژانرها
    image = models.ImageField(upload_to='songs/covers/', null=True, blank=True)  # تصویر کاور آهنگ
    audio_file = models.FileField(upload_to='songs/audio/', null=True, blank=True)  # فایل صوتی آهنگ
    lyrics = models.TextField(null=True, blank=True)  # متن آهنگ
    created_at = models.DateTimeField(auto_now_add=True)  # زمان ایجاد آهنگ

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']  # ترتیب آهنگ‌ها بر اساس جدیدترین تاریخ ایجاد (نزولی)

class Playlist(models.Model):
    name = models.CharField(max_length=100)
    songs = models.ManyToManyField(Song, related_name="playlists")
    created_at = models.DateTimeField(auto_now_add=True)  # زمان ایجاد پلی‌لیست
    image = models.ImageField(upload_to='playlists/', null=True, blank=True)  # تصویر پلی‌لیست
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)  # امتیاز پلی‌لیست

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']  # ترتیب پلی‌لیست‌ها بر اساس جدیدترین تاریخ ایجاد (نزولی)
