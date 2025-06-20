from django.db import models

class BotBlock(models.Model):
    BLOCK_TYPES = [
        ('message', 'Сообщение'),
        ('input', 'Ввод'),
        ('button', 'Кнопки'),
        ('api', 'API-запрос'),
    ]
    title = models.CharField(max_length=255)
    message = models.TextField()
    block_type = models.CharField(max_length=20, choices=BLOCK_TYPES, default='message')
    position = models.PositiveIntegerField(default=0)
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['position'] 
    
    def __str__(self):
        return self.title


class BlockButton(models.Model):
    block = models.ForeignKey(BotBlock, related_name='buttons', on_delete=models.CASCADE)
    label = models.CharField(max_length=255)
    to_block = models.ForeignKey(BotBlock, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.block.title} → {self.to_block.title if self.to_block else '—'} [{self.label}]"
