# Generated by Django 2.0.10 on 2019-01-23 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0003_notification_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notification',
            options={'ordering': ['-created_at']},
        ),
    ]
