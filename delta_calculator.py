import math

print("Delta calculator:")
a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
c = int(input("Enter number c: "))

delta = (b*b) - 4 * a * c
print("Delta is equal: ", delta)

if (delta >= 0):
    sqrt_delta = (math.sqrt(delta))
else:
    print("Delta < 0, no solutions")
    quit()

x1 = (-b - sqrt_delta ) / 2 * a
x2 = (-b + sqrt_delta ) / 2 * a
x0 = -b / 2 * a

if (delta > 0):
    print("Delta > 0, 2 solutions:")
    print("x1 = ", x1)
    print("x2 = ", x2)
elif (delta == 0):
    print("Delta == 0, 1 solution")
    print("x0 = ", x0)

