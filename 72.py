# Write a menu-driven Python program where the user can add items, remove items, view cart, and exit.
cart = []

while True:
    print("1. Add")
    print("2. Remove")
    print("3. View")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        item = input("Enter item: ")
        cart.append(item)

    elif choice == 2:
        item = input("Enter item: ")
        if item in cart:
            cart.remove(item)

    elif choice == 3:
        print(cart)

    elif choice == 4:
        break