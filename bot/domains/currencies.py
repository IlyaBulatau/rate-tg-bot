from enum import Enum


class AvalibaleCurrency(Enum):
    USD = "USD"
    EUR = "EUR"
    CZK = "CZK"
    KZT = "KZT"
    EGP = "EGP"
    RUB = "RUB"
    TRY = "TRY"

    @classmethod
    def to_list(cls):
        return [abbreviation.value for abbreviation in cls]
