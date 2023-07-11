from django.db import models


class GalleryImage(models.Model):
    category = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255)
    image = models.ImageField()

    def __str__(self):
        return self.title
