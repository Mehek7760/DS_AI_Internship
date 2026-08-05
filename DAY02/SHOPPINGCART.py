# Fruit Shopping Cart - CRUD Application (0-Based Indexing)

cart = []

while True:
    print("\n========== FRUIT SHOPPING CART ==========")
    print("1. Add Fruit")
    print("2. View Cart")
    print("3. Update Fruit")
    print("4. Delete Fruit")
    print("5. Checkout")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # CREATE
    if choice == "1":
        fruit = input("Enter fruit name: ")
        cart.append(fruit)
        print(f"{fruit} added to cart.")

    # READ
    elif choice == "2":
        if len(cart) == 0:
            print("Shopping cart is empty.")
        else:
            print("\nShopping Cart:")
            for i in range(len(cart)):
                print(f"{i} : {cart[i]}")
            print("Total items in cart:", len(cart))

    # UPDATE
    elif choice == "3":
        if len(cart) == 0:
            print("Shopping cart is empty.")
        else:
            print("\nCurrent Shopping Cart:")
            for i in range(len(cart)):
                print(f"{i} : {cart[i]}")

            index = int(input("Enter index to update: "))

            if 0 <= index < len(cart):
                new_fruit = input("Enter new fruit name: ")
                cart[index] = new_fruit
                print("Item updated successfully.")
            else:
                print("Invalid index.")

    # DELETE
    elif choice == "4":
        if len(cart) == 0:
            print("Shopping cart is empty.")
        else:
            print("\nCurrent Shopping Cart:")
            for i in range(len(cart)):
                print(f"{i} : {cart[i]}")

            index = int(input("Enter index to delete: "))

            if 0 <= index < len(cart):
                removed = cart.pop(index)
                print(f"{removed} removed from cart.")
            else:
                print("Invalid index.")

    # CHECKOUT
    elif choice == "5":
        print("\n========== CHECKOUT ==========")

        if len(cart) == 0:
            print("Shopping cart is empty.")
        else:
            print("Final Shopping Cart:")
            for i in range(len(cart)):
                print(f"{i} : {cart[i]}")

            print("Total items in cart:", len(cart))

            # Convert list to tuple
            cart = tuple(cart)

            print("\nShopping Cart after Checkout (Tuple):")
            print(cart)

        break

    # EXIT
    elif choice == "6":
        print("Thank you for shopping!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 6.")