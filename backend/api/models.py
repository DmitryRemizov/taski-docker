"""Models for the API application."""

from django.db import models


class Task(models.Model):
    """Model representing a task."""

    title = models.CharField(verbose_name='Заголовок', max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        """Return string representation of the task."""
        return self.title


