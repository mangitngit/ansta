from decimal import Decimal


def generate_list():
    return [element * Decimal(0.1) for element in range(20, 60, 5)]
