# Generated by Django 4.1.7 on 2023-03-12 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tweets", "0007_remove_user_mobile_profile"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="mobile",
            field=models.CharField(default=True, max_length=20),
        ),
        migrations.DeleteModel(name="Profile",),
    ]
