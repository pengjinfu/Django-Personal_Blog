# Generated by Django 3.1 on 2020-10-01 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0010_remove_tag_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='tags',
            field=models.ManyToManyField(related_name='tag', to='article.Tag', verbose_name='标签'),
        ),
    ]
