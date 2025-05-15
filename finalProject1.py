import time

# Repeated Text
first_text = "I can see that the first number is "
second_text = "and the second is "
both_text = "So both of them are "
different_text = "So one is even and one is odd"

#Start of code
print("Hello, This is my final project")
name=input("What is your name?\n")
print("Hi " + name + ", nice to meet you!")
print("This is a special calculator, I would need you to input two numbers")
first_number =int( input("First Number: "))
second_number = int(input("Second Number: "))
print("Thank you for putting in your numbers",first_number, "and",second_number)

#Checking if the numbers are even or odd
if first_number % 2 == 0:
  print(first_text + "even")
  if second_number % 2 == 0:
    print(second_text + "even")
    print(both_text + "even")
  else:
    print(second_text + "odd") 
    print(different_text)
else:
  print(first_text + "odd")
  if second_number % 2 == 0:
    print(second_text + "even")
    print(different_text)
  else:
    print(second_text + "odd") 
    print(both_text + "even")

#checking if numbers are even or odd with flags
first_flag = False
second_flag = False
if first_number % 2 == 0:
  first_flag = True
  print(first_text + "even")
else:
  print(first_text + "odd")
if second_number % 2 == 0:
  print(second_text + "even")
  second_flag = True
else:
  print(second_text + "odd")

if(first_flag and second_flag):
  print(both_text + "even")
elif(first_flag or second_flag):
  print(different_text)
else:
  print(both_text + "odd")

#Arithmetics
operator = input("Operator (+, -, *, /): ")
if(operator == "+"):
  print(first_number ,"+" , second_number ,"=", first_number+second_number)
elif(operator == '-'):
  print(first_number ,"-", second_number ,"=", first_number-second_number)
elif(operator == '*'):
  print(first_number ,"*", second_number ,"=", first_number*second_number)
elif(operator == '/'):
  if(second_number==0):
    print("Error, cannot divide by 0")
  int_or_float = input("You chose division, should the result be integer? (y/n)")
  if(int_or_float == 'y'):
    print(first_number ,"/", second_number ,"=", first_number//second_number)
  else:
    print(first_number ,"/", second_number ,"=", first_number/second_number)
else:
  print("Error: operator",operator, "is not supported")

print("Thank you "+ name +" for using the calculator on",time.ctime())