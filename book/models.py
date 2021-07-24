from django.db import models
from django.utils import timezone


class Book(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField(null=True, editable=False)
    # deleted = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        else:
            self.updated = timezone.now()
        return super(Book, self).save(*args, **kwargs)

    class Meta:
        ordering = ["-updated", "-created"]
