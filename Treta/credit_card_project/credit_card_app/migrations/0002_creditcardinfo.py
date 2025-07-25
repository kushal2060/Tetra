# Generated by Django 5.0.1 on 2024-01-24 19:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("credit_card_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CreditCardInfo",
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
                ("email", models.EmailField(max_length=254, unique=True)),
                ("encrypted_credit_card", models.BinaryField()),
            ],
        ),
    ]
