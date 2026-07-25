print("===== ATM SIMULATION =====")

balance = 5000
pin = "1234"

user_pin = input("Enter PIN: ")

if user_pin == pin:

    while True:
        print("\n===== MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change PIN")
        print("5. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            print("Balance: ₹", balance)

        elif choice == "2":
            amount = int(input("Enter Amount: "))
            balance += amount
            print("Money Deposited!")
            print("Balance: ₹", balance)

        elif choice == "3":
            amount = int(input("Enter Amount: "))

            if amount <= balance:
                balance -= amount
                print("Money Withdrawn!")
                print("Balance: ₹", balance)
            else:
                print("Insufficient Balance!")

        elif choice == "4":
            old_pin = input("Enter Old PIN: ")

            if old_pin == pin:
                pin = input("Enter New PIN: ")
                print("PIN Changed Successfully!")
            else:
                print("Incorrect PIN!")

        elif choice == "5":
            print("Thank You!")
            break

        else:
            print("Invalid Choice!")

else:
    print("Incorrect PIN!")