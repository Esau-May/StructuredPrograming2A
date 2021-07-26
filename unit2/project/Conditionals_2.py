import sys

if __name__ == "__main__":

    num3=[]
    num5=[]


    low = int(input("Enter the lowest range:"))
    high = int(input("Enter the highest range:"))

    for i in range(low, high+1):
        if(i%3==0 and i%5==0):
            num3.append(i)
            num5.append(i)

        elif(i%3==0):
            num3.append(i)
            
        elif(i%5==0):
            num5.append(i)

    print("All the numbers divisible by 3:", num3)
    print("All the numbers divisible by 5:", num5)