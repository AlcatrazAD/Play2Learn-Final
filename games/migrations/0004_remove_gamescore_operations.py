# Generated by Django 5.1.4 on 2025-01-16 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_rename_operation_gamescore_operations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamescore',
            name='operations',
        ),
    ]
