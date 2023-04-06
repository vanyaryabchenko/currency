from decimal import Decimal


def to_2_point_decimal(value: str) -> Decimal:
    return round(Decimal(value), 2)
