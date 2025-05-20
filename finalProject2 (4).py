#Final Project 2
def printMenu():
  print("1. Save a new entry\n"
        "2. Search by ID\n"
        "3. Print ages average\n" 
        "4. Print all names\n"
        "5. Print all IDs\n"
        "6. Print all enteries\n"
        "7. Print entry by index\n"
        "8. Exit")

def saveNewEntry(index_id_list,enteries_dict,total_age):
  id = input("ID: ")
  if(not id.isdigit()):
    input(f'Error: ID must be a number. {id} is not a number\nPress Enter to continue')
    return total_age
  if(id in enteries_dict):
    input(f'Error: ID already exists: {enteries_dict[id]}\nPress Enter to continue')
    return total_age
  name = input("Name: ")
  age = input("Age: ")
  if(not age.isdigit()):
    input(f'Error: Age must be a number. {age} is not a number\nPress Enter to continue')
    return total_age
  age = int(age)
  index_id_list.append(id)
  enteries_dict[id]=({"Name":name,"Age":age})
  total_age += age
  input(f'ID [{id}] saved successfuly\nPress Enter to continue')
  return total_age

def searchById(enteries_dict):
  id = input("Please enter the ID you want to look for: ")
  if(not id.isdigit()):
    input(f'Error: ID must be a number. {id} is not a number\nPress Enter to continue')
    return
  if(not id in enteries_dict):
    input(f'ID {id} is not saved\nPress Enter to continue')
    return
  entry = enteries_dict[id]
  name = entry['Name']
  age = entry['Age']
  input(f'ID: {id}\nName: {name}\nAge:{age}\nPress Enter to continue')

def printAgesAvg(total_age,num_of_enteries):
  if num_of_enteries == 0:
    input("No enteries yet!\nPress Enter to continue")
    return
  avg = total_age/num_of_enteries
  input(f'Average age: {avg}\nPress Enter to continue')

def printNames(enteries_dict):
  for index,id in enumerate(enteries_dict):
    entry = enteries_dict[id]
    name = entry['Name']
    print(f'{index}. {name}')
  input('Press Enter to continue')

def printIds(index_id_list):
  for i in range(len(index_id_list)):
    print(f'{i}. {index_id_list[i]}')
  input('Press Enter to continue')

def printEnteries(enteries_dict):
  index = 0
  for item_tuple in enteries_dict.items():
    id = item_tuple[0]
    value = item_tuple[1]
    name = value['Name']
    age = value['Age']
    print(f'{index}. Id: {id}\n   Name: {name}\n   Age: {age}')
    index+=1
  input('Press Enter to continue')

def printEntryByIndex(index_id_list,enteries_dict):
  index = input("Please enter the index of the entry you want to print: ")
  if(not index.isdigit()):
    input(f'Error: Index must be a number. {index} is not a number\nPress Enter to continue')
    return
  index = int(index)
  if(index >= len(index_id_list)):
    input(f'Error: Index out of range. The maximum index allowed is {len(index_id_list)}')
    return
  id = index_id_list[index]
  name = enteries_dict[id]['Name']
  age = enteries_dict[id]['Age']
  input(f'ID: {id}\nName: {name}\nAge:{age}\nPress Enter to continue')

def exitMenu():
  while True:
    exit = input("Are you sure you want to exit? (y/n): ")
    if(exit == 'y' or exit == 'n'):
      return exit

def menu():
  total_age = 0
  index_id_list = []
  enteries_dict = {}
  while True:
    printMenu()
    choice = input("Please enter your choice: ")
    match choice:
      case '1':
        total_age = saveNewEntry(index_id_list,enteries_dict,total_age)
      case '2':
        searchById(enteries_dict)
      case '3':
        printAgesAvg(total_age,len(enteries_dict))
      case '4':
        printNames(enteries_dict)
      case '5':
        printIds(index_id_list)
      case '6':
        printEnteries(enteries_dict)
      case '7':
        printEntryByIndex(index_id_list,enteries_dict)
      case '8':
        if exitMenu() == 'y':
          print("Goodbye!")
          break
      case _:
        print(f'Option [{choice}] does not exist. Please try again')

menu()

