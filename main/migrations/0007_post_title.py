# Generated by Django 4.1.2 on 2023-02-19 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='', max_length=80),
            preserve_default=False,
        ),
    ]