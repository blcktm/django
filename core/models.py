from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")

    class Meta:
        verbose_name = "Афтор"
        verbose_name_plural = "АфторЫ"

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Track(models.Model):
    name = models.CharField(max_length=255)
    duration = models.DurationField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
