from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=25, blank=False)
    description = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='img', blank=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']