from higher_lower_game_art import logo, vs
from higher_lower_game_data import data
import random


print(logo)
count = 0

def get_details():
    number = random.randint(0, len(data) -1)
    name = data[number]['name']
    description = data[number]['description']
    country = data[number]['country']
    follower_count = data[number]['follower_count']

    return number, name, description, country, follower_count

user_answer = True

while user_answer:
    number_1, name_1, description_1, country_1, follower_count_1 = get_details()
    number_2, name_2, description_2, country_2, follower_count_2 = get_details()
    if number_1 == number_2:
        number_2, name_2, description_2, country_2, follower_count_2 = get_details()

    print(f"Compare A: {name_1}, a {description_1}, from {country_1}.")
    print(vs)
    print(f"Against B: {name_2}, a {description_2}, from {country_2}.")
    letter = input("Who has more followers? Type 'A' or 'B':").lower()

    if follower_count_1 > follower_count_2:
        answer = "a"
    else:
        answer = "b"

    if answer == letter:
        count += 1
        print(f"You're right! Current score: {count}")
    else:
        user_answer = False
        print(f"Sorry, that's wrong. Final score: {count}")







