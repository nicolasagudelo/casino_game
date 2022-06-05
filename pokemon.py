from os import curdir
from random import randint

from pkg_resources import compatible_platforms

pokemon_list = ['Bulbasaur','Ivysaur','Venusaur','Charmander†','Charmeleon','Charizard','Squirtle','Wartortle','Blastoise','Caterpie','Metapod','Butterfree','Weedle','Kakuna','Beedrill','Pidgey','Pidgeotto','Pidgeot','Rattata','Raticate','Spearow','Fearow','Ekans','Arbok','Pikachudagger','Raichu','Sandshrew','Sandslash','Nidoran♀','Nidorina','Nidoqueen','Nidoran♂','Nidorino','Nidoking','Clefairy','Clefable','Vulpix','Ninetales','Jigglypuff','Wigglytuff','Zubat','Golbat','Oddish','Gloom','Vileplume','Paras','Parasect','Venonat','Venomoth','Diglett','Dugtrio','Meowth','Persian','Psyduck','Golduck','Mankey','Primeape','Growlithe','Arcanine','Poliwag','Poliwhirl','Poliwrath','Abra','Kadabra','Alakazam','Machop','Machoke','Machamp','Bellsprout','Weepinbell','Victreebel','Tentacool','Tentacruel','Geodude','Graveler','Golem','Ponyta','Rapidash','Slowpoke','Slowbro','Magnemite','Magneton','Farfetch','Doduo','Dodrio','Seel','Dewgong','Grimer','Muk','Shellder','Cloyster','Gastly','Haunter','Gengar','Onix','Drowzee','Hypno','Krabby','Kingler','Voltorb','Electrode','Exeggcute','Exeggutor','Cubone','Marowak','Hitmonlee','Hitmonchan','Lickitung','Koffing','Weezing','Rhyhorn','Rhydon','Chansey','Tangela','Kangaskhan','Horsea','Seadra','Goldeen','Seaking','Staryu','Starmie','Mr. Mime','Scyther','Jynx','Electabuzz','Magmar','Pinsir','Tauros','Magikarp','Gyarados','Lapras','Ditto','Eeveedagger','Vaporeon','Jolteon','Flareon','Porygon','Omanyte','Omastar','Kabuto','Kabutops','Aerodactyl','Snorlax','Articuno','Zapdos','Moltres','Dratini','Dragonair','Dragonite','Mewtwo','Mew']
pokemon_type = ['Grass', 'Grass', 'Grass', 'Fire', 'Fire', 'Fire', 'Water', 'Water', 'Water', 'Bug', 'Bug', 'Bug', 'Bug', 'Bug', 'Bug', 'Normal', 'Normal', 'Normal', 'Normal', 'Normal', 'Normal', 'Normal', 'Poison', 'Poison', 'Electric', 'Electric', 'Ground', 'Ground', 'Poison', 'Poison', 'Poison', 'Poison', 'Poison', 'Poison', 'Fairy', 'Fairy', 'Fire', 'Fire', 'Normal', 'Normal', 'Poison', 'Poison', 'Grass', 'Grass', 'Grass', 'Bug', 'Bug', 'Bug', 'Bug', 'Ground', 'Ground', 'Normal', 'Normal', 'Water', 'Water', 'Fighting', 'Fighting', 'Fire', 'Fire', 'Water', 'Water', 'Water', 'Psychic', 'Psychic', 'Psychic', 'Fighting', 'Fighting', 'Fighting', 'Grass', 'Grass', 'Grass', 'Water', 'Water', 'Rock', 'Rock', 'Rock', 'Fire', 'Fire', 'Water', 'Water', 'Electric', 'Electric', 'Normal', 'Normal', 'Normal', 'Water', 'Water', 'Poison', 'Poison', 'Water', 'Water', 'Ghost', 'Ghost', 'Ghost', 'Rock', 'Psychic', 'Psychic', 'Water', 'Water', 'Electric', 'Electric', 'Grass', 'Grass', 'Ground', 'Ground', 'Fighting', 'Fighting', 'Normal', 'Poison', 'Poison', 'Ground', 'Ground', 'Normal', 'Grass', 'Normal', 'Water', 'Water', 'Water', 'Water', 'Water', 'Water', 'Psychic', 'Bug', 'Ice', 'Electric', 'Fire', 'Bug', 'Normal', 'Water', 'Water', 'Water', 'Normal', 'Normal', 'Water', 'Electric', 'Fire', 'Normal', 'Rock', 'Rock', 'Rock', 'Rock', 'Rock', 'Normal', 'Ice', 'Electric', 'Fire', 'Dragon', 'Dragon', 'Dragon', 'Psychic', 'Psychic']

