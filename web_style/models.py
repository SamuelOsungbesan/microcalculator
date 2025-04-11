from django.db import models
from django.utils import timezone


class Specimen(models.Model):
    name = models.CharField(max_length=100)
    magnified_size = models.FloatField()
    magnification_factor = models.FloatField()
    actual_size = models.FloatField()
    date_added = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        # Calculate actual size before saving
        if not self.actual_size:
            self.actual_size = self.magnified_size / self.magnification_factor
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.actual_size:.6f} units"