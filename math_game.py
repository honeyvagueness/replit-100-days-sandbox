### Drew's math game ###
### Think you're good with multiplications... well let's see about that ###
### beginning of program ###
print('Drew\'s math game')
print('Pick a number and I will give you 10 math facts to solve.')
### beginning of code ###
mul = int(input('Choose your number of choice to be multiplied > '))
counter = 0
for i in range(1, 11):
  ans = i * mul
  print(i, 'x', mul, '=')
  res = int(input('> '))
### end of program ###
  if res == ans:
    print('\033[32m', 'Correct!', '\033[0m')
    counter += 1
  else:
    print('\033[31m', 'Wrong!!','\033[0m', 'the answer is', ans )

if counter == 10:
  print('Yayy!!!, you got it all correct')
  print('You got', counter, 'out of 10 correct.')
elif counter < 5:
  print('That\'s poor')
  print('You got', counter, 'out of 10 correct.')
elif counter == 5:
  print('Average, You got it halfway correctly')
  print('You got', counter, 'out of 10 correct.')
elif counter > 5 or counter == 9:
  print('Beyond average, congrats')
  print('You got', counter, 'out of 10 correct.')
else:
  print('Unknown score')
### end of code ###
### Drewbox ###