# Generated by Django 5.1 on 2024-10-01 13:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_remove_blogs_category_blogs_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogs',
            name='categories',
        ),
        migrations.AddField(
            model_name='blogs',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blogs', to='app.categoryweblog'),
        ),
    ]
