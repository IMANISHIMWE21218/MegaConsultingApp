# Generated by Django 4.2.3 on 2023-09-12 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mega_consulting', '0002_alter_blogpost_blog_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footer',
            name='office_time',
            field=models.CharField(help_text='office time  (e.g.,"Monday- Friday 8h-18h00")', max_length=35),
        ),
    ]
