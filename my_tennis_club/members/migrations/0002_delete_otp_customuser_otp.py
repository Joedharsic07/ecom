# Generated by Django 5.1.1 on 2024-10-16 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OTP',
        ),
        migrations.AddField(
            model_name='customuser',
            name='otp',
            field=models.CharField(default='', max_length=6),
        ),
    ]
