from django.db import models

class BotBlock(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()
    next_block = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    position = models.PositiveIntegerField(default=0)  # <--- добавили поле
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)

    class Meta:
        ordering = ['position']  # <--- сортировка по позиции

    def __str__(self):
        return self.title


class BlockTransition(models.Model):
    from_block = models.ForeignKey(BotBlock, related_name='transitions_from', on_delete=models.CASCADE)
    to_block = models.ForeignKey(BotBlock, related_name='transitions_to', on_delete=models.CASCADE)
    condition = models.CharField(max_length=255, blank=True, help_text="Условие перехода (например, текст кнопки)")

    def __str__(self):
        return f"{self.from_block} → {self.to_block} [{self.condition}]"