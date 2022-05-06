orders = [
    {'Customer_Name': 'Bob', 'Customer_Address': '12', 'Customer_Phone_Number': 33333, 'Courier': 'Ali Sakanak', 'Status': 'preparing'},
    {'Customer_Name': 'Jesus', 'Customer_Address': 'Christ', 'Customer_Phone_Number': 223222, 'Courier': 'John', 'Status': 'preparing'}
    ]

order_dict_choice = orders[0]
print(order_dict_choice)
for i, key_value in enumerate(order_dict_choice.items()):
    print(i, key_value)
order_item_change = 1
keys = list(order_dict_choice)
print(keys)
changedname = '159 restons crescent'
order_dict_choice[keys[order_item_change]] = changedname

for i, key_value in enumerate(order_dict_choice.items()):
    print(i, key_value)
