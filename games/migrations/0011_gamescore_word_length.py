# Generated by Django 5.1.4 on 2025-01-20 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0010_alter_gamescore_operation'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamescore',
            name='word_length',
            field=models.IntegerField(default=0),
        ),
    ]
