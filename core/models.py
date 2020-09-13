from django.db import models
from django.dispatch import receiver
import os


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


@receiver(models.signals.post_delete, sender=Image)
def auto_delete_file_detected(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            instance.image.delete(False)
