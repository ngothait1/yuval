def inputNumber(name_of_input: str) -> int:
    number_input = input(f'{name_of_input}: ')
    while not number_input.isdigit():
        print(f'Error: {name_of_input} must be a number. {number_input} is not a number')
        number_input = input(f'{name_of_input}: ')
    return int(number_input)