class Player:
    def __init__(self, name, pokemon_list, num_potions):
        self.pokemons = pokemon_list
        self.potions = num_potions
        self.current_pokemon = 0
        self.name = name

    def __repr__(self) -> str:
        # Printing the player will tell us their name, the amount of potions they have, the pokemon they have and which is their active pokemon.
        print("This trainer name is: {name}.\nHere is the list of pokemons that {name} has:".format(name = self.name))
        for pokemon in self.pokemons:
            print(pokemon)
        print('{name} currently has {potions} potions'.format(name = self.name, potions = self.potions))
        return('The current active pokemon is {pokemon}'.format(pokemon = self.pokemons[self.current_pokemon].name))

    def switch_pokemon(self):
        print('What pokemon do you want to choose as your active pokemon now?\n')
        print('Write the number next to the pokemon you want to choose.\n')
        index = 1
        for pokemon in self.pokemons:
            print (index, pokemon.name)
            index += 1
        active = int(input('\n')) - 1
        self.current_pokemon = active
        print('{Trainer} your new active pokemon is {active_pokemon}'.format(Trainer = self.name, active_pokemon = self.pokemons[self.current_pokemon].name))
    """
    def switch_active_pokemon(self, new_active):
        # Switches the active pokemon to the number given as a parameter
        # First checks to see the number is valid (between 0 and the length of the list)
        if new_active < len(self.pokemons) and new_active >= 0:
            # You can't switch to a pokemon that is knocked out
            if self.pokemons[new_active].is_knocked_out:
                print("{name} is knocked out. You can't make it your active pokemon".format(name = self.pokemons[new_active].name))
            # You can't switch to your current pokemon
            elif new_active == self.current_pokemon:
                print("{name} is already your active pokemon".format(name = self.pokemons[new_active].name))
            # Switches the pokemon
            else:
                self.current_pokemon = new_active
                print("Go {name}, it's your turn!".format(name = self.pokemons[self.current_pokemon].name))

    def use_potion(self):
        # Uses a potion on the active pokemon, assuming you have at least one potion.
        if self.potions > 0:
            print("You used a potion on {name}.".format(name = self.pokemons[self.current_pokemon].name))
            # A potion restores 20 health
            self.pokemons[self.current_pokemon].gain_health(20)
            self.potions -= 1
        else:
            print("You don't have any more potions")

    def attack_other_trainer(self, other_trainer):
        # Your current pokemon attacks the other trainer's current pokemon
        my_pokemon = self.pokemons[self.current_pokemon]
        their_pokemon = other_trainer.pokemons[other_trainer.current_pokemon]
        my_pokemon.attack(their_pokemon)
    """


class Pokemon:
    def __init__(self, name, type, owner, level = 1):
        self.name = name
        self.level = level
        self.health = level * 5
        self.max_health = level * 5
        self.attack = round(level * 0.7)
        self.defense = round(level * 0.3)
        self.speed = randint(0, 40)
        self.type = type
        self.isFaint = False
        self.owner = owner
    
    def __repr__(self) -> str:
        # Printing a pokemon will tell us it's name, level, current health, and type
        return ('{name} is a level {level} {type} pokemon, his current health is {current_health} out of {full_health}'.format(name = self.name, level = self.level, type = self.type, current_health = self.health, full_health = self.max_health))
        


def create_player():
    while True:
        
        name = input("Please start by typing the trainer name\n")
        try:
            answer = input("The name you wrote is {name}. Is this the correct name? \n(Type Y if yes, or, N if no)\n".format(name = name))
            answer = answer.upper()
            match answer:
                case 'Y': break
                case 'N': continue
                case _: 
                    print("Please type Y for yes, or, N for no. Other answers are not supported.") 
                    continue
        except ValueError :
            print("Sorry we didn\'t get that, please try again\n")
            continue
    
    print("Thanks {name}, you will now receive 5 random pokemon for your battle.\n".format(name = name))

    # Add a random method to give the trainer 5 pokemons from the pokemon list

    trainer_pokemon = []
    for i in range(0,5,1):
        position = randint(0,150)
        level = randint(0,10)
        trainer_pokemon.append(Pokemon(pokemon_list[position],pokemon_type[position], name, level))


    # Create player once we have all his information collected:

    return (Player(name, trainer_pokemon, randint(1,5)))

def coinflip(name1, name2):
    random_number = randint(1,2)
    Head_Tails = ""
    #Promp the user for their guess
    while True:
        try:
            guess = input("{player} write your guess, Heads or Tails\n".format(player = name1))
            guess = guess.upper().strip()
            if guess == 'HEADS' or guess == 'TAILS': break
            print ('Please write, Heads or Tails as your guess')
        except ValueError:
            print('Sorry we didn\'t get your guess please write it again.')


    #Depending on the random number generated we define the correct Head_Tails

    Head_Tails = "HEADS" if random_number == 1 else "TAILS"

    print("\nCoin landed on:", str(Head_Tails.capitalize()))
    print ("\nYour guess was...", str(guess.capitalize()))

    if guess == Head_Tails:
        print ("\n{player} won the coin flip you will go first".format(player = name1))
        return 1
    else: 
        print("\n{playerone} lost the coin flip {playertwo} will go first".format(playerone = name1, playertwo = name2))
        return 2


def menu():
    print('Welcome to pokemon random battle, in this game two trainers will receive 5 random pokemon and a random number of potions to battle each other\nI hope you have good luck!\n')
    print('Let\'s start with trainer #1\n')
    player_one = create_player()
    print('Now let\'s do the same for trainer #2\n')
    player_two = create_player()
    print('\nGreat, let\'s have a look of how our two trainers look like\n')
    print('Player one:\n')
    print(player_one)
    print('Player two:\n')
    print(player_two)

    # Decide who will have the first turn by guessing heads or tails
    print('\nNow let\'s decide who will have the first turn by tossing a coin.')
    turn = coinflip(player_one.name, player_two.name)
    turn = 1
    # Create logic for turn base combat between both trainers
    combat = True
    while combat == True:
        if turn == 1:
            decision = int(input('It\'s your turn {trainer1} your current active pokemon is {active_pokemon} what do you want to do?\n1. Attack\n2. Use potion\n3. Change Pokemon\n'.format(trainer1 = player_one.name, active_pokemon = player_one.pokemons[player_one.current_pokemon].name)))
            match decision:
                case 1: print ('Attack!')
                case 2: print ('Use potion')
                case 3: 
                    player_one.switch_pokemon()

            turn = 2
        elif turn == 2:
            decision = int(input('It\'s your turn {trainer2} your current active pokemon is {active_pokemon} what do you want to do?\n1. Attack\n2. Use potion\n3. Change Pokemon\n'.format(trainer2 = player_two.name, active_pokemon = player_two.pokemons[player_two.current_pokemon].name)))
            match decision:
                case 1: print ('Attack!')
                case 2: print ('Use potion')
                case 3: 
                    player_two.switch_pokemon()
            turn = 1
            # combat = False



menu()

