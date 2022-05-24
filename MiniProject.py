from logging import exception
import pickle
import pymysql
from time import sleep
# I WOULD LIKE TO ADD DATE/TIME OF ORDER CREATED

try:
    connection = pymysql.connect(
    host="localhost",
    user="root",
    password="kelebek18",
    db="mini_project"
    )
    print ("\n***Connected to cafe's database***")
except pymysql.OperationalError as e:
    print(f"\nERROR: Unable to successfully connect to Database.\n{e}")
    print("Please check database connection. Quitting application...\n")
    quit()
sleep(1)


def print_product_menu():
    print("\n___Product Menu___")
    print("[0] Return to Main Menu")
    print("[1] View Products List")
    print("[2] Add New Product")
    print("[3] Update Existing Product")
    print("[4] Delete Product\n")


def print_couriers_menu():
    print("\n___Couriers Menu___")
    print("[0] Return to Main Menu")
    print("[1] View Couriers List")
    print("[2] Add New Courier")
    print("[3] Update Existing Courier")
    print("[4] Delete Courier\n")


def print_orders_menu():
    print("\n___Orders Menu___")
    print("[0] Return to Main Menu")
    print("[1] View Orders List")
    print("[2] Create New Order")
    print("[3] Update Existing Order Status") 
    print("[4] Update Existing Order Details")
    print("[5] Delete Order\n")

def print_main_menu():
    print("\n___Main Menu___")
    print("[0] Exit App")
    print("[1] Product Menu")
    print("[2] Couriers Menu")
    print("[3] Orders Menu\n")


def main_menu():
    while True:
        try:
            print_main_menu()
            option = int(input("Select option: "))
        except ValueError:
            print("ERROR: You entered a letter value. Please enter a number option.")
            continue
        if option == 0:
            print("\nExiting App...")
            quit()
        elif option not in range(4):
            print(
                "ERROR: That number option doesn't seem to exist! Please choose a correct number from the list for the corresponding action."
            )
            continue
        while option == 1:
            print_product_menu()
            try:
                product_menu_choice = int(input("Select option: "))
            except ValueError:
                print("ERROR: You entered a letter value. Please enter a number option.")
                continue
            match product_menu_choice:
                case 0:
                    break
                case 1:
                    view_table("products")
                case 2:
                    add_new_product()
                case 3:
                    update_product()
                case 4:
                    delete_item("products")
                case _:
                    print("ERROR: Option not recognised. Please enter a valid number option.")
        
        while option == 2:
            print_couriers_menu()
            try:
                courier_menu_choice = int(input("Select option: "))
            except ValueError:
                print("Please enter a valid number option!")
                continue
            match courier_menu_choice:
                case 0:
                    break
                case 1:
                    view_table("couriers")
                case 2:
                    add_new_courier()
                case 3:
                    update_courier()
                case 4:
                    delete_item("couriers")
                case _:
                    print(
                        "ERROR: The number option you have input does not exist. Please view the options and choose accordingly."
                    )

        while option == 3:
            print_orders_menu()
            try:
                orders_menu_choice = int(input("Select option: "))
            except ValueError:
                print("Please enter a valid number option!")
                continue
            match orders_menu_choice:
                case 0:
                    break
                case 1:
                    view_table("orders")
                case 2:
                    add_new_order()
                case 3:
                    update_order_status()
                case 4:
                    update_order_details()
                case 5:
                    delete_item("orders")
                case _:
                    print(
                    "Invalid option. Please choose a correct number from the list for the corresponding action."
                )


# def ask_save():
#     print("\n[1] Yes")
#     print("[0] No")

#     save_option = input("Would you like to save changes? ").lower().strip()
#     if save_option == "1" or save_option == "yes":
#         print("Saving changes...")
#         pickle.dump(products, open("products.dat", "wb"))
#         pickle.dump(couriers, open("couriers.dat", "wb"))
#         pickle.dump(orders, open("orders.dat", "wb"))
#         print("Save successful.\nProgram terminated.")
#         quit()
#     elif save_option == "0" or save_option == "no":
#         print("Quitting without saving changes!\nProgram terminated.")
#         quit()
#     else:
#         print("Choose a valid option!")


