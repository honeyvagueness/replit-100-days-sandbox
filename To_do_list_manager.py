todolist = []
import time, os

def printList():
  print()
  for item in todolist:
    print(item)
    time.sleep(1.0)


def editList():
  if item in todolist:
    todolist.remove(item)
  else:
    print(f"{item} is not in list, would you like to view to check? ")
    check = input('>')
    if check == "yes":
      printList()
    else:
      print('\033[31m', 'invalid entry', '\033[0m')
print('\t To-Do-List Manager')
while True:
  menu = print('Do you want to view, add, or edit your to-do-list?')
  menu = input('>')
  if menu == 'view':
    printList()
  elif menu == 'add':
    print("What would you like to add to your list?")
    item = input('>')
    print()
    todolist.append(item)
  elif menu == 'edit':
    print('What item have you completed?')
    item = input('>')
    editList()

  time.sleep(1.0)
  os.system('clear')
  
### run to check ###
### drewbox ###
### SAASS codes ###
