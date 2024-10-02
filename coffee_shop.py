#Version 1
#Created by Astra Bavier - Oct 2 2024

#Coffee shop header
print('***************************************\nMy Coffee and Muffin Shop')

#Ask for purchase information
coffee = input('Number of coffees bought?\n')
muffin = input('Number of muffins bought?\n')
print('***************************************\n')

#Calculate totals
coffee_cost = float(coffee) * 5.0
muffin_cost = float(muffin) * 4.0
total = coffee_cost + muffin_cost
tax = (0.06 * total)
total = total + tax

#Convert floats to monetary values
coffee_cost = '$' + str(coffee_cost) + '0'
muffin_cost = '$' + str(muffin_cost) + '0'

#Check for plurality 
if int(coffee) == 1:  
    coffee_count = str(coffee) + ' Coffees'
else: 
    coffee_count = str(coffee) + ' Coffee'
if int(muffin) == 1:
    muffin_count = str(muffin) + ' Muffins'
else: 
    muffin_count = str(muffin) + ' Muffin'

#Print receipt
print('***************************************\nMy Coffee and Muffin Shop receipt\n', coffee_count, ' at $5 each: ', coffee_cost, '\n', muffin_count, ' at $4 each: ', muffin_cost, '\n6% tax: $', tax, '\n---------\nTotal: $', total, '\n***************************************')

