def add(a,b):
    return a+b 

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a,b):
    try:
        return a/b
    except Exception as e:
        print(e)

def power(a, b):
    return a ** b

def remainder(a, b):
    return a % b

#-------------------------------------
#TODO: Write the select_op(choice) function here
#This function sould cover Task 1 (Section 2) and Task 3
def select_op(choice):
    if choice == '#':
        return -1
    elif(choice in('+','-','*','/','^','%')):
         while True:
            firstnum = input ("Enter first number: ")  
            print(firstnum)
            secondtnum = input ("Enter second number: ")  
            print(secondtnum)
            try:
                num1 = float(firstnum)
                num2 = float(secondtnum)
                break
            except:
                print("Not a valid number,please enter again")
                continue
            
           
            

    if choice == '+':
        print(num1, '+' , num2, '=', add(num1,num2))

    elif choice == '-':
        print(num1, '-' , num2, '=', subtract(num1,num2))

    elif choice == '*':
        print(num1, '*' , num2, '=', multiply(num1,num2))

    elif choice == '/':
        print(num1, '/' , num2, '=', divide(num1,num2))

    elif choice == '**':
        print(num1, '**' , num2, '=', power(num1,num2))



   



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