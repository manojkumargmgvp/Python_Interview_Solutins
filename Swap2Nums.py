# Swap 2 Numbers Using 3rd variable

var_1 = int(input("enter the number:"))

var_2 = int(input("enter the number:"))

Temp = var_1

Var_1 = var_2

var_2 = Temp

print(Var_1)
print(var_2)

# without 3rd Variable

a = int(input("enter the number:"))
b = int(input("enter the number:"))
a,b = b,a
print(a,b)

# Another method
a = 10
b = 20
a = a+b
b = a-b
a = a-b
print(a,b)
