# Generated by Django 5.0.6 on 2024-05-28 10:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_transaction_transaction_amount"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="transaction",
            name="balance",
        ),
        migrations.AddField(
            model_name="transaction",
            name="transaction_type",
            field=models.CharField(
                choices=[("debit", "Debit"), ("credit", "Credit")],
                default="debit",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="account",
            name="email",
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="transaction_amount",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name="wallet",
            name="account",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="accounts.account"
            ),
        ),
    ]
