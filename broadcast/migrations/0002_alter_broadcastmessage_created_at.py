# Generated by Django 5.1.3 on 2024-11-07 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("broadcast", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="broadcastmessage",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Дата создания"),
        ),
    ]