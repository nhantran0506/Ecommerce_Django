# Generated by Django 4.1.13 on 2024-06-07 12:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Items",
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
                ("name", models.CharField(default="Items", max_length=250)),
                ("des", models.TextField(default="Item des")),
                ("price", models.FloatField(default=0.0)),
                ("sales_off", models.FloatField(default=0.0)),
                ("create", models.DateField()),
                ("update", models.DateField()),
                (
                    "belong_to",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="item",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
