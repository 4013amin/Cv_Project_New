# Generated by Django 5.1 on 2024-09-16 04:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_otherexample_cv'),
    ]

    operations = [
        migrations.AddField(
            model_name='otherexample',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='otherexample',
            name='popularity',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='cv',
            name='otherexamples',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cv_examples', to='app.otherexample'),
        ),
    ]
