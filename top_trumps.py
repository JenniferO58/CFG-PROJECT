import random
import requests
from time import sleep

my_score = 0
opponent_score = 0
games = 0

username = input("\nWhat is your name? ")
print("\nHey {}, welcome to the online Top Trumps game!\n".format(username))
sleep(1)
print("You can either choose to play with Pokemon characters or Superheroes.\n")
sleep(1)
print("At the end of the game, final scores will be multiplied by 5. Whoever scores the highest wins.\n")
sleep(1)

def random_pokemon():
    random_selection = random.randint(1, 151)
    url = "https://pokeapi.co/api/v2/pokemon/{}/".format(random_selection)
    response = requests.get(url)
    pokemon = response.json()

    return {
        "name": pokemon["name"],
        "id": pokemon["id"],
        "height": pokemon["height"],
        "weight": pokemon["weight"]
    }

def print_pokemon_stats(my_choice, opponent_choice):
    print("You were given {}\n".format(my_choice["name"]))
    sleep(2)
    print("Your opponent's chosen Pokemon is {}\n".format(opponent_choice["name"]))
    sleep(1.5)
    print("{}'s stats: "
          "\n ID: {} "
          "\n Height: {}"
          "\n Weight: {} ".format(my_choice["name"], my_choice["id"], my_choice["height"], my_choice["weight"]))

def print_pokemon_opponent_stat(stat_choice, opponent_choice):
    if stat_choice == "id":
        print("The stat data for your opponent's chosen Pokemon is is {}\n ".format(opponent_choice["id"]))
    elif stat_choice == "height":
        print("The stat data for your opponent's chosen Pokemon is {}\n ".format(opponent_choice["height"]))
    elif stat_choice == "weight":
        print("The stat data for your opponent's chosen Pokemon is {}\n ".format(opponent_choice["weight"]))

def user_stat_choice_pokemon():
    stat_choice = input("\nWhich stat do you want to use? (id, height, weight): ")
    valid_choices = ['id', 'height', 'weight']
    while stat_choice not in valid_choices:
        stat_choice = input("\n Please try again, invalid stat choice entered. Choose either (id, height, weight): ")
    return stat_choice


def play_pokemon_top_trumps_round():
    my_choice = random_pokemon()
    opponent_choice = random_pokemon()

    print_pokemon_stats(my_choice, opponent_choice)

    stat_choice = user_stat_choice_pokemon()
    sleep(1.5)
    print("\nYour opponent's chosen stat is {} \n".format(stat_choice))
    sleep(1.5)

    my_stat = my_choice[stat_choice]
    opponent_stat = opponent_choice[stat_choice]

    print_pokemon_opponent_stat(stat_choice, opponent_choice)
    calculate_pokemon_scores(my_stat, opponent_stat)


def random_superhero_character():
    random_superhero = random.randint(1, 500)
    url = "https://www.superheroapi.com/api.php/3631677060217708/{}/".format(random_superhero)
    response = requests.get(url)
    superhero = response.json()

    return dict(name=superhero["name"], id=superhero["id"], powerstats=superhero["powerstats"],
                intelligence=superhero["powerstats"]["intelligence"], strength=superhero["powerstats"]["strength"],
                speed=superhero["powerstats"]["speed"], durability=superhero["powerstats"]["durability"],
                power=superhero["powerstats"]["power"], combat=superhero["powerstats"]["combat"])

def print_superhero_stats(my_superhero_choice, opponent_superhero_choice):
    print("You were given {}\n".format(my_superhero_choice["name"]))
    sleep(2)
    print("Your opponent's chosen superhero is {}\n".format(opponent_superhero_choice["name"]))
    sleep(1.5)
    print('{}\'s stats: '
          '\n Intelligence: {} '
          '\n Strength: {}'
          '\n Speed: {}'
          '\n Durability: {} '
          '\n Power: {}'
          '\n Combat: {}'.format(my_superhero_choice["name"], my_superhero_choice["powerstats"]["intelligence"], my_superhero_choice["powerstats"]["strength"], my_superhero_choice["powerstats"]["speed"], my_superhero_choice["powerstats"]["durability"], my_superhero_choice["powerstats"]["power"], my_superhero_choice["powerstats"]["combat"]))

def print_superhero_opponent_stat(superhero_stat_choice, superhero_opponent_choice):
    if superhero_stat_choice == "intelligence":
        print("The stat data for your opponent's chosen superhero is is {}\n ".format(superhero_opponent_choice["powerstats"]["intelligence"]))
    elif superhero_stat_choice == "strength":
        print("The stat data for your opponent's chosen superhero is {}\n ".format(superhero_opponent_choice["powerstats"]["strength"]))
    elif superhero_stat_choice == "speed":
        print("The stat data for your opponent's chosen superhero is {}\n ".format(superhero_opponent_choice["powerstats"]["speed"]))
    elif superhero_stat_choice == "durability":
        print("The stat data for your opponent's chosen superhero is {}\n ".format(superhero_opponent_choice["powerstats"]["durability"]))
    elif superhero_stat_choice == "power":
        print("The stat data for your opponent's chosen superhero is {}\n ".format(superhero_opponent_choice["powerstats"]["power"]))
    elif superhero_stat_choice == "combat":
        print("The stat data for your opponent's chosen superhero is {}\n ".format(superhero_opponent_choice["powerstats"]["combat"]))

def user_stat_choice_superhero():
    stat_choice = input("\nWhich stat do you want to use? (intelligence, strength, speed, durability, power, combat): ")
    valid_choices = ["intelligence", "strength", "speed", "durability", "power", "combat"]
    while stat_choice not in valid_choices:
        stat_choice = input("Please try again, invalid stat choice entered. Choose either (intelligence, strength, speed, durability, power, combat)\n : ")
    return stat_choice

def calculate_pokemon_scores(my_stat, opponent_stat):
    global my_score, opponent_score

    if my_stat > opponent_stat:
      sleep(0.5)
      print("You win this round!\n")
      my_score += 2
      sleep(0.5)
      print("You have {} points".format(my_score))

    elif my_stat < opponent_stat:
      sleep(0.5)
      print("You lose this round!\n")
      opponent_score += 2
      sleep(0.5)
      print("Your opponent now has {} points".format(opponent_score))

    else:
        sleep(0.5)
        print("It's a draw!\n")
        my_score += 1
        opponent_score += 1
        sleep(0.5)
        print("You have {} point(s) and your opponent has {} point(s)".format(my_score, opponent_score))

def calculate_superhero_scores(my_superhero_stat, opponent_superhero_stat):
    global my_score, opponent_score

    if my_superhero_stat > opponent_superhero_stat:
      sleep(0.5)
      print("You win this round!\n")
      my_score += 2
      sleep(0.5)
      print("You have {} points".format(my_score))

    elif my_superhero_stat < opponent_superhero_stat:
      sleep(0.5)
      print("You lose this round!\n")
      opponent_score += 2
      sleep(0.5)
      print("Your opponent now has {} points".format(opponent_score))

    else:
        sleep(0.5)
        print("It's a draw!\n")
        my_score += 1
        opponent_score += 1
        sleep(0.5)
        print("You have {} point(s) and your opponent has {} point(s)".format(my_score, opponent_score))

def play_superhero_top_trumps_round():
    my_choice = random_superhero_character()
    opponent_choice = random_superhero_character()

    print_superhero_stats(my_choice, opponent_choice)

    stat_choice = user_stat_choice_superhero()
    sleep(1.5)
    print("\nYour opponent's chosen stat is {} \n".format(stat_choice))
    sleep(1.5)

    my_stat = my_superhero_choice[stat_choice]
    opponent_stat = opponent_superhero_choice[stat_choice]

    print_superhero_opponent_stat(stat_choice, opponent_choice)

    calculate_superhero_scores(my_superhero_stat, opponent_superhero_stat)

    my_stat = my_choice[stat_choice]
    opponent_stat = opponent_choice[stat_choice]

    print_pokemon_opponent_stat(stat_choice, opponent_choice)
    calculate_pokemon_scores(my_stat, opponent_stat)


game_request = input("So, what will it to be today? Pokemon or Superheroes?: ")
comment = int(input("\nHow many rounds would you like to play?: "))
print("\nGreat! You have selected {} rounds(s)\n".format(comment))

while games < comment:
    print("*" * 300)
    sleep(1)
    print("ROUND {}\n".format(games + 1))
    games += 1

    if game_request == "superheroes":
      play_superhero_top_trumps_round()
    elif game_request == "pokemon":
      play_pokemon_top_trumps_round()

if my_score > opponent_score:
    print("*" * 300)
    my_new_score = my_score * 5
    sleep(1)
    print("\nCongratulations {}, you have won the game with {} points!".format(username, my_new_score))

elif my_score < opponent_score:
    print("*" * 300)
    opponent_new_score = opponent_score * 5
    sleep(1)
    print("\nUnfortunately {}, you have lost the game to your opponent who scored {} points overall.".format(username, opponent_new_score))

elif my_score == opponent_score:
    print("*" * 300)
    my_new_score = my_score * 5
    opponent_new_score = opponent_score * 5
    sleep(1)
    print("\nYou and your opponent have both finished the game with {} points. Better luck next time!".format(
        my_new_score))



# filename = "project.txt"
#
# with open(filename, "a") as score_count:
#     score_count.write("My score, computer score \n")
#     # score_count.write(str(my_score))
#     # score_count.write(str(opponent_score))
