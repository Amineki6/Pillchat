from django.db import models
# Create your models here.

class table(models.Model):
    ids = models.TextField()
    title_labeler = models.TextField()
    title = models.TextField()
    labeler = models.TextField()
    rxcui = models.TextField()
    strength = models.TextField()
    query = models.TextField()


    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]  # Default ordering for the model