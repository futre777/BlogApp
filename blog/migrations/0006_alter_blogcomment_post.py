# Generated by Django 3.2 on 2021-06-19 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_rename_post_id_blogcomment_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blogpost'),
        ),
    ]
