import sys


if __name__ == "__main__":


    for Month in range(1,13):
        print("Month: ", Month)

        if Month==2:
            for Day in range(1,29):
                print("Day: ", Day)

        elif Month==4:
            for Day in range(1,31):
                print("Day: ", Day)

        elif Month==6:
            for Day in range(1,31):
                print("Day: ", Day)

        elif Month==9:
            for Day in range(1,31):
                print("Day: ", Day)

        elif Month==11:
            for Day in range(1,31):
                print("Day: ", Day)

        else:
            for Day in range(1,32):
                print("Day: ", Day)