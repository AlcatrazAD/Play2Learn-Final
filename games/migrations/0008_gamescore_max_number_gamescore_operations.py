# Generated by Django 5.1.4 on 2025-01-20 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0007_delete_reviews'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamescore',
            name='max_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='gamescore',
            name='operations',
            field=models.TextField(default='+'),
        ),
    ]
