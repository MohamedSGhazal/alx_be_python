def perform_operation(num1, num2, operation):
        if operation == "add":
            return num1 + num2
        elif operation == "subtract":
            return num1 - num2
        elif operation == "multiply":
            return num1 * num2
        elif operation == "divide":
            if num2 == 0:
                 return "number 2 can't be zero"
            return num2 / num1
        else:
            raise ValueError("Invalid operation")