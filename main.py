import random

# Initialize game variables
player_name = input("Enter your player name: ")
pokeballs = 5
money = 100
level = 1
caught_pokemon = []

def read_pokemon_names():
    with open("pokemons.txt", "r") as file:
        pokemons = file.read().splitlines()
    return pokemons

def catch_pokemon():
    global pokeballs, money, caught_pokemon
    pokemons = read_pokemon_names()
    pokemon = random.choice(pokemons)
    print(f"A wild {pokemon} appears!")
    action = input("Enter 'C' to catch or 'R' to run: ")
    if action.upper() == "C":
        if pokeballs > 0:
            pokeballs -= 1
            if random.random() < 0.5:
                print(f"You caught the {pokemon}!")
                caught_pokemon.append(pokemon)
            else:
                print(f"{pokemon} escaped!")
        else:
            print("You don't have any pokeballs!")
    else:
        print("You ran away!")

def visit_shop():
    global pokeballs, money
    print("Welcome to the Shop!")
    print("Pokeballs: $10 each")
    quantity = int(input("Enter the number of pokeballs you want to buy: "))
    if money >= (10 * quantity):
        pokeballs += quantity
        money -= 10 * quantity
        print(f"You bought {quantity} pokeballs!")
    else:
        print("You don't have enough money!")

def battle():
    global level, money
    opponent_level = random.randint(1, 10)
    print(f"A wild Pokemon (Level {opponent_level}) appears!")
    while True:
        action = input("Enter 'A' to attack or 'R' to run: ")
        if action.upper() == "A":
            player_attack = random.randint(1, level)
            opponent_attack = random.randint(1, opponent_level)
            if player_attack >= opponent_attack:
                print("You won the battle!")
                money += opponent_level * 10
                level += 1
                break
            else:
                print("You lost the battle!")
                break
        elif action.upper() == "R":
            print("You ran away!")
            break
        else:
            print("Invalid input. Try again!")

def see_caught_pokemon():
    print(f"\n{player_name}'s Caught Pokemon:")
    if len(caught_pokemon) > 0:
        for pokemon in caught_pokemon:
            print(pokemon)
    else:
        print("No Pokemon caught yet!")

def play_game():
    while level <= 10:
        print(f"\n----- Level {level} -----")
        print(f"Player: {player_name}")
        print(f"Pokeballs: {pokeballs}")
        print(f"Money: ${money}")
        action = input("Enter 'C' to catch a Pokemon, 'S' to visit the shop, 'B' to battle, 'P' to see caught Pokemon, or 'Q' to quit: ")
        if action.upper() == "C":
            catch_pokemon()
        elif action.upper() == "S":
            visit_shop()
        elif action.upper() == "B":
            battle()
        elif action.upper() == "P":
            see_caught_pokemon()
        elif action.upper() == "Q":
            print("Thanks for playing!")
            break
        else:
            print("Invalid input. Try again!")

# Start the game
print("Welcome to the Pokemon Game!")
play_game()
