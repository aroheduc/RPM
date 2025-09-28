# import math module
import math

a = int(input("Enter the first known number (a): "))
b = int(input("Enter the second known number (b): "))
c = int(input("Enter the third known number (c): "))

# calculating  the discriminant
dis = (b**2) - (4 * a*c)

if dis > 0:

    # find two results
    sol1 = (-b-math.sqrt(dis))/(2 * a)
    sol2 = (-b + math.sqrt(dis)) / (2 * a)

    # printing the results
    print('First solution: ', round(sol1), "\nSecond solution: ", round(sol2))

elif dis == 0:

    # find sole result
    sol = (b/(2 * a)) * -1

    # printing the result
    print('Single solution: ', round(sol))

else:

    print("No real roots; Two imaginary roots")

