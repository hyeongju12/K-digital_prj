# Generated by Django 3.2.9 on 2021-11-11 15:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Faceapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emotion',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='emotion',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
