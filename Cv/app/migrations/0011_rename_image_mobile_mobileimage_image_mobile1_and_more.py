# Generated by Django 5.1 on 2024-09-22 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_mobileimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mobileimage',
            old_name='image_mobile',
            new_name='image_mobile1',
        ),
        migrations.AddField(
            model_name='mobileimage',
            name='image_mobile2',
            field=models.ImageField(null=True, upload_to='otherexamples/mobile'),
        ),
        migrations.AddField(
            model_name='mobileimage',
            name='image_mobile3',
            field=models.ImageField(null=True, upload_to='otherexamples/mobile'),
        ),
        migrations.AddField(
            model_name='mobileimage',
            name='image_mobile4',
            field=models.ImageField(null=True, upload_to='otherexamples/mobile'),
        ),
    ]
