from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]


class Book(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(
        Category, related_name="books", on_delete=models.CASCADE
    )

    class Meta:
        ordering = ["title"]
