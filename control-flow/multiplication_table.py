number = int(input("Enter a number to see its multiplication table: "))
for Y in range(1, 11):
 X = number
 Z = X * Y
 print(str(X) + str(" * ") + str(Y) + str(" = ") + str(Z))