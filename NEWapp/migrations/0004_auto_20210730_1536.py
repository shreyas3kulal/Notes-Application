# Generated by Django 3.2.5 on 2021-07-30 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NEWapp', '0003_document_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='file',
        ),
        migrations.AddField(
            model_name='document',
            name='files',
            field=models.FileField(default=2, upload_to=''),
            preserve_default=False,
        ),
    ]