def view_table(table):
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {table}")
    result = cursor.fetchall()
    column_names = [i[0] for i in cursor.description]
    column_names_string = ", ".join(column_names).title()
    if not result:
        print(f"{table} table is empty".capitalize())
    else:
        if table == "products":
            print(f"\n[Loading {table}] How would you like the list to be displayed?")
            print("[0] Exit View Table")
            print("[1] Sort Products By Name")
            print("[2] Sort Products By Price")
            print("[3] Sort Products By ID")
            try:
                order_by_option = int(input("Select an option to view list sorted, or enter 0 to exit: "))
            except ValueError:
                print("ERROR: You have input a letter value where a number option is required.")
                main_menu()
            
            match order_by_option:
                case 0:
                    main_menu()
                case 1:
                    order_by_query("name", "products", column_names_string)
                case 2:
                    order_by_query("price", "products", column_names_string)
                case 3:
                    order_by_query("products_id", "products", column_names_string)
                case _:
                    print(f"ERROR: That number option ({order_by_option}) does not exist.")
                    main_menu()
        
        elif table == "couriers":
            print(f"\n[Loading {table}] How would you like the list to be displayed?")
            print("[0] Exit View Table")
            print("[1] Sort Couriers By Name")
            print("[2] Sort Couriers By Phone Number")
            print("[3] Sort Couriers By ID")
            try:
                order_by_option = int(input("Select an option to view list sorted, or enter 0 to exit: "))
            except ValueError:
                print("ERROR: You have input a letter value where a number option is required.")
                main_menu()
            
            match order_by_option:
                case 0:
                    main_menu()
                case 1:
                    order_by_query("name", "couriers", column_names_string)
                case 2:
                    order_by_query("phone_number", "couriers", column_names_string)
                case 3:
                    order_by_query("couriers_id", "couriers", column_names_string)
                case _:
                    print(f"ERROR: That number option ({order_by_option}) does not exist.")
                    main_menu()

        elif table == "orders":
            print(f"\n[Loading {table}] How would you like the list to be displayed?")
            print("[0] Exit View Table")
            print("[1] Sort Orders By Customer Name")
            print("[2] Sort Orders By Address")
            print("[3] Sort Orders By Customer Phone Number")
            print("[4] Sort Orders By Courier ID")
            print("[5] Sort Orders By Status ID")
            print("[6] Sort Orders By Product ID")
            print("[7] Sort Orders By Order_ID")
            try:
                order_by_option = int(input("Select an option to view list sorted, or enter 0 to exit: "))
            except ValueError:
                print("ERROR: You have input a letter value where a number option is required.")
                main_menu()
            
            match order_by_option:
                case 0:
                    main_menu()
                case 1:
                    order_by_query("customer_name", "orders", column_names_string)
                case 2:
                    order_by_query("customer_address", "orders", column_names_string)
                case 3:
                    order_by_query("customer_address", "orders", column_names_string)
                case 4:
                    order_by_query("couriers_id", "orders", column_names_string)
                case 5:
                    order_by_query("status_id", "orders", column_names_string)
                case 6:
                    order_by_query("products_id", "orders", column_names_string)
                case 7:
                    order_by_query("orders_id", "orders", column_names_string)
                case _:
                    print(f"ERROR: That number option ({order_by_option}) does not exist.")
                    main_menu()
    cursor.close()


def order_by_query(column, table, column_names_string):
    sql = f"SELECT * FROM {table} ORDER BY {column}"
    result = retrieve_fetchall(sql)
    print(f"\n({column_names_string})")
    for item in result:
        print(item)
    print(f"Number of items: {len(result)}")
    print(f"\n(Results were ordered by {column})")


def add_new_product():
    try:
        cursor = connection.cursor()
        product_name = input("Type the name of product to add: ").title().strip()
        product_price = float(input("Type the price of the product: "))
        if len(product_name) == 0:
            print("ERROR: Product name field cannot be blank.")
            return

        sql = f"INSERT INTO products (name, price) VALUES (%s,%s)"
        cursor.execute(sql, (product_name, product_price))
        print(f"\n{product_name} successfully added to products.")
        connection.commit()
        cursor.close()

    except ValueError:
        print(f"ERROR: Please input the correct value type for the associated field.\nExample: Product price must be int or float")


def add_new_courier():
    try:
        cursor = connection.cursor()
        courier_name = input("Type the name of courier to add: ").title().strip()
        courier_phone = input("Type the phone number of the courier: ").strip()
        if len(courier_name) == 0 or len(courier_phone) == 0:
            print("ERROR: When adding a new courier, fields cannot be left blank")
            return
        
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
            print(f"ERROR: Input cannot be blank.")
            return
        view_table("products")
        products_input = input("Type ID of products you wish to order, seperated by commas: ")
        removed_spaces = products_input.replace(" ","")
        listed_version = removed_spaces.split(",")
        products_list_chosen = []
        for number in listed_version:
            cursor.execute(f"SELECT * FROM mini_project.products WHERE products_id = {number}")
            products_choice = cursor.fetchone()
            products_list_chosen.append(products_choice)
        print(f"*{products_list_chosen} added to order*")
        view_table("couriers")
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
        print("ERROR: Please enter correct number associated with courier.")
    except IndexError:
        print("ERROR: No such number item exists.")
    except TypeError:
        print("ERROR: Invalid entry.")


def update_product():
    try:
        view_table("products")
        sql = f"SELECT COUNT(*) FROM products"
        check_empty = retrieve_fetchone(sql)
        if check_empty[0] == 0:
            print("Exiting update menu")
            return

        user_choice = int(input("Type the product_id of item you wish to update: "))
        sql = f"SELECT * FROM products WHERE products_id = {user_choice}"
        old_item = retrieve_fetchone(sql)
        if old_item == None:
            print(f"ERROR: The products_id you have entered ({user_choice}) could not be found")
            return
        
        old_name = old_item[1]
        old_price = old_item[2]
        product_id = old_item[0]
        print(f"*{old_item} selected*")

        new_name = input("Type updated name of product, or leave blank for no change: ").strip().title()
        new_price = input("Type the updated product price, or leave blank for no change: ").strip()

        if new_name:
            cursor = connection.cursor()
            sql = F"UPDATE products SET name = \'{new_name}\' WHERE products_id = {user_choice}"
            cursor.execute(sql)
            connection.commit()
            cursor.close()
            print(f"\n*[ID {product_id}]: Product name {old_name} updated to {new_name} successfully*")
        else:
            print(f'\n*[ID {product_id}]: Product name not changed as entry was left blank*')

        if new_price:
            cursor = connection.cursor()
            sql = f"UPDATE products SET price = {new_price} WHERE (products_id = {user_choice})"
            cursor.execute(sql)
            connection.commit()
            cursor.close()
            print(f"*[ID {product_id}]: Price of {old_price} updated to {new_price} successfully*")
        else:
            print(f'*[ID {product_id}]: Product price not changed as entry was left blank*')

    except ValueError:
        print(f"ERROR: Please input the correct value type for the associated field")
    except pymysql.OperationalError:
        print(f"ERROR: Please ensure that price is a float value")


def update_courier():
    try:
        view_table("couriers")
        sql = f"SELECT COUNT(*) FROM couriers"
        check_empty = retrieve_fetchone(sql)
        if check_empty[0] == 0:
            print("Exiting update menu")
            return
        
        user_choice = int(input("Type the courier_id of courier you wish to update: "))
        sql = (f"SELECT * FROM couriers WHERE couriers_id = {user_choice}")
        old_item = retrieve_fetchone(sql)

        if old_item == None:
            print(f"ERROR: The couriers_id you have entered ({user_choice}) could not be found")
            return
        print(f"*{old_item} selected*")

        new_name = input("Type updated name of courier, or leave blank for no change: ").strip().title()
        new_number = input("Type the courier phone number, or leave blank for no change: ").strip()

        if len(new_name) > 0:
            sql = F"UPDATE couriers SET name = \'{new_name}\' WHERE couriers_id = {user_choice}"
            commit_query(sql)
            print(f"\n*{old_item} updated to {new_name} successfully*")
        else:
            print('\n*Product name not changed as entry was left blank*')

        if len(new_number) > 0:
            sql = f"UPDATE couriers SET phone_number = {new_number} WHERE couriers_id = {user_choice}"
            commit_query(sql)
            print(f"*{old_item} updated to {new_number} successfully*")
        else:
            print('*Courier phone number not changed as entry was left blank*')

    except ValueError:
        print(f"ERROR: Please input the correct value type for the associated field")
    except pymysql.OperationalError:
        print(f"ERROR: operationalerror")

