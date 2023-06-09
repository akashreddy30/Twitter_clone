# Generated by Django 4.1.7 on 2023-03-12 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("tweets", "0006_user_mobile"),
    ]

    operations = [
        migrations.RemoveField(model_name="user", name="mobile",),
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("mobile", models.CharField(max_length=20)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="tweets.user"
                    ),
                ),
            ],
        ),
    ]
