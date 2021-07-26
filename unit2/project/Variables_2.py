import sys


Adition= 0
Substraction= 0
Multiplication= 0
Division= 0

Number1= int(sys.argv[1])
Number2= int(sys.argv[2])

if __name__ == "__main__":
    Adition= Number1+Number2
    print(f'The adition is: {Adition}')

    Substraction= Number1-Number2
    print(f'The substraction is: {Substraction}')

    Multiplication= Number1*Number2
    print(f'The multiplication is: {Multiplication}')

    Division= Number1/Number2
    print(f'The division is: {Division}')