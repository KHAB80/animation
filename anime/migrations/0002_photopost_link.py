# Generated by Django 4.0 on 2023-11-27 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photopost',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='リンク'),
        ),
    ]
