from django.db import models


class Videoss(models.Model):
    youtube_url = models.URLField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.description} ---> {self.youtube_url}"

