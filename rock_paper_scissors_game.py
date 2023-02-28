### replit day 14 r p s game ###
### listing global parameters ###
### taking names in ###
counter = 0
player1_score = 0
player2_score = 0
player1_name = input('Player 1 name > ')
player2_name = input('Player 2 name > ')
while True:
  print('Drew\'s rock, paper, scissors game')
  print('\033[31m', 'r = rock, p = paper, s = scissors', '\033[0m')
### beginning of code ###
  from getpass import getpass as input
  ### any input taken after this comment will not be displayed ###
  print(player1_name, 'turn')
  player1_move = input('Enter move here > ')
  print(player2_name, 'turn')
  player2_move = input('Enter move here > ')
  if player1_move == "r":
    if player2_move == "r":
      counter += 1
      print('You both chose rock')
    elif player2_move == "p":
      player2_score += 1
      counter += 1
      print('\033[32m', player2_name, 'wins🥳', '\033[0m')
      print('Rock is wrapped by paper') 
    elif player2_move == "s":
      counter += 1
      player1_score += 1
      print('\033[32m', player1_name, 'wins🥳', '\033[0m')
      print('Rock smashes scissors')
    else:
      print('\033[31m', 'Error: invalid entry', '\033[0m')
  elif player1_move == "p":
    if player2_move == "r":
      counter += 1
      player1_score += 1
      print('\033[32m', player1_name, 'wins🥳', '\033[0m')
      print('Paper wraps rock')
    elif player2_move == "p":
      print('You both chose paper')
    elif player2_move == "s":
      counter += 1
      player2_score += 1
      print('\033[32m', player2_name, 'wins🥳', '\033[0m')
      print('Paper is shredded by scissors')
    else:
      print('\033[31m', 'Error: invalid entry', '\033[0m')
  elif player1_move == "s":
    if player2_move == "r":
      counter += 1
      player2_score += 1
      print('\033[32m', player2_name, 'wins🥳', '\033[0m')
      print('Scissors is smashed by rock')
    elif player2_move == "p":
      counter += 1
      player1_score += 1
      print('\033[32m', player1_name, 'wins🥳', '\033[0m')
      print('Scissors shreds paper')
    elif player2_move == "s":
      print('You both chose scissors') 
      continue
    else:
      print('\033[31m', 'Error: invalid entry', '\033[0m')
  else:
    print('\033[31m', 'Error: invalid entry', '\033[0m')
  if counter == 3:
    break
  else:
    print('no score recorded')
print(player1_name, 'scored', player1_score)
print(player2_name, 'scored', player2_score)
    ### code retains score now and only allows 3 rounds... thus, it prints result after 3 rounds ###
    ### end of code ###
