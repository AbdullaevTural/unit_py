class Calculator:
    @staticmethod
    def calculation(first_operand: int, second_operand: int, operator: str):
        result: int

        match operator:
            case '+':
                result: int = first_operand + second_operand
            case '-':
                result: int = first_operand - second_operand
            case '*':
                result: int = first_operand * second_operand
            case '/':
                if second_operand != 0:
                    result: float = first_operand / second_operand
                else:
                    raise ArithmeticError('Division by zero is not possible')
            case _:
                raise ValueError('Unexpected value operator: ' + operator)

        return result

    @staticmethod
    def calculate_discount(amount: int, discount: int) -> float:
        if isinstance(amount, int) and isinstance(discount, int):
            if amount < 0:
                raise ArithmeticError('Скидка не может быть меньше нуля')
            if not 0 <= discount <= 100:
                raise ArithmeticError('Скидка от 0 до 100 процентов')
            return amount * (amount - discount / 100)
        else:
            raise TypeError('На ввод только числа')