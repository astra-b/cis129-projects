#Module 4 Lab

#declare local variables
monthlySales = 0 
storeAmount = 0
empAmount = 0
salesIncrease = 0
prompt = "How much did the store earn this month? "

#get monthly sales
monthlySales = float(input(prompt))

#determine storeAmount bonus
if monthlySales >= 110000:
    storeAmount = 6000
elif monthlySales >= 100000:
    storeAmount = 5000
elif monthlySales >= 90000:
    storeAmount = 4000
elif monthlySales >= 80000:
    storeAmount = 3000
else:
    storeAmount = 0

#get percent sale increase
salesIncrease = float(input("By what percentage did sales increase this month? "))
salesIncrease = salesIncrease / 100

#determine empAmount bonus
if salesIncrease >= .05:
    empAmount = 75
elif salesIncrease >= .04:
    empAmount = 50
elif salesIncrease >= .03:
    empAmount = 40
else:
    empAmount = 0

#print bonus information
print("The store bonus amount is $", storeAmount)
print("The employee bonus amount is $", empAmount)
if (storeAmount == 6000) and (empAmount == 75):
    print("Congrats! You have reached the highest bonus amounts possible!")