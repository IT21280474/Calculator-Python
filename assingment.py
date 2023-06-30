def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None

def power(a, b):
    return a ** b

def remainder(a, b):
    return a % b

def select_op(choice):
    if choice == '#':
        return -1
    elif choice in ('+', '-', '*', '/', '^', '%'):
        while True:
            first_num = input("Enter first number: ")
            second_num = input("Enter second number: ")
            try:
                num1 = float(first_num)
                num2 = float(second_num)
                break
            except ValueError:
                print("Not a valid number, please enter again")

        try:
            if choice == '+':
                print(f"{num1} + {num2} = {add(num1, num2)}")

            elif choice == '-':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '*':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '/':
                result = divide(num1, num2)
                if result is not None:
                    print(f"{num1} / {num2} = {result}")

            elif choice == '^':
                print(f"{num1} ^ {num2} = {power(num1, num2)}")

            elif choice == '%':
                print(f"{num1} % {num2} = {remainder(num1, num2)}")

        except:
            print("Something Went Wrong")

    elif choice == '$':
        return 0

    else:
        print("Error: Unrecognized operation")
        return None



#End the select_op(choice) function here
#-------------------------------------
#This is the main loop. It covers Task 1 (Section 1)
#YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE
while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  

  # take input from the user
  choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
  print(choice)
  if(select_op(choice) == -1):
    #program ends here
    print("Done. Terminating")
    exit()