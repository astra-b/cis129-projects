#Version 2
#Updated by Astra Bavier - Oct 2 2024

#Coffee shop header
print('***************************************\nMy Coffee and Baked Goods Shop')

#Ask for purchase information
coffee = input('Number of coffees bought?\n')
muffin = input('Number of muffins bought?\n')
donut = input('Number of donuts bought?\n')
bagel = input('Number of bagels bought?\n')
print('***************************************\n')

#Calculate totals
coffee_cost = float(coffee) * 5.0
muffin_cost = float(muffin) * 4.0
donut_cost = float(donut) * 6.0
bagel_cost = float(bagel) * 4.5
total = coffee_cost + muffin_cost + donut_cost + bagel_cost
tax = (0.06 * total)
total = total + tax

#Convert floats to monetary values
coffee_cost = '$' + str(coffee_cost) + '0'
muffin_cost = '$' + str(muffin_cost) + '0'
donut_cost = '$' + str(donut_cost) + '0'
bagel_cost = '$' + str(bagel_cost) + '0'

#Check for plurality 
if int(coffee) == 1:  
    coffee_count = str(coffee) + ' Coffee'
else: 
    coffee_count = str(coffee) + ' Coffees'
if int(muffin) == 1:
    muffin_count = str(muffin) + ' Muffin'
else: 
    muffin_count = str(muffin) + ' Muffins'
if int(donut) == 1:
    donut_count = str(donut) + ' Donut'
else: 
    donut_count = str(donut) + ' Donuts'
if int(bagel) == 1:
    bagel_count = str(bagel) + ' Bagel'
else: 
    bagel_count = str(bagel) + ' Bagels'

#Print receipt
print('***************************************\nMy Coffee and Baged Goods Shop receipt\n', 
      coffee_count, ' at $5 each: ', coffee_cost, '\n', 
      muffin_count, ' at $4 each: ', muffin_cost,  '\n',
      donut_count, ' at $6 each:', donut_cost, '\n',
      bagel_count, 'at $4.50 each:', bagel_cost, 
      '\n6% tax: $', tax, 
      '\n---------\nTotal: $', total, 
      '\nThank you for your business!\n***************************************')

