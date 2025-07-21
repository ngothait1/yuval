from models import Person, Student, Employee
import pandas as pd
from menu_enum import MenuOption
from typing import Optional


def printMenu():
  print("1. Save a new entry\n"
        "2. Search by ID\n"
        "3. Print ages average\n" 
        "4. Print all names\n"
        "5. Print all IDs\n"
        "6. Print all entries\n"
        "7. Print entry by index\n"
        "8. Save all data\n"
        "9. Exit")


def inputNumber(name_of_input: str) -> int:
  number_input = input(f'{name_of_input}: ')
  while not number_input.isdigit():
    print(f'Error: {name_of_input} must be a number. {number_input} is not a number')
    number_input = input(f'{name_of_input}: ')
  return int(number_input)


def saveNewEntry(index_id_list: list[int], entries_dict: dict[int, Person], total_age: int) -> int:
  id = inputNumber("ID")
  if id in entries_dict:
    print(f'Error: ID already exists: {entries_dict[id]}')
    return total_age
  
  name = input("Name: ")
  age = inputNumber("Age")

  person_types = [Student, Employee, Person]

  print("Choose person type:")
  for i, cls in enumerate(person_types):
      print(f"{i}. {cls.__name__}")

  try:
      choice = int(input("Enter your choice: "))
      person_class = person_types[choice]
  except (ValueError, IndexError):
      print("Invalid selection.")
      return total_age

  person = person_class(name, age)
  
  index_id_list.append(id)
  entries_dict[id] = person
  total_age += age
  print(f'ID [{id}] saved successfully as a {person.__class__.__name__}')
  return total_age


def searchById(entries_dict: dict[int, Person]) -> None:
  id = inputNumber("Please enter the ID you want to look for")
  if not id in entries_dict :
    print(f'ID {id} is not saved')
    return
  person = entries_dict[id]
  printEntry(id, person)


def printAgesAvg(total_age: int, num_of_entries: int) -> None:
  if num_of_entries == 0:
    print("No entries yet")
    return
  avg = total_age/num_of_entries
  print(f'Average age: {avg}')


def printEntry(id: int, person: Person, index: Optional[int] = None, mode: str = "full") -> None:
  if mode == "all":
    print(f"{index}. {id}")
    print(person)
  elif mode == "names":
    print(f"{index}. {person.getName()}")
  elif mode == "ids":
    print(f"{index}. {id}")
  else:
    print(f"ID: {id}")
    print(person)
    

def printEntries(entries_dict: dict[int, Person], mode: str = "all") -> None:
  for index, id in enumerate(entries_dict):
    person = entries_dict[id]
    printEntry(id, person, index, mode)


def printEntryByIndex(index_id_list: list[int], entries_dict: dict[int, Person]) -> None:
  index = inputNumber("Please enter the index of the entry you want to print")
  if index >= len(index_id_list):
    print(f'Error: Index out of range. The maximum index allowed is {len(index_id_list) - 1}')
    return
  id = index_id_list[index]
  person = entries_dict[id]
  printEntry(id, person)


def exitMenu() -> str:
  while True:
    exit_input = input("Are you sure you want to exit? (y/n): ")
    if exit_input in ['y','n']:
      return exit_input


def waitForUser(message: str = "Press Enter to continue") -> None:
  input(message)


def saveToCsv(entries_dict: dict[int, Person]) -> None:
  csv_name = input("what is your output file name? ") + ".csv"
  
  rows = []
  for entry_id, person in entries_dict.items():
    row = {"ID": entry_id}
    row.update(person.to_dict())
    rows.append(row)

  df = pd.DataFrame(rows)
  df.to_csv(csv_name, index=False)


def menu() -> None:
  total_age = 0
  index_id_list = []
  entries_dict = {}
  while True:
    printMenu()
    try:
      choice_input = input("Please enter your choice: ")
      choice = MenuOption(int(choice_input))
    except ValueError:
      print(f"Invalid input: '{choice_input}' is not a number.")
      continue
    except KeyboardInterrupt:
      print("\nExiting gracefully. Goodbye!")
      break
    except Exception:
      print(f"Option '{choice_input}' does not exist. Please try again.")
      continue

    match choice:
      case MenuOption.SAVE_NEW:
        total_age = saveNewEntry(index_id_list, entries_dict, total_age)
      case MenuOption.SEARCH_BY_ID:
        searchById(entries_dict)
      case MenuOption.PRINT_AGE_AVG:
        printAgesAvg(total_age,len(entries_dict))
      case MenuOption.PRINT_NAMES:
        printEntries(entries_dict, "names")
      case MenuOption.PRINT_IDS:
        printEntries(entries_dict, "ids")
      case MenuOption.PRINT_ALL:
        printEntries(entries_dict, "all")
      case MenuOption.PRINT_BY_INDEX:
        printEntryByIndex(index_id_list,entries_dict)
      case MenuOption.SAVE_TO_CSV:
        saveToCsv(entries_dict)      
      case MenuOption.EXIT:
        if exitMenu() == 'y':
          print("Goodbye!")
          break

      case _:
        print(f'Option [{choice}] does not exist. Please try again')

    waitForUser()

menu()