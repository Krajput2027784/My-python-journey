while True:
    num1 = int(input("enter first number:"))
    num2 = int(input("enter second number:"))
  
    operator = input("Choose operation(+, -, *, /):")

    match operator:
     case"+":
        print("Result =",num1+num2)

     case"-":
        print("Result =",num1-num2)
 
     case"*":
        print("Result =",num1*num2)
 
     case"/":
       if num2 != 0:
        print("Result =",num1/num2)
 
       else:
        print("not divisible by zero")
 
     case _:
      print("invalid input") 

    choice = input("Do you want to use calculator? (yes/no):").lower()

    if choice != "yes":
       print("Thank you for using the calculator!🤝")
       break            