

if __name__ == '__main__':

    store = {"Monitor": 199.9, "Keyboard": 99.9, "Desktop Computer": 999.9, "Watch": 499, "Laptop": 1499, "Table": 800}

    price = float(input("Enter the maximum price: "))

    print("\nList of all the items in the store: ")

    for product in store:
        print(f"{product} : {store[product]}")

    print("\nList of affordable items: ")

    for product in store:
        if store[product] <= price:
            print(f"{product} : {store[product]}")
