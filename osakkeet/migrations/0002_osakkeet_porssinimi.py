# Generated by Django 3.0.6 on 2020-05-07 03:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('osakkeet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='osakkeet',
            name='porssinimi',
            field=models.CharField(default=django.utils.timezone.now, max_length=24),
            preserve_default=False,
        ),
    ]
