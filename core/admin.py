from django.contrib import admin

from core.models import Author, Genre, Track

admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Track)