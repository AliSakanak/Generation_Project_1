import pickle

try:
    products = pickle.load(open("products.dat", "rb"))
    print("\nProducts save found and loaded.")
except FileNotFoundError:
    print("\nExisting products not found. Creating products file.")
    products = []

try:
    couriers = pickle.load(open("couriers.dat", "rb"))
    print("\nCouriers save found and loaded.")
except FileNotFoundError:
    print("\nExisting couriers not found. Creating couriers file.")
    couriers = []

try:
    orders = pickle.load(open("orders.dat", "rb"))
    print("\nOrders save found and loaded.")
except FileNotFoundError:
    print("\nExisting orders not found. Creating orders file.")
    orders = []


def main_menu():
    print("\n___Main Menu___")
    print("[0] Exit App")
    print("[1] Product Menu")
    print("[2] Couriers Menu")
    print("[3] Orders Menu\n")


def product_menu():
    print("\n___Product Menu___")
    print("[0] Return to Main Menu")
    print("[1] View Products List")
    print("[2] Add New Product")
    print("[3] Update Existing Product")
    print("[4] Delete Product\n")


def couriers_menu():
    print("\n___Couriers Menu___")
    print("[0] Return to Main Menu")
    print("[1] View Couriers List")
    print("[2] Add New Courier")
    print("[3] Update Existing Courier")
    print("[4] Delete Courier\n")


def orders_menu():
    print("\n___Orders Menu___")
    print("[0] Return to Main Menu")
    print("[1] View Orders List")
    print("[2] Create New Order")
    print("[3] Update Existing Order Status")
    print("[4] Update Existing Order Details")
    print("[5] Delete Order\n")


def ask_save():
    print("\n[1] Yes")
    print("[0] No")

    save_option = input("Would you like to save changes? ").lower().strip()
    if save_option == "1" or save_option == "yes":
        print("Saving changes...")
        pickle.dump(products, open("products.dat", "wb"))
        pickle.dump(couriers, open("couriers.dat", "wb"))
        pickle.dump(orders, open("orders.dat", "wb"))
        print("Save successful.\nProgram terminated.")
        quit()
    elif save_option == "0" or save_option == "no":
        print("Quitting without saving changes!\nProgram terminated.")
        quit()
    else:
        print("Choose a valid option!")


def index_list(item_list):
    for i, item in enumerate(item_list):
        print(f"[{i}] {item}")


def view_list(item_list):
    print(item_list)
    print(f"Number of items: {len(item_list)}")


def add_new_item(item_list):
    item_name = input("Type the item you want to add: ").title().strip()
    item_list.append(item_name)
    print(f"{item_name} added to list.")


def update_item(item_list):
    try:
        user_choice = int(input("Type number of item you wish to update: "))
        old_item = item_list[user_choice]
        new_item = input("Type name of new item: ").title().strip()
        item_list[user_choice] = new_item
        print(f"{old_item} changed to {new_item}.")
    except IndexError:
        print("No such number item exists.")
    except ValueError:
        print("Please enter the number of the item, not the word.")


def delete_item(item_list):
    try:
        deleted_item = int(input("Type number of item you wish to delete: "))
        print(f"Deleted {item_list[deleted_item]} from list.")
        del item_list[deleted_item]
    except IndexError:
        print("No such number item exists.")
    except ValueError:
        print("Please enter the number of the item, not the word.")


def create_new_order():
    try:
        customer_name = input("Type customer name: ").title().strip()
        customer_address = input("Type customer address: ").title().strip()
        customer_phone_number = input("Type customer's phone number: ").strip()
        index_list(couriers)
        courier_input = int(input("Type number of courier you wish to use: "))
        courier_choice = couriers[courier_input]
        order_dictionary = {
            "Customer_Name": customer_name,
            "Customer_Address": customer_address,
            "Customer_Phone_Number": customer_phone_number,
            "Courier": courier_choice,
            "Status": order_status_list[0],
        }
        orders.append(order_dictionary)
        print("Order successfully created!")
    except ValueError:
        print("Please enter correct number associated with courier.")
    except IndexError:
        print("No such number item exists.")
    except Exception as e:
        print(f"Unidentified error: {e}")


