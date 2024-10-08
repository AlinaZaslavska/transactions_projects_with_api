# Generated by Django 5.0.6 on 2024-05-28 11:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_remove_transaction_balance_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="transaction_amount",
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name="wallet",
            name="balance",
            field=models.FloatField(default=0.0),
        ),
        migrations.CreateModel(
            name="TransactionLog",
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
                ("transaction_time", models.DateTimeField(auto_now_add=True)),
                ("transaction_type", models.CharField(max_length=10)),
                ("transaction_amount", models.FloatField()),
                ("balance_before", models.FloatField()),
                ("balance_after", models.FloatField()),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.account",
                    ),
                ),
            ],
        ),
    ]
