from django.db import models
from django.utils import timezone

class Prediction(models.Model):
    text = models.CharField(max_length=255)
    result = models.CharField(max_length=10, choices=[('Positive', 'Positive'), ('Negative', 'Negative'), ('Neutral', 'Neutral')])
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
