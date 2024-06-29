num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")
match operation:
 case "+":
  sum = num1 + num2
  print("The result is " + str(sum))
 case "-":
  subtract = num1 - num2
  print("The result is " + str(subtract))
 case "*":
  multiply = num1 * num2
  print("The result is " + str(multiply))
 case "/":
  divide = num1 / num2
  print("The result is " + str(divide))