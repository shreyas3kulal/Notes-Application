# Generated by Django 3.1.3 on 2020-12-08 10:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('NEWapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='contactholder',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
