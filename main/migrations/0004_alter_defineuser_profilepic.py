# Generated by Django 4.1.2 on 2023-02-19 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_defineuser_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defineuser',
            name='profilePic',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile/'),
        ),
    ]