order_status_list = [
    "preparing",
    "assigning driver",
    "out for delivery",
    "nearby",
    "delivered",
]
new_launch = True
while new_launch:
    print(
        "\n*Welcome to the app! Navigate through the application by inputting"
        " the number seen in [square brackets] and pressing Enter."
    )
    new_launch = False
while True:
    try:
        main_menu()
        option = int(input("Select option: "))
    except ValueError:
        print("Please enter a number option!")
        continue
    if option == 0:
        print("\nExiting App...")
        break
    elif option not in range(4):
        print(
            "That number option doesn't seem to exist! Please choose a correct number from the list for the corresponding action."
        )
        continue
    while option == 1:
        product_menu()
        try:
            product_menu_choice = int(input("Select option: "))
        except ValueError:
            print("Enter a number option!")
            continue
        if product_menu_choice == 0:
            break
        elif product_menu_choice == 1:
            view_list(products)
        elif product_menu_choice == 2:
            add_new_item(products)
        elif product_menu_choice == 3:
            index_list(products)
            update_item(products)
        elif product_menu_choice == 4:
            index_list(products)
            delete_item(products)
        else:
            print("Enter a valid option")
    while option == 2:
        couriers_menu()
        try:
            courier_menu_choice = int(input("Select option: "))
        except ValueError:
            print("Please enter a valid number option!")
            continue
        if courier_menu_choice == 0:
            break
        elif courier_menu_choice == 1:
            view_list(couriers)
        elif courier_menu_choice == 2:
            add_new_item(couriers)
        elif courier_menu_choice == 3:
            index_list(couriers)
            update_item(couriers)
        elif courier_menu_choice == 4:
            index_list(couriers)
            delete_item(couriers)
        else:
            print(
                "Invalid option. Please choose a correct number from the list for the corresponding action."
            )
    while option == 3:
        orders_menu()
        try:
            orders_menu_choice = int(input("Select option: "))
        except ValueError:
            print("Please enter a valid number option!")
            continue
        if orders_menu_choice == 0:
            break
        elif orders_menu_choice == 1:
            view_list(orders)
        elif orders_menu_choice == 2:
            create_new_order()
        elif orders_menu_choice == 3:
            index_list(orders)
            try:
                order_number_input = int(
                    input("Type number of order you want to change status for: ")
                )
                old_order_status = orders[order_number_input]["Status"]
                index_list(order_status_list)
                order_status_input = int(
                    input("Type number of status you wish to update to: ")
                )
                new_order_status = order_status_list[order_status_input]
                orders[order_number_input]["Status"] = new_order_status
                print(
                    f"Order [{order_number_input}] changed from {old_order_status} to {new_order_status}."
                )
            except ValueError:
                print("Please enter a valid number option.")
            except IndexError:
                print("Item number doesn't exist.")
        elif orders_menu_choice == 4:
            index_list(orders)
            try:
                order_index_input = int(
                    input("Type number of order you want to edit: ")
                )
                order_dict_choice = orders[order_index_input]
                for i, key_value in enumerate(order_dict_choice.items()):
                    print(f"[{i}] {key_value[0]}: {key_value[1]}")
                order_key_choice = int(input("Type number of item you want to edit: "))
                order_value_change = (
                    input("Type input you'd like to change to: ").strip().title()
                )
                keys = list(order_dict_choice.keys())
                if len(order_value_change) > 0:
                    old_item = order_dict_choice[keys[order_key_choice]]
                    order_dict_choice[keys[order_key_choice]] = order_value_change
                    print(f"{old_item} changed to {order_value_change}.")
                else:
                    print("No changes were made as no input was given.")
            except ValueError:
                print("Please enter a valid number option.")
            except IndexError:
                print("Item number doesn't exist.")
        elif orders_menu_choice == 5:
            index_list(orders)
            delete_item(orders)
        else:
            print(
                "Invalid option. Please choose a correct number from the list for the corresponding action."
            )

while True:
    ask_save()
