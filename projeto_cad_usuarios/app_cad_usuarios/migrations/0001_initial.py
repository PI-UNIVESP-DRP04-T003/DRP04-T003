# Generated by Django 5.0.2 on 2024-03-30 11:42

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="usuario",
            fields=[
                ("id_usuario", models.AutoField(primary_key=True, serialize=False)),
                ("nome", models.TextField(max_length=255)),
                ("rs", models.TextField(max_length=255)),
            ],
        ),
    ]
