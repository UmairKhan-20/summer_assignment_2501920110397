# program to create inventory management system
inventory = []
while True:
    print("    Inventory Management System    ")
    print("1. Add Item")
    print("2. View Items")
    print("3. Update Item")
    print("4. Delete Item")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        item_id = input("Enter item ID: ")
        item_name = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        item = {"item_id": item_id, "item_name": item_name, "quantity": quantity}
        inventory.append(item)
    elif choice == 2:
        for i in inventory:
            print("Item ID:", i["item_id"], "Item Name:", i["item_name"], "Quantity:", i["quantity"])
    elif choice == 3:
        update_id = input("Enter item ID to update: ")
        if update_id in inventory:
            qty=int(input("Enter new quantity: "))
            inventory[update_id]=qty
            print("Item updated successfully")
        else:
            print("Item not found")
    elif choice == 4:
        delete_id = input("Enter item ID to delete: ")
        found=False
        for i in inventory:
            if i["item_id"]==delete_id:
                inventory.remove(i)
                print("Item deleted successfully")
                found=True
                break
        if not found:
            print("Item not found")
    elif choice == 5:
        print("Exit")
        break
    else:
        print("Invalid choice")