# Generated by Django 5.1.1 on 2024-10-17 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_otp_remove_customuser_otp'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OTP',
        ),
        migrations.AddField(
            model_name='customuser',
            name='otp',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]