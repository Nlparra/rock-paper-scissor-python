import random

user_hand = input("rock, paper or scissors? shoot")

# rock > paper
# rock < scissors
# scissors > paper
def pc_choice():
    hand = ["rock", "paper", "scissors"]
    random_hand = hand[random.randint(0, len(hand))]
    return (random_hand)

def game(user_hand):
        if user_hand == pc_choice():
            print("Tied")
        elif user_hand == "rock":
            if pc_choice() == "Paper":
                print("You lose!", pc_choice(), "covers", user_hand)
            else:
                print("You win!", user_hand, "smashes", pc_choice())
        # elif user_hand == "Paper":
        #     if pc_choice() == "Scissors":
        #         print("You lose!", pc_choice(), "cut", user_hand)
        #     else:
        #         print("You win!", user_hand, "covers", pc_choice())
        # elif user_hand == "Scissors":
        #     if pc_choice() == "Rock":
        #         print("You lose...", pc_choice(), "smashes", user_hand)
        #     else:
        #         print("You win!", user_hand, "cut", pc_choice())
        # else:
        #     print("That's not a valid play. Check your spelling!")
need to improve the code
print(game())




