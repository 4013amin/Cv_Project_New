# Generated by Django 5.1.1 on 2024-09-24 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_imageotherexample'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imageotherexample',
            name='image',
        ),
        migrations.AddField(
            model_name='imageotherexample',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='otherExampleImages'),
        ),
        migrations.AddField(
            model_name='imageotherexample',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='otherExampleImages'),
        ),
        migrations.AddField(
            model_name='imageotherexample',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='otherExampleImages'),
        ),
        migrations.AddField(
            model_name='imageotherexample',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='otherExampleImages'),
        ),
    ]
