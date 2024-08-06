def menu():
    print("\nMain Menu:")
    print("1. View the store")
    print("2. Purchase an item")
    print("3. Update a purchased item")
    print("4. Remove an item")
    print("5. View Cart")
    print("6. Exit and Generate Invoice")
  
store_items = {
    1: ("Apple  ", 20.0),
    2: ("Banana ", 60.0),
    3: ("Grapes ", 25.0),
    4: ("Strawberry  ", 40.0),
    5: ("Orange", 50.0),
    6: ("Kiwi", 60.0)
}
 
# Empty Cart
cart = {}

def update_item(item_id, quantity):       
    cart[item_id] = quantity
    print(f"Quantity for {store_items[item_id][0]} updated to {quantity}.")
    
def view_store(): 
    print("*"*45)
    print("Id"," "*10 ,"Name" ," "* 14," Price ")
    print("*"*45)
    for item_id, (item_name, item_price) in store_items.items():
        print(item_id ,10*" ",item_name,15*" ",item_price)
   
def purchase_item(item_id, quantity): 
    if item_id in store_items:
        if item_id in cart:
            cart[item_id] += quantity
        else:
            cart[item_id] = quantity
        print(f"{quantity} {store_items[item_id][0]} added to cart.")
    else:
        print("Item not found in store.")
 
def remove_item(item_id):
    del cart[item_id]
    print("items removed from cart.") 
 
def view_cart():
   
    sum = 0
    print("*"*40)
    print("Purchased item")
    print("*"*40)
    for item_id, quantity in cart.items():
        item_name, item_price = store_items[item_id]
        total_price = item_price * quantity
        sum +=total_price
        print(f"{item_id} {item_name} {item_price} {quantity} {total_price}")
    
def generate_invoice():
    total_price=0
    total=0
    with open("invoice.txt", "w") as file:
        file.write("--------------Invoice Copy--------------\n")       
        for item_id, quantity in cart.items():
            item_name, item_price = store_items[item_id]
            total_price = item_price * quantity
            total +=total_price           
            file.write(f"\n{item_id} {item_name} {item_price} {quantity} {total_price}")
      
        file.write(f"\ntotal amount:: {total}")       
   
menu()
while True:   
    choice = int(input("\n Enter your choice: "))
 
    if choice == 1:
        view_store()
 
    elif choice == 2:       
        item_id = int(input("Enter item ID to purchase: "))                   
        if item_id not in store_items.keys():
            print("item not present in store")
   
        else:
            quantity = int(input("Enter quantity to purchase: "))
            purchase_item(item_id, quantity)
        while True:
            option=input("Add more items? (y/n): ")
            if option.lower()=='y':
 
                item_id = int(input("Enter item ID to purchase: "))
                if item_id not in store_items.keys():
                    print("item not present in store")           
                else:
                    quantity = int(input("Enter quantity to purchase: "))
                    purchase_item(item_id, quantity)               
            else:
                menu()
                break
 
    elif choice == 3:
        item_id = int(input("Enter item ID to update: "))
        if item_id in cart:
            quantity = int(input("Enter new quantity: "))
            update_item(item_id, quantity)
        else:
            print("Item not found in cart")    
    elif choice == 4:
        item_id = int(input("Enter item ID to remove: "))
        if item_id in cart:
            remove_item(item_id)
        else:
           print("Item not found in cart.")
       
    elif choice == 5:
        view_cart()
    elif choice == 6:
        generate_invoice()
        break
    else:
        print("Invalid choice. Please try again.")
 