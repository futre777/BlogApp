# Generated by Django 3.2 on 2021-06-14 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blogcomment_post_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogcomment',
            old_name='post_id',
            new_name='post',
        ),
    ]