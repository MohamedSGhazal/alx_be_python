num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
wanted_opertaion = input("Choose the operation (+, -, *, /): ")
match wanted_opertaion:
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