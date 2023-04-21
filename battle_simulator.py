### DREWBOX BATTLE SIMULATOR ###
import os, random, time

def dice_roll(side):
  res = random.randint(1, side)
  return res

def health():
  health1 = (dice_roll(6) * dice_roll(12)) / 2
  health = health1 + 10
  return health

def strength():
  strength1 = (dice_roll(6) * dice_roll(12)) / 2
  strength = strength1 + 12
  return strength
print("⚔️ BATTLE TIME ⚔️")
print()
c1Name = input("Name your Legend:\n")
c1Type = input("Character Type (Human, Elf, Wizard, Orc):\n")
print()
print(c1Name)
c1Health = health()
c1Strength = strength()
print("HEALTH:", c1Health)
print("STRENGTH:", c1Strength)
print()
print("Who are they battling?")
print()


c2Name = input("Name your Legend:\n")
c2Type = input("Character Type (Human, Elf, Wizard, Orc):\n")
print()
print(c2Name)
c2Health = health()
c2Strength = strength()
print("HEALTH:", c2Health)
print("STRENGTH:", c2Strength)
print()
round = 1
winner = None
while True:
  time.sleep(1)
  os.system("clear")
  print("⚔️ DREWBOX BATTLE TIME ⚔️")
  print()
  print("The battle begins!")
  c1Dice = dice_roll(6)
  c2Dice = dice_roll(6)
  difference = abs(c1Strength - c2Strength) + 1
  if c1Dice > c2Dice:
    c2Health -= difference
    if round==1:
      print(c1Name, "wins the first blow")
    else:
      print(c1Name, "wins round", round)
  elif c2Dice > c1Dice:
    c1Health -= difference
    if round==1:
      print(c2Name, "wins the first blow")
    else:
      print(c2Name, "wins round", round)
  else:
    print("Their swords clash and they draw round", round)
  print()
  print(c1Name)
  print("HEALTH:", c1Health)
  print()
  print(c2Name)
  print("HEALTH:", c2Health)
  print()
  if c1Health<=0:
    print(c1Name, "has died!")
    winner = c2Name
    break
  elif c2Health<=0:
    print(c2Name, "has died!")
    winner = c1Name
    break
  else:
    print("And they're both standing for the next round")
    round += 1
    
time.sleep(5)
os.system("clear")
print("⚔️DREWBOX BATTLE TIME ⚔️")
print()
print(winner, "has won in", round, "round(s)")
