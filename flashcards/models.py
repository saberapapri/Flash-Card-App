from django.db import models
from django.utils import timezone  # Import timezone

class Flashcard(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)  # Use timezone.now for existing rows

    def __str__(self):
        return self.question
