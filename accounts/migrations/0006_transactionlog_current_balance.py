# Generated by Django 5.0.6 on 2024-05-28 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0005_remove_transactionlog_balance_after"),
    ]

    operations = [
        migrations.AddField(
            model_name="transactionlog",
            name="current_balance",
            field=models.FloatField(default=0.0),
        ),
    ]
