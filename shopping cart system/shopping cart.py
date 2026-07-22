print("===== Shopping Cart =====")

cart = []

while True:
    print("\n1. Add Product")
    print("2. View Cart")
    print("3. Remove Product")
    print("4. Total Bill")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        name = input("Enter Product Name: ")
        price = int(input("Enter Price: "))
        cart.append((name, price))
        print("Product Added!")

    elif choice == "2":
        if cart:
            for item in cart:
                print(item)
        else:
            print("Cart is Empty!")

    elif choice == "3":
        name = input("Enter Product Name: ")
        found = False

        for item in cart:
            if item[0].lower() == name.lower():
                cart.remove(item)
                print("Product Removed!")
                found = True
                break

        if not found:
            print("Product Not Found!")

    elif choice == "4":
        total = 0

        for item in cart:
            total += item[1]

        print("Total Bill = ₹", total)

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")