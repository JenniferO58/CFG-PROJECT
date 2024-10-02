import random
from time import sleep

my_score = 0
opponent_score = 0
games = 0

print("Welcome to the Pokemon Top Trumps Game!\n")
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

def print_pokemon_stats():
    print("You were given {}\n".format(my_choice["name"]))
    sleep(2)
    print("Your opponent's chosen Pokemon is {}\n".format(opponent_choice["name"]))
    sleep(1.5)
    print("{}'s stats: "
          "\n ID: {} "
          "\n Height: {}"
          "\n Weight: {} ".format(my_choice["name"], my_choice["id"], my_choice["height"], my_choice["weight"]))

def print_opponent_stat(stat_choice, opponent_choice):
    if stat_choice == "id":
        print("The stat data for your opponent's chosen Pokemon is is {}\n ".format(opponent_choice["id"]))
    elif stat_choice == "height":
        print("The stat data for your opponent's chosen Pokemon is {}\n ".format(opponent_choice["height"]))
    elif stat_choice == "weight":
        print("The stat data for your opponent's chosen Pokemon is {}\n ".format(opponent_choice["weight"]))

def run():
    my_choice = random_pokemon()
    opponent_choice = random_pokemon()

    print("You were given {}\n".format(my_choice["name"]))
    sleep(2)
    print("Your opponent's chosen Pokemon is {}\n".format(opponent_choice["name"]))
    sleep(1.5)
    print("{}'s stats: "
          "\n ID: {} "
          "\n Height: {}"
          "\n Weight: {} ".format(my_choice["name"], my_choice["id"], my_choice["height"], my_choice["weight"]))
    stat_choice = input("\nWhich stat do you want to use? (id, height, weight): ")

    sleep(1.5)
    print("\nYour opponent's chosen stat is {} \n".format(stat_choice))
    sleep(1.5)


    my_stat = my_choice[stat_choice]
    opponent_stat = opponent_choice[stat_choice]

    global my_score, opponent_score

    if my_stat > opponent_stat:
        sleep(0.5)
        print("You win this round!\n")
        my_score += 2
        sleep(0.5)
        print("You have {} points!".format(my_score))
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
        print("You have {} point(s) and your opponent has {} points".format(my_score, opponent_score))


comment = int(input("\nHow many rounds would you like to play today?: "))
print("Great! You have selected {} rounds(s)\n".format(comment))

while games < comment:
    print("*" * 200)
    sleep(1)
    print("ROUND {}".format(games + 1))
    games += 1

    # print_opponent_stat(stat_choice, opponent_choice)
    run()

if my_score > opponent_score:
    my_new_score = my_score * 5
    sleep(1)
    print("\nCongratulations, you have won the game with {} points!".format(my_new_score))
elif my_score < opponent_score:
    opponent_new_score = opponent_score * 5
    sleep(1)
    print("\nUnfortunately, you have lost the game to your opponent who scored {} points overall.".format(
        opponent_new_score))

# filename = "project.txt"
#
# with open(filename, "a") as score_count:
#     score_count.write("My score, computer score \n")
#     # score_count.write(str(my_score))
#     # score_count.write(str(opponent_score))
