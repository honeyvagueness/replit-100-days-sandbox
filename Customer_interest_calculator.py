### This is a remake of my first ever python program.... I'm looking forward to making it more complex and upgraded ###
### This is to be an interest calculator in respect to deposit... hopefully it works out I'll share more details at the end of the code ###
### beginning of code ###
deposit = int(input('Enter your deposit > '))
interest_1 = deposit * 0.05
interest_2 = deposit * 0.075
interest_3 = deposit * 0.09
new_balance_1 = deposit + interest_1
new_balance_2 = deposit + interest_2
new_balance_3 = deposit + interest_3

if deposit < 5000:
  print('You deposited', deposit)   
  print('An interest of', interest_1, 'was added to your deposit')
  print('Your new balance is', new_balance_1)
elif deposit >= 5000 and deposit == 20000:
  print('You deposited', deposit)   
  print('An interest of', interest_2, 'was added to your deposit')
  print('Your new balance is', new_balance_2)
elif deposit > 200000:
  print('You deposited', deposit)   
  print('An interest of', interest_3, 'was added to your deposit')
  print('Your new balance is', new_balance_3)
else:
  print('Unknown entry')
### end of code ###
### While writing this code i thought of an idea.... of creating an admin program that enables the user preset their interest rates.... but the problem is linking the programs together let's see how that works out ###
# Drewbox #