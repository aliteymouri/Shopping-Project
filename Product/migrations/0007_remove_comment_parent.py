# Generated by Django 4.1.4 on 2022-12-23 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0006_alter_comment_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='parent',
        ),
    ]
