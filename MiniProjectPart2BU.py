import pickle

try:
    products = pickle.load(open('products.dat', 'rb'))
    print('\nProducts save found and loaded.')
except FileNotFoundError:
    print('\nExisting products not found. Creating products file.')
    products = []

try:
    couriers = pickle.load(open('couriers.dat', 'rb'))
    print('\nCouriers save found and loaded.')
except FileNotFoundError:
    print('\nExisting couriers not found. Creating couriers file.')
    couriers = []

def mmenu():
    print('\n___Main Menu___')
    print('[0] Exit App')
    print('[1] Product Menu')
    print('[2] Couriers Menu\n')

def product_menu():
    print('\n___Product Menu___')
    print('[0] Return to Main Menu')
    print('[1] View Products List')
    print('[2] Add New Product')
    print('[3] Update Existing Product')
    print('[4] Delete Product\n')

def couriers_menu():
    print('\n___Couriers Menu___')
    print('[0] Return to Main Menu')
    print('[1] View Couriers List')
    print('[2] Add New Courier')
    print('[3] Update Existing Courier')
    print('[4] Delete Courier\n')

def save_menu():
    print('\n[1] Yes')
    print('[0] No')

def index_list(list):
    for i, product in enumerate(list):
        print(i, product)

while True:
    try:    
        mmenu()
        option = int(input('Select option: '))
    except ValueError:
        print('Please enter a correct number option!')
        continue
    if option == 0:
        print('Exiting App')
        break
    elif option not in range(3):
        print('Invalid option. Please choose a correct number from the list for the corresponding action.')
        continue
    while option == 1:
        product_menu()
        try:
            product_menu_choice = int(input('Select option: '))
        except ValueError:
            print('Enter a valid number option')
            continue
        if product_menu_choice == 0:
            break
        elif product_menu_choice == 1:
            print(products)
            print(f'Number of products: {len(products)}')
        elif product_menu_choice == 2:
            product_name = input('Type the product you want to add: ').title().strip()
            products.append(product_name)
            print(f'{product_name} added to products list.')
        elif product_menu_choice == 3:
            index_list(products)
            try:
                user_choice = int(input('Type number of item you wish to update: '))
                old_product = products[user_choice]
                new_product = input('Type name of new product name: ').title().strip()
                products[user_choice] = new_product
                print(f'{old_product} changed to {new_product}.')
            except IndexError:
                print('No such number item exists.')
            except ValueError:
                print('Please enter the number of the item, not the word.')
        elif product_menu_choice == 4:
            index_list(products)
            try:
                deleted_item = int(input('Type number of item you wish to delete: '))
                print(f'Deleting {products[deleted_item]} from products list.')
                del products[deleted_item]
            except IndexError:
                print('No such number item exists.')
            except ValueError:
                print('Please enter the number of the item, not the word.')
        else:
            print('Enter a valid option')
    while option == 2:
        couriers_menu()
        try:
            courier_menu_choice = int(input('Select option: '))
        except ValueError:
            print('Please enter a correct number option!')
            continue
        if courier_menu_choice == 0:
            break
        elif courier_menu_choice == 1:
            print(couriers)
            print(f'Number of couriers: {len(couriers)}')
        elif courier_menu_choice == 2:
            courier_name = input('Type the courier you want to add: ').title().strip()
            couriers.append(courier_name)
            print(f'{courier_name} added to couriers list.')
        elif courier_menu_choice == 3:
            index_list(couriers)
            try:
                user_choice = int(input('Type the number of courier you wish to update: '))
                old_courier = couriers[user_choice]
                new_courier = input('Type name of new courier: ').title().strip()
                couriers[user_choice] = new_courier
                print(f'{old_courier} changed to {new_courier}.')
            except IndexError:
                print('No such number courier exists.')
            except ValueError:
                print('Please enter the number of the courier, not the word.')
        elif courier_menu_choice == 4:
            index_list(couriers)
            try:
                deleted_item = int(input('Type number of courier you wish to delete: '))
                print(f'Deleting {couriers[deleted_item]} from couriers list.')
                del couriers[deleted_item]
            except IndexError:
                print('No such number courier exists.')
            except ValueError:
                print('Please enter the number of the courier, not the word.')
        else:
            print('Enter a valid number option.')

while True:
    save_menu()
    try:
        save_option = int(input('Would you like to save changes? '))
        if save_option == 1:
            print('Saving changes...')
            pickle.dump(products, open('products.dat', 'wb'))
            pickle.dump(couriers, open('couriers.dat', 'wb'))
            print('Save successful. Quitting.')
            quit()
        elif save_option == 0:
            print('Quitting without saving changes!')
            quit()
        else:
            print('Choose a valid option.')
    except ValueError:
        print('Choose a valid option.')