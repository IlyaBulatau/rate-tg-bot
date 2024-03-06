from django.db import models


class Currency(models.Model):
    abbreviation = models.CharField(
        verbose_name="Буквенный код валюты", max_length=3, unique=True
    )
    name_ru = models.CharField(verbose_name="Имя на русском", max_length=128)
    name_eng = models.CharField(verbose_name="Имя на английском", max_length=128)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "currencies"
        indexes = [
            models.Index(fields=["abbreviation"]),
        ]
        verbose_name = "Валюта"
        verbose_name_plural = "Валюты"

    def __str__(self):
        return f"{self.abbreviation}:{self.name_ru}"


class Rate(models.Model):
    date = models.DateField(verbose_name="Дата установки курса")
    rate = models.DecimalField(verbose_name="Курс", max_digits=8, decimal_places=4)
    scale = models.IntegerField(verbose_name="Количество единиц валюты")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    currency_abbreviation = models.ForeignKey(
        Currency,
        verbose_name="Код валюты",
        on_delete=models.PROTECT,
        related_name="rates",
        to_field="abbreviation",
    )

    class Meta:
        db_table = "rates"
        indexes = [
            models.Index(fields=["date"]),
        ]
        unique_together = ("currency_abbreviation", "date")
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return f"Курс валюты {self.currency_abbreviation.abbreviation} на {self.date}"
