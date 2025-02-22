# Generated by Django 5.1.3 on 2024-11-06 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="RequiredChat",
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
                ("chat_id", models.CharField(max_length=255, unique=True)),
                ("name", models.CharField(max_length=255)),
                (
                    "chat_type",
                    models.CharField(
                        choices=[("group", "Группа"), ("channel", "Канал")],
                        max_length=7,
                    ),
                ),
            ],
            options={
                "verbose_name": "Требуемый чат",
                "verbose_name_plural": "Требуемые чаты",
            },
        ),
    ]
