# Generated by Django 5.1.1 on 2024-09-12 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_userprofile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, default='images/avatar.png', null=True, upload_to='profiles/'),
        ),
    ]
