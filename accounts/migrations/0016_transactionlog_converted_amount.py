# Generated by Django 5.0.6 on 2024-05-31 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0015_account_preferred_currency"),
    ]

    operations = [
        migrations.AddField(
            model_name="transactionlog",
            name="converted_amount",
            field=models.FloatField(null=True),
        ),
    ]
