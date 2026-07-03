while True:

 Marks1 = int(input("enter english marks :"))
 Marks2 = int(input("enter hindi marks :"))
 Marks3 = int(input("enter math's marks :"))
 Maxmarks = int(300)


 Total = int(Marks1 + Marks2 + Marks3)
 Percentage = (Total/Maxmarks)*100

 if Percentage >= 90:
    print("Grade : A")

 elif Percentage >= 80:
    print("Grade : B")

 elif Percentage >= 70:
    print("Grade : C")

 elif Percentage >= 60:
    print("Grade : D")

 else:
    print("fail")

 choice = input("Do you want to calculate? (yes/no):").lower()
 if choice != "yes":
       print("Thank You for using the calculator!")
       break