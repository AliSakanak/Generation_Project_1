import random


def menu():
    print("___Game Menu___")
    print("[1] Hit")
    print("[2] Stand")

J = 10
K = 10
Q = 10
A = 11

deck = [
    A, 2, 3, 4, 5, 6, 7, 8, 9,
    A, 2, 3, 4, 5, 6, 7, 8, 9,
    A, 2, 3, 4, 5, 6, 7, 8, 9,
    A, 2, 3, 4, 5, 6, 7, 8, 9,
    J, K, Q,
    J, K, Q,
    J, K, Q,
    J, K, Q
    ]

user_hand = []
dealer_hand = []

user_card_1 = random.choice(deck)
deck.remove(user_card_1)
user_hand.append(user_card_1)

dealer_card_1 = random.choice(deck)
deck.remove(dealer_card_1)
dealer_hand.append(dealer_card_1)

user_card_2 = random.choice(deck)
deck.remove(user_card_2)
user_hand.append(user_card_2)

dealer_card_2 = random.choice(deck)
deck.remove(dealer_card_2)
dealer_hand.append(dealer_card_2)

user_hand_int = user_card_1 + user_card_2
dealer_hand_int = dealer_card_1 + dealer_card_2

print(f"Your hand: {user_hand_int} ({user_card_1} and {user_card_2})")
print(f"Dealer's hand: {dealer_hand_int} ({dealer_card_1} and {dealer_card_2})")
print(f"User_hand_list: {sum(user_hand)}")
print(f"Dealer_hand_list: {sum(dealer_hand)}")

if sum(dealer_hand) == 21:
    print("You lose")
    quit()
elif sum(user_hand) < 21:
    menu()
    choice = int(input("Selection option: "))
    if choice == 1:
        user_card_3 = random.choice(deck)
        print(user_card_3)
        deck.remove(user_card_3)
        if user_card_3 == 11 and sum(user_hand) + user_card_3 > 21:
                user_hand.append(1)
        else:
            user_hand.append(user_card_3)
        print(user_hand)
        if sum(user_hand) > 21:
            print("You lost")
            quit()
    if choice == 2:
        print(f"You chose to stick. Your hand: {sum(user_hand)}")
        if sum(dealer_hand) >= sum(user_hand):
            print(f"Dealer's hand: {sum(dealer_hand)}")
            print("You lost")
        else:
            print(f"Dealer's hand: {dealer_hand_int}")
            print(f"Your hand: {user_hand_int}")
            dealer_card_3 = random.choice(deck)
            print(dealer_card_3)
            deck.remove(dealer_card_3)
            if dealer_card_3 == 11 and sum(dealer_hand) + dealer_card_3 > 21:
                dealer_hand.append(1)
            else:
                dealer_hand.append(dealer_card_3)
            print(f"Dealer's hand: {sum(dealer_hand)} {dealer_hand}")
            