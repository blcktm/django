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
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='tracks')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    tags = models.ManyToManyField("core.Tag", blank=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

