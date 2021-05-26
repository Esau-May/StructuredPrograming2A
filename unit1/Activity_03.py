hours = 0
hoursext = 0
priceh = 1
priceext = 1.5
salary = 0

hours = int(input("How many hours did you work this week?"))

if (hours >= 40):
    hoursext = (hours - 40)
    hours = (hours - hoursext)
    salary = ((hours * priceh)+(hoursext * priceext))
else:
    salary = (hours * priceh)

print("Your salary is: $", salary)