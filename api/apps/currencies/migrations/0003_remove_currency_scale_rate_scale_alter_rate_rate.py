# Generated by Django 4.2 on 2024-03-06 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("currencies", "0002_currency_created_at_currency_updated_at_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="currency",
            name="scale",
        ),
        migrations.AddField(
            model_name="rate",
            name="scale",
            field=models.IntegerField(
                default=1, verbose_name="Количество единиц валюты"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="rate",
            name="rate",
            field=models.DecimalField(
                decimal_places=4, max_digits=8, verbose_name="Курс"
            ),
        ),
    ]