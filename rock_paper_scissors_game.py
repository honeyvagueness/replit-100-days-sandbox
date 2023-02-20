### replit day 14 r p s game ###
print('Drew\'s rock, paper, scissors game')
print('\033[31m', 'r = rock, p = paper, s = scissors', '\033[0m')
### beginning of code ###
player1_name = input('Player 1 name > ')
player2_name = input('Player 2 name > ')
from getpass import getpass as input
print(player1_name, 'turn')
player1_move = input('Enter move here > ')
print(player2_name, 'turn')
player2_move = input('Enter move here > ')
if player1_move == "r":
  if player2_move == "r":
    print('You both chose rock')
  elif player2_move == "p":
    print('\033[32m', player2_name, 'wins🥳', '\033[0m')
    print('Rock is wrapped by paper')
  elif player2_move == "s":
    print('\033[32m', player1_name, 'wins🥳', '\033[0m')
    print('Rock smashes scissors')
  else:
    print('\033[31m', 'Error: invalid entry', '\033[0m')
elif player1_move == "p":
  if player2_move == "r":
    print('\033[32m', player1_name, 'wins🥳', '\033[0m')
    print('Paper wraps rock')
  elif player2_move == "p":
    print('You both chose paper')
  elif player2_move == "s":
    print('\033[32m', player2_name, 'wins🥳', '\033[0m')
    print('Paper is shredded by scissors')
  else:
    print('\033[31m', 'Error: invalid entry', '\033[0m')
elif player1_move == "s":
  if player2_move == "r":
    print('\033[32m', player2_name, 'wins🥳', '\033[0m')
    print('Scissors is smashed by rock')
  elif player2_move == "p":
    print('\033[32m', player1_name, 'wins🥳', '\033[0m')
    print('Scissors shreds paper')
  elif player2_move == "s":
    print('You both chose scissors')
  else:
    print('\033[31m', 'Error: invalid entry', '\033[0m')
else:
  print('\033[31m', 'Error: invalid entry', '\033[0m')
    ### end of code ###