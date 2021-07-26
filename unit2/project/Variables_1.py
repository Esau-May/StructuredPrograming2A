import sys

Numbers= 0
Add= 0
Average= 0

if __name__ == "__main__":


    for Numbers in range(1, len(sys.argv)):
        Add= (Add + float(sys.argv[Numbers]))
        Average= Add/Numbers
    print("The Average of Numbers is: ", Average)