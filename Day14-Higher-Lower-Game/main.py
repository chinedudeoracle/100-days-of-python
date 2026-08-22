from art import logo
from art import vs
from game_data import data
from random import randint
import os


DATA_SIZE = len(data)

def generate_message(index):
    return f"{data[index]['name']}, a {data[index]['description']}, from {data[index]['country']}."

def show_messages(first_message, second_message):
    print(f"Compare A: {first_message}")
    print("")
    print("")
    print(vs)
    print(f"Compare B: {second_message}")

def higher_search(score_a, score_b):
    if score_a > score_b:
        return 'a'
    else:
        return 'b'

def game():
    continue_game = True
    current_score = 0
    index_a = randint(0, DATA_SIZE - 1)
    index_b = randint(0, DATA_SIZE - 1)

    while index_b == index_a:
        index_b = randint(0, DATA_SIZE - 1) 
    
    while continue_game:
        a_score = data[index_a]['follower_count']   
        b_score = data[index_b]['follower_count']
        first_message = generate_message(index_a)
        second_message = generate_message(index_b)
        print(logo)
        show_messages(first_message, second_message)
        user_choice = input("Who has more followers? Type 'A' or 'B': ").lower().strip()
        while user_choice == higher_search(score_a=a_score, score_b=b_score):
            os.system("cls" if os.name == "nt" else "clear")
            current_score += 1
            index_a = index_b
            a_score = data[index_a]['follower_count']
            index_b = randint(0, DATA_SIZE - 1)
            if index_b == index_a:
                while index_b == index_a:
                    index_b = randint(0, DATA_SIZE - 1) 
            b_score = data[index_b]['follower_count']
            first_message = generate_message(index_a)
            second_message = generate_message(index_b)

            print(logo)
            print(f"You're right! Current score: {current_score}")
            show_messages(first_message, second_message)
            user_choice = input("Who has more followers? Type 'A' or 'B': ").lower().strip()

        continue_game = False
        os.system("cls" if os.name == "nt" else "clear")
        print(logo)
        print(f"Sorry, that's wrong. Final score: {current_score}")


game()