class Calculator:
    def calculateDiscount(self, purchase_amount, discount_percent):
        if purchase_amount < 0 or discount_percent < 0 or discount_percent > 100:
            raise ArithmeticException("Невалидные аргументы")
        discount_amount = purchase_amount * (discount_percent / 100)
        return purchase_amount - discount_amount


class ArithmeticException(Exception):
    pass


if __name__ == '__main__':
    c = Calculator()
    print(c.calculateDiscount(12543, 120))

