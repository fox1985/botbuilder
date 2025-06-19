from django.db import models

class BotBlock(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()
    next_block = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    position = models.PositiveIntegerField(default=0)  # <--- добавили поле

    class Meta:
        ordering = ['position']  # <--- сортировка по позиции

    def __str__(self):
        return self.title
