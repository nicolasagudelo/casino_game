from random import randint

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
    # Create logic for turn base combat between both trainers
    

menu()

