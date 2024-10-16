# Lab 5 The Bottle Return Program

# Step 1: Declare variables below 
totalBottles = 0
counter = 1
todayBottles = 0
totalPayout = 0
keepGoing = 'y'
	
# Step 2: Loop to run program again
while keepGoing == 'y':
    totalBottles = 0
    totalPayout = 0
    counter = 1

# Step 3: Code to set value of variables
# code to set value of variable totalBottles 
    while counter <= 7:
        todayBottles = int(input("Enter number of bottles returned  for day #{}: ".format(counter)))
        totalBottles += todayBottles
        counter += 1
# code to set value of variable totalPayout
# code to print the number of total bottles and total payout
    totalPayout = totalBottles * 0.10
    print('\nThe total number of bottles collected is', totalBottles)
    print('The total paid out is $', f"{totalPayout:.2f}", "\n", sep='')
    print("Do you want to enter another week’s worth of data?")
    keepGoing = input("(Enter y or n):")