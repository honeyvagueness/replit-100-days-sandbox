### grade generator ###
print('Drew\'s grade calculator')
### beginning of code ###
test_name = input('Enter test name > ')
test_max_score = int(input('Enter maximum test score obtainable > '))
test_score_obtained = int(input('Enter score obtained > '))
test_score_percentage = test_score_obtained / test_max_score * 100
final_tsp = round(test_score_percentage, 2)
if final_tsp >= 90 and final_tsp <= 100:
  print('With a percentage of', final_tsp, 'in your', test_name, 'test your letter grade is', '\033[32m', 'A+')
elif final_tsp >= 80 and final_tsp <= 89:
  print('With a percentage of', final_tsp, 'in your', test_name, 'test your letter grade is', '\033[32m', 'A')
elif final_tsp >= 70 and final_tsp <= 79:
  print('With a percentage of', final_tsp, 'in your', test_name, 'test your letter grade is', '\033[33m', 'B')
elif final_tsp >= 60 and final_tsp <= 69:
  print('With a percentage of', final_tsp, 'in your', test_name, 'test your letter grade is', '\033[33m', 'C')
elif final_tsp >= 50 and final_tsp <= 59:
  print('With a percentage of', final_tsp, 'in your', test_name, 'test your letter grade is', '\033[31m', 'D')
elif final_tsp < 50:
  print('With a percentage of', final_tsp, 'in your', test_name, 'test your letter grade is', '\033[31m', 'U')
else:
  print('\033[31m', 'Error; Unknown type')
### end of code ###