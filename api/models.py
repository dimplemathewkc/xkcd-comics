from django.db import models
import uuid


class Comic(models.Model):
    """
    A model representing a comic book.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image = models.URLField(null=True, blank=True)
    issue = models.IntegerField(null=True, blank=True)

    day = models.CharField(max_length=100, null=True, blank=True)
    month = models.CharField(max_length=100, null=True, blank=True)
    year = models.CharField(max_length=100, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Comics"
        db_table = "comics"
