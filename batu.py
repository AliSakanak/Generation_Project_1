
import random

def menu():
    print("___Game Menu___")
    print("[1] Hit")
    print("[2] Stand")


bj_card_1 = random.randint(1,11)
print(f"Your first card = {bj_card_1}")

bj_card_2 = random.randint(1,11)
print(f"Your second card = {bj_card_2}")

bj_hand = bj_card_1 + bj_card_2
print (f"Your Total Hand = {bj_hand}")


if bj_hand == 21:
    print ("You WIN")
elif bj_hand > 21:
    print ("BUST")
else:
    menu()
    user_choice = int(input("Enter choice: "))
    if user_choice == 1:
        bj_hand = random.randint(1,11) + bj_hand
        print(f"Your Total Hand ={bj_hand}")
        if bj_hand == 21:
            print ("You WIN")
        elif bj_hand > 21:
            print ("BUST")
        else:
            menu()
            user_choice = int(input("Enter choice: "))
            if user_choice == 1:
                bj_hand = random.randint(1,11) + bj_hand
                print(f"Your Total Hand ={bj_hand}")
                if bj_hand == 21:
                    print ("You WIN")
                elif bj_hand > 21:
                    print ("BUST")