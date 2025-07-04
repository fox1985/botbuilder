# Generated by Django 5.2.1 on 2025-06-19 16:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bots', '0003_botblock_x_botblock_y'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlockTransition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.CharField(blank=True, help_text='Условие перехода (например, текст кнопки)', max_length=255)),
                ('from_block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transitions_from', to='bots.botblock')),
                ('to_block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transitions_to', to='bots.botblock')),
            ],
        ),
    ]