def update_order_details():
    try:
        check = view_table("orders")
        if check == None:
            print("Returning to orders menu")
            return
    
        order_id_input = int(input("Type the orders_id of order you wish to update: "))
        sql = f"SELECT * FROM orders WHERE orders_id = {order_id_input}"
        old_order = retrieve_fetchone(sql)

        if old_order == None:
            print(f"ERROR: The orders_id you have entered ({order_id_input}) could not be found")
            return
        print(f"*{old_order} selected*")

        new_name = input("Type updated name of customer, or leave blank for no change: ").strip().title()
        new_address = input("Type updated customer address, or leave blank for no change: ").strip()
        new_phonenumber = input("Type updated customer phone number, or leave blank for no change: ").strip()

        view_table("products")
        products_input = input("Type ID of products you wish to overwrite with, or leave blank for no change: ")
        removed_spaces = products_input.replace(" ","")
        listed_version = removed_spaces.split(",")

        view_table("couriers")
        courier_input = input("Type ID of courier you want to use, or leave blank for no change: ").strip()
        if len(removed_spaces) > 0:
            products_list_chosen = []
            cursor = connection.cursor()
            for number in listed_version:
                cursor.execute(f"SELECT * FROM mini_project.products WHERE products_id = {number}")
                products_choice = cursor.fetchone()
                products_list_chosen.append(products_choice)
            print(products_list_chosen)
            sql = f"UPDATE orders SET products_id = \'{products_input}\' WHERE orders_id = {order_id_input}"
            commit_query(sql)
            print(f"*{products_list_chosen} added to order*")
        else:
            print('\n*Products ordered not changed as entry was left blank*')

        if len(courier_input) > 0:
            courier_input = int(courier_input)
            cursor = connection.cursor()
            sql = F"UPDATE orders SET couriers_id = \'{courier_input}\' WHERE orders_id = {order_id_input}"
            commit_query(sql)
            print(f"\n*{old_order} updated to {courier_input} successfully*")
        else:
            print("\n*Courier was not changed as entry was left blank*")
    
        if len(new_name) > 0:
            cursor = connection.cursor()
            sql = F"UPDATE orders SET customer_name = \'{new_name}\' WHERE orders_id = {order_id_input}"
            commit_query(sql)
            print(f"\n*{old_order} updated to {new_name} successfully*")
        else:
            print('\n*Customer name not changed as entry was left blank*')

        if len(new_address) > 0:
            cursor = connection.cursor()
            sql = f"UPDATE orders SET customer_address = \'{new_address}\' WHERE orders_id = {order_id_input}"
            commit_query(sql)
            print(f"*{old_order} updated to {new_address} successfully*")
        else:
            print('\n*Customer address not changed as entry was left blank*')

        if len(new_phonenumber) > 0:
            cursor = connection.cursor()
            sql = f"UPDATE orders SET customer_phone= \'{new_phonenumber}\' WHERE orders_id = {order_id_input}"
            commit_query(sql)
            print(f"*{old_order} updated to {new_phonenumber} successfully*")
        else:
            print("\n*Customer phone number not changed as entry was left blank*")

    except ValueError:
        print(f"ERROR: ID not found")
    except pymysql.OperationalError:
        print(f"ERROR: operationalerror")

def update_order_status():
    try:
        check = view_table("orders")
        if check == None:
            print("Returning to order menu")
            return

        cursor = connection.cursor()
        order_id_input = int(input("Type the order_id you want to update status for: "))
        cursor.execute(f"SELECT * FROM orders WHERE orders_id = {order_id_input}")
        old_item = cursor.fetchone()
        print(old_item)
        if old_item == None:
            print(f"ERROR: The orders_id you have entered ({order_id_input}) could not be found")
            return
        print(f"*{old_item} selected*")
        view_table("orders_status")
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


def delete_item(table):
    try:
        view_table(table)
        sql = f"SELECT COUNT(*) FROM {table}"
        check_empty = retrieve_fetchone(sql)
        if check_empty[0] == 0:
            print("Exiting delete menu")
            return
        
        deleted_item = int(input("Type ID number of item you wish to delete: "))
        sql = (f"SELECT * FROM {table} WHERE {table}_id = {deleted_item}")
        selection = retrieve_fetchone(sql)

        if not selection:
            print(f"\nError: Item associated with chosen ID ({deleted_item}) not found.")
            return
    
        sql = (f"DELETE FROM {table} WHERE {table}_id = {deleted_item}")
        commit_query(sql)
        print(f"\n*Deleted {selection} from database*")
    except pymysql.IntegrityError:
        print(
            "ERROR: The item you are trying to delete is currently present in an order. "
        "The item cannot be deleted until the order is either deleted or completed."
        )
    except ValueError:
        print("ERROR: You did not input an ID value. To select an item, please input the ID.")

def commit_query(query):
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()


def retrieve_fetchone(query):
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()
    return result


def retrieve_fetchall(query):
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results

new_launch = True
while new_launch:
    print(
        "\n*Welcome to the app! Navigate through the application by inputting"
        " the number seen in [square brackets] and pressing Enter*"
    )
    new_launch = False
    sleep(2)

main_menu()

while True:
    print("reached the end option")
