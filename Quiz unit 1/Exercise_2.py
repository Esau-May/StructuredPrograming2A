from typing import List


num1 = 0
num2 = 0
num3 = 0

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if (num1 == num2 == num3):
    print ("There are no greatest number")
else:
    list = [num1, num2, num3]
    print ("The greatest number is: ", max(list))
