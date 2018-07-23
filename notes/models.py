from django.db import models


class Note(models.Model):
    text = models.TextField(max_length=128)
    author = models.TextField(max_length=32, default='anonymous')
    created = models.TimeField(auto_now_add=True, auto_now=False)
    unique_words = models.IntegerField(default=0)

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'
