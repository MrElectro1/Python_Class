# Eric Hayden 04/15/2021
# introduction to explain the purpose of the program
print ("This program will calculate how long an investment will take to double at a given interest rate.")
# obtaining the amount being invested
investment=float(input("Please enter the amount you will be investing.: "))
# obtaining the interst rate
rate=float(input("Please enter the annualized intrest rate that will be applied to the investment.: "))
# calculating
print("Calculating.......")
goal=investment*2
time=0
while investment <= goal:
    investment*=rate
    time+=1
print(f"It will take {time} years to reach double your innitial investment.")