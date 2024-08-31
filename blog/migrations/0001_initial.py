# Generated by Django 5.1 on 2024-08-28 19:43

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blog",
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
                ("title", models.CharField(max_length=255)),
                ("pub_date", models.DateTimeField()),
                ("body", models.TextField()),
                ("image", models.ImageField(upload_to="images/")),
            ],
        ),
    ]
