from django.db import models


class Task(models.Model):
    text = models.CharField(
        max_length=50,
    )

    title = models.CharField(
        max_length=15,
        null=False,
    )

    def __str__(self):
        return f"{self.id}: {self.title}"
