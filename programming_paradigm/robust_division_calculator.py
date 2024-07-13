class ZeroDivisionError(Exception):
    pass


def safe_divide(numerator, denominator):
    try:
        if type(numerator) not in [int, float] or type(denominator) not in [int, float]:
            raise ValueError()
        elif denominator == 0:
            raise ZeroDivisionError()
        result = numerator / denominator
        return f"The result of the division is {result}"
    except ZeroDivisionError as e:
        return "Error: Cannot divide by zero."
    except ValueError as e:
        return "Error: Please enter numeric values only."
    