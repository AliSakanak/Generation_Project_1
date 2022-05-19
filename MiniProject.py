from logging import exception
import pickle
import pymysql
from time import sleep

try:
    connection = pymysql.connect(
    host="localhost",
    user="root",
    password="kelebek18",
    db="mini_project"
    )
    print ("Connected to cafe's database")
except pymysql.OperationalError as e:
    print(f"Error: {e}\nUnable to successfully connect to Database.")
#sleep(1)

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

def view_list(item_list):
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {item_list}")
    result = cursor.fetchall()
    column_names = [i[0] for i in cursor.description]
    column_names_string = ", ".join(column_names).title()
    if len(result) == 0:
        print(f"{item_list} table is empty".capitalize())
    else:
        print(f"\n({column_names_string})")
        for item in result:
            print(item)
        print(f"Number of items: {len(result)}")
    cursor.close()

def add_new_product():
    try:
        cursor = connection.cursor()
        product_name = input("Type the name of product to add: ").title().strip()
        product_price = float(input("Type the price of the product: "))
        sql = f"INSERT INTO products (name, price) VALUES (%s,%s)"
        cursor.execute(sql, (product_name, product_price))
        print(f"\n{product_name} successfully added to products.")
        connection.commit()
        cursor.close()
    except ValueError:
        print(f"Please input the correct value type for the associated field.")

def add_new_courier():
    try:
        cursor = connection.cursor()
        courier_name = input("Type the name of courier to add: ").title().strip()
        courier_phone = input("Type the phone number of the courier: ").strip()
        sql = f"INSERT INTO couriers (name, phone_number) VALUES (%s,%s)"
        cursor.execute(sql, (courier_name, courier_phone))
        print(f"\n{courier_name} successfully added")
        connection.commit()
        cursor.close()
    except ValueError:
        print(f"Please input the correct value type for the associated field.")

def add_new_order():
    try:
        cursor = connection.cursor()
        customer_name = input("Type customer name: ").title().strip()
        customer_address = input("Type customer address: ").title().strip()
        customer_phone_number = input("Type customer's phone number: ").strip()
        if len(customer_name) == 0 or len(customer_address) == 0 or len(customer_phone_number) == 0:
            print(f"Error: Input cannot be blank.")
            return
        view_list("products")
        products_input = input("Type ID of products you wish to order, seperated by commas: ")
        removed_spaces = products_input.replace(" ","")
        listed_version = removed_spaces.split(",")
        products_list_chosen = []
        for number in listed_version:
            cursor.execute(f"SELECT * FROM mini_project.products WHERE products_id = {number}")
            products_choice = cursor.fetchone()
            products_list_chosen.append(products_choice)
        print(f"*{products_list_chosen} added to order*")
        view_list("couriers")
        courier_input = int(input("Type ID of courier you wish to use: "))
        cursor.execute(f"SELECT name FROM mini_project.couriers WHERE couriers_id = {courier_input}")
        courier_choice = cursor.fetchone()[0]
        print(courier_choice)
        print(f"*{courier_choice} chosen as courier*\n")
        sql = f"""INSERT INTO mini_project.orders (customer_name, customer_address, customer_phone, couriers_id, status_id, products_id) 
        VALUES (%s,%s,%s,%s,%s,%s)"""
        cursor.execute(sql, (customer_name, customer_address, customer_phone_number, courier_input, 1, products_input))
        connection.commit()
        cursor.close()
        print("Order successfully created!")
    except ValueError:
        print("Error: Please enter correct number associated with courier.")
    except IndexError:
        print("Error: No such number item exists.")
    except TypeError:
        print("Error: Values entered cannot be blank unless stated otherwise.")


def update_courier():
    try:
        cursor = connection.cursor()
        user_choice = int(input("Type the courier_id of courier you wish to update: "))
        cursor.execute(f"SELECT * FROM couriers WHERE couriers_id = {user_choice}")
        old_item = cursor.fetchone()
        print(old_item)
        if old_item == None:
            print(f"ERROR: The couriers_id you have entered ({user_choice}) could not be found")
            return
        print(f"*{old_item} selected*")
        new_name = input("Type updated name of courier, or leave blank for no change: ").strip().title()
        new_number = input("Type the courier phone number, or leave blank for no change: ").strip()
        if len(new_name) > 0:
            cursor = connection.cursor()
            sql = F"UPDATE couriers SET name = \'{new_name}\' WHERE couriers_id = {user_choice}"
            cursor.execute(sql)
            connection.commit()
            cursor.close()
            print(f"\n*{old_item} updated to {new_name} successfully*")
        else:
            print('\n*Product name not changed as entry was left blank*')
        if len(new_number) > 0:
            cursor = connection.cursor()
            sql = f"UPDATE couriers SET phone_number = {new_number} WHERE couriers_id = {user_choice}"
            cursor.execute(sql)
            connection.commit()
            cursor.close()
            print(f"*{old_item} updated to {new_number} successfully*")
        else:
            print('*Courier phone number not changed as entry was left blank*')
    except ValueError:
        print(f"ERROR: Please input the correct value type for the associated field")
    except pymysql.OperationalError:
        print(f"ERROR: operationalerror")

def update_order_status():
    try:
        cursor = connection.cursor()
        order_id_input = int(input("Type the order_id you want to update status for: "))
        cursor.execute(f"SELECT * FROM orders WHERE orders_id = {order_id_input}")
        old_item = cursor.fetchone()
        print(old_item)
        if old_item == None:
            print(f"ERROR: The orders_id you have entered ({order_id_input}) could not be found")
            return
        print(f"*{old_item} selected*")
        view_list("orders_status")
        new_status_input = int(input("Type status_id of status name you wish to update to, or leave blank for no change: "))
        cursor.execute(f"SELECT name FROM orders_status WHERE status_id = {new_status_input}")
        status_name_choice = cursor.fetchone()[0]
        if len(str(new_status_input)) > 0:
            cursor = connection.cursor()
            sql = F"UPDATE orders SET status_id = {new_status_input} WHERE orders_id = {order_id_input}"
            cursor.execute(sql)
            connection.commit()
            cursor.close()
            print(f"\n*{old_item} updated to {status_name_choice} successfully*")
        else:
            print('\n*Order status not changed as entry was left blank*')
    except ValueError:
        print(f"ERROR: Please input the correct value type for the associated field")
    except pymysql.OperationalError:
        print(f"ERROR: operationalerror")

def update_product():
    try:
        cursor = connection.cursor()
        user_choice = int(input("Type the product_id of item you wish to update: "))
        cursor.execute(f"SELECT * FROM products WHERE products_id = {user_choice}")
        old_item = cursor.fetchone()
        if old_item == None:
            print(f"ERROR: The products_id you have entered ({user_choice}) could not be found")
            return
        print(f"*{old_item} selected*")
        new_name = input("Type updated name of product, or leave blank for no change: ").strip().title()
        new_price = input("Type the updated product price, or leave blank for no change: ").strip()
        if len(new_name) > 0:
            cursor = connection.cursor()
            sql = F"UPDATE products SET name = \'{new_name}\' WHERE products_id = {user_choice}"
            cursor.execute(sql)
            connection.commit()
            cursor.close()
            print(f"\n*{old_item} updated to {new_name} successfully*")
        else:
            print('\n*Product name not changed as entry was left blank*')
        if len(new_price) > 0:
            cursor = connection.cursor()
            sql = f"UPDATE products SET price = {new_price} WHERE (products_id = {user_choice})"
            cursor.execute(sql)
            connection.commit()
            cursor.close()
            print(f"*{old_item} updated to {new_price} successfully*")
        else:
            print('*Product price not changed as entry was left blank*')
    except ValueError:
        print(f"ERROR: Please input the correct value type for the associated field")
    except pymysql.OperationalError:
        print(f"ERROR: Please ensure that price is a float value")


#def add_new_item(item_list):
    # item_name = input("Type the item you want to add: ").title().strip()
    # item_list.append(item_name)
    # print(f"{item_name} added to list.")
    # #INSERT INTO `mini_project`.`products` (`product_id`, `name`, `price`) VALUES ('2', 'Coke', '0.99');


# def update_item(item_list):
#     try:
#         user_choice = int(input("Type number of item you wish to update: "))
#         old_item = item_list[user_choice]
#         new_item = input("Type name of new item: ").title().strip()
#         item_list[user_choice] = new_item
#         print(f"{old_item} changed to {new_item}.")
#     except IndexError:
#         print("No such number item exists.")
#     except ValueError:
#         print("Please enter the number of the item, not the word.")

def delete_item_new(table):
    try:
        cursor = connection.cursor()
        deleted_item = int(input("Type ID number of item you wish to delete: "))
        cursor.execute(f"SELECT * FROM {table} WHERE {table}_id = {deleted_item}")
        selection = cursor.fetchone()
        if selection == None:
            print(f"\nError: Item associated with chosen ID ({deleted_item}) not found.")
            return
        cursor.execute(f"DELETE FROM {table} WHERE {table}_id = {deleted_item}")
        connection.commit()
        cursor.close()
        print(f"\n*Deleted {selection} from database*")
    except Exception as e:
        print(f"Unexpected error: {e}")

order_status_list = [
    "preparing",
    "assigning driver",
    "out for delivery",
    "nearby",
    "delivered",
]

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="kelebek18",
    db="mini_project"
)


new_launch = True
while new_launch:
    print(
        "\n*Welcome to the app! Navigate through the application by inputting"
        " the number seen in [square brackets] and pressing Enter."
    )
    new_launch = False
    #sleep(3)
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
            view_list("products")
        elif product_menu_choice == 2:
            add_new_product()
        elif product_menu_choice == 3:
            view_list("products")
            update_product()
        elif product_menu_choice == 4:
            view_list("products")
            delete_item_new("products")
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
            view_list("couriers")
        elif courier_menu_choice == 2:
            add_new_courier()
        elif courier_menu_choice == 3:
            view_list("couriers")
            update_courier()
        elif courier_menu_choice == 4:
            view_list("couriers")
            delete_item_new("couriers")
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
            view_list("orders")
        elif orders_menu_choice == 2:
            add_new_order()
        elif orders_menu_choice == 3:
            view_list("orders")
            update_order_status()
        elif orders_menu_choice == 4:
            view_list("orders")
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
            view_list("orders")
            delete_item_new("orders")
        else:
            print(
                "Invalid option. Please choose a correct number from the list for the corresponding action."
            )

while True:
    ask_save()
