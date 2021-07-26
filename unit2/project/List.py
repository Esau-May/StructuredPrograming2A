import sys
from statistics import mean


tempF = [63, 73, -999, 91, 86, 82, 72, 81, 66, 77, 75, 104, -999, 84, 77, 66, 82, 63, 93, 72, 82, 64, 75 , 90, 64, -999, 99, 82, 95, 82]

tempC = []


if __name__ == "__main__":

    remove = tempF.count(-999)
    for i in range (0, remove):
        tempF.remove(-999)

    for j in range(0, len(tempF)):
        tempC.append(round((tempF[j]-32)*(5/9)))
    print("The Celcius list is: \n", tempC)

    print("\n The maximum value in Celsius is:", max(tempC))
    print("\n The average in Celsius is:", mean(tempC))