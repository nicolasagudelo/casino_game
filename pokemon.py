
from random import randint
from random import random

pokemon_list = ['Bulbasaur','Ivysaur','Venusaur','Charmander†','Charmeleon','Charizard','Squirtle','Wartortle','Blastoise','Caterpie','Metapod','Butterfree','Weedle','Kakuna','Beedrill','Pidgey','Pidgeotto','Pidgeot','Rattata','Raticate','Spearow','Fearow','Ekans','Arbok','Pikachu','Raichu','Sandshrew','Sandslash','Nidoran♀','Nidorina','Nidoqueen','Nidoran♂','Nidorino','Nidoking','Clefairy','Clefable','Vulpix','Ninetales','Jigglypuff','Wigglytuff','Zubat','Golbat','Oddish','Gloom','Vileplume','Paras','Parasect','Venonat','Venomoth','Diglett','Dugtrio','Meowth','Persian','Psyduck','Golduck','Mankey','Primeape','Growlithe','Arcanine','Poliwag','Poliwhirl','Poliwrath','Abra','Kadabra','Alakazam','Machop','Machoke','Machamp','Bellsprout','Weepinbell','Victreebel','Tentacool','Tentacruel','Geodude','Graveler','Golem','Ponyta','Rapidash','Slowpoke','Slowbro','Magnemite','Magneton','Farfetch','Doduo','Dodrio','Seel','Dewgong','Grimer','Muk','Shellder','Cloyster','Gastly','Haunter','Gengar','Onix','Drowzee','Hypno','Krabby','Kingler','Voltorb','Electrode','Exeggcute','Exeggutor','Cubone','Marowak','Hitmonlee','Hitmonchan','Lickitung','Koffing','Weezing','Rhyhorn','Rhydon','Chansey','Tangela','Kangaskhan','Horsea','Seadra','Goldeen','Seaking','Staryu','Starmie','Mr. Mime','Scyther','Jynx','Electabuzz','Magmar','Pinsir','Tauros','Magikarp','Gyarados','Lapras','Ditto','Eeveedagger','Vaporeon','Jolteon','Flareon','Porygon','Omanyte','Omastar','Kabuto','Kabutops','Aerodactyl','Snorlax','Articuno','Zapdos','Moltres','Dratini','Dragonair','Dragonite','Mewtwo','Mew']
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
        while True:
            print('What pokemon do you want to choose as your active pokemon now?\n')
            print('Write the number next to the pokemon you want to choose.\n')
            index = 1
            # We let the player know what pokemons he have and in which position they are so he can choose which pokemon he want to set as active
            for pokemon in self.pokemons:
                if pokemon.isFaint == True:
                    print (index, pokemon.name, 'level:', pokemon.level ,'(fainted)') 
                else:
                    print (index, pokemon.name, 'level:', pokemon.level, 'current HP:', pokemon.health,'/',pokemon.max_health)
                index += 1
            try:
                active = int(input('\n')) - 1
                # we check that the number is not lower than 0 and not greater than the size of the list with the pokemons
                if active < 0 or active >= len(self.pokemons):
                    # We let the player know that his input was not valid
                    print('That number doesn\'t correspond to any pokemon, please write a valid number')
                    continue
                # We check that the pokemon that the trainer chose is not fainted.
                elif self.pokemons[active].isFaint:
                    # We let him know that the selected pokemon has 0 hp and can not fight.
                    print('{pokemon} is out of hp and can\'t fight, choose another active pokemon'.format(pokemon = self.pokemons[active].name))
                    continue
                # We check that he doesn't choose the pokemon that he is already using.
                elif active == self.current_pokemon:
                    # We let him know that he chose the same pokemon he already has as active pokemon.
                    print('{pokemon} is already your active pokemon, choose a different pokemon to switch to'.format(pokemon = self.pokemons[active].name))
                    continue
                # If everything is okay we change the active pokemon.
                else: 
                    self.current_pokemon = active
                    print('{trainer}: Go {pokemon} I choose you!'.format(trainer = self.name, pokemon = self.pokemons[self.current_pokemon].name))
                    break
            except ValueError:
                print('Please choose using only numbers. Select the pokemon you want by typing the number next to it\'s name')
    
    def use_potion(self):
        # Uses a potion on the active pokemon, assuming you have at least one potion.
        if self.potions > 0:
            while True:
                print('On which pokemon do you want to use the potion? (In this game you can revive your pokemon using potions)\n')
                print('Write the number next to the pokemon you want to choose.\n')
                index = 1
                # We let the player know what pokemons he have and in which position they are so he can choose on which pokemon he wants to use the potion.
                for pokemon in self.pokemons:
                    if pokemon.isFaint == True:
                        print (index, pokemon.name, 'level:', pokemon.level ,'(fainted)') 
                    else:
                        print (index, pokemon.name, 'level:', pokemon.level, 'current HP:', pokemon.health,'/',pokemon.max_health)
                    index += 1
                try:
                    pokemon_to_use_potion = int(input('\n')) - 1
                    # we check that the number is not lower than 0 and not greater than the size of the list with the pokemons
                    if pokemon_to_use_potion < 0 or pokemon_to_use_potion >= len(self.pokemons):
                        # We let the player know that his input was not valid
                        print('That number doesn\'t correspond to any pokemon, please write a valid number')
                        continue
                    # If everything is okay we give the potion to the pokemon.
                    else:
                        # If the pokemon is at it's current maximum HP we inform the trainer and don't make him lose his turn
                        if self.pokemons[pokemon_to_use_potion].health == self.pokemons[pokemon_to_use_potion].max_health:
                            print('This pokemon already has the maximum amount of hp it can get, don\'t worry, you won\'t lose your turn.')
                            return False
                        else:
                        # If we get here we give the potion to the pokemon and reduce the amount of potions that the trainer has by 1
                            self.pokemons[pokemon_to_use_potion].gainhealth()
                            self.potions -= 1
                            return True
                            break
                except ValueError:
                    print('Please choose using only numbers. Select the pokemon you want by typing the number next to it\'s name')
        else: print('You don\'t have any potions left.')

        if self.potions > 0:
            print("You used a potion on {name}.".format(name = self.pokemons[self.current_pokemon].name))
            # A potion restores 20 health
            self.pokemons[self.current_pokemon].gain_health(20)
            self.potions -= 1
        else:
            print("You don't have any more potions")
    
    def attack_other_player(self, other_player):
        # Your current pokemon attacks the other trainer's current pokemon
        my_pokemon = self.pokemons[self.current_pokemon]
        their_pokemon = other_player.pokemons[other_player.current_pokemon]
        my_pokemon.attack_other_pokemon(their_pokemon)


class Pokemon:
    def __init__(self, name, type, owner, level = 5):
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
    
    def gainhealth(self):
        # If a pokemon has no health he will be revived.
        if self.health == 0:
            self.revive()
            self.health += 19
        else:
            self.health += 20 
        if self.health > self.max_health:
            self.health = self.max_health
        print ('{name} now has {health} hp'.format(name = self.name, health = self.health))
        
    

    def revive(self):
        # We change the is faint boolean to false since the pokemon is no longer out of combat
        self.isFaint = False
        if self.health == 0:
            self.health = 1
        print('{name} has been revived'.format(name = self.name))
    
    def dodge(self):
        if ((random()*100) < self.speed):
            return True
        return False

    def lose_health(self, damage):
        # We calculate the damage to the pokemon after the attack
        self.health -= damage
        # Check if the pokemon fainted
        if self.health <=0:
            self.health = 0
            self.Faint()
        else:
            print('{pokemon} has taken {damage} damage, it has {health} points remaining'.format(pokemon = self.name, damage = damage, health = self.health))


    def Faint(self):
        self.isFaint = True
        if self.health != 0:
            self.health = 0
        print('{pokemon} has taken too much damage and can not continue fighting'.format(pokemon = self.name))



    def attack_other_pokemon(self, other_pokemon):
        dodge = other_pokemon.dodge()
        if dodge:
            print ('{pokemon_attacked} is too fast!, he dodged {attacker} attack!'.format(pokemon_attacked = other_pokemon.name, attacker = self.name))
        else:
            # Add logic to check the types of both pokemons and calculate the damage taking into account advantages and disadvantages.
            match self.type:
                case 'Normal':
                    if other_pokemon.type == 'Rock':
                        print('{my_pokemon} attacked {their_pokemon}'.format(my_pokemon = self.name, their_pokemon = other_pokemon.name))
                        print('Is not very effective!')
                        other_pokemon.lose_health(self.attack * 0.5)
                    elif other_pokemon.type == 'Ghost':
                        print('{my_pokemon} attacked {their_pokemon}'.format(my_pokemon = self.name, their_pokemon = other_pokemon.name))
                        immune(other_pokemon.name, self.name)
                    else: 
                        print('{my_pokemon} attacked {their_pokemon}'.format(my_pokemon = self.name, their_pokemon = other_pokemon.name))
                        other_pokemon.lose_health(self.attack)
                case 'Fire':
                    if other_pokemon.type == 'Fire' or other_pokemon.type == 'Water' or other_pokemon.type == 'Rock' or other_pokemon.type == 'Dragon':
                        print('{my_pokemon} attacked {their_pokemon}'.format(my_pokemon = self.name, their_pokemon = other_pokemon.name))
                        print('Is not very effective!')
                        other_pokemon.lose_health(self.attack * 0.5)
                    elif other_pokemon.type == 'Grass' or other_pokemon.type == 'Ice' or other_pokemon.type == 'Bug':
                        print('{my_pokemon} attacked {their_pokemon}'.format(my_pokemon = self.name, their_pokemon = other_pokemon.name))
                        print('Is super effective!')
                        other_pokemon.lose_health(self.attack * 2)
                    else:
                        print('{my_pokemon} attacked {their_pokemon}'.format(my_pokemon = self.name, their_pokemon = other_pokemon.name))
                        other_pokemon.lose_health(self.attack)
                case 'Water':
                    if other_pokemon.type == 'Water' or other_pokemon.type == 'Grass' or other_pokemon.type == 'Dragon':
                        print('{my_pokemon} attacked {their_pokemon}'.format(my_pokemon = self.name, their_pokemon = other_pokemon.name))
                        print('Is not very effective!')
                        other_pokemon.lose_health(self.attack * 0.5)
                    elif other_pokemon.type == 'Fire' or other_pokemon.type == 'Ground' or other_pokemon.type == 'Rock':
                        print('{my_pokemon} attacked {their_pokemon}'.format(my_pokemon = self.name, their_pokemon = other_pokemon.name))
                        print('Is super effective!')
                        other_pokemon.lose_health(self.attack * 2)
                    else:
                        print('{my_pokemon} attacked {their_pokemon}'.format(my_pokemon = self.name, their_pokemon = other_pokemon.name))
                        other_pokemon.lose_health(self.attack)
                case 'Electric':
                    if other_pokemon.type == 'Electric' or  other_pokemon.type == 'Grass' or  other_pokemon.type == 'Dragon':
                        print('{my_pokemon} attacked {their_pokemon}'.format(my_pokemon = self.name, their_pokemon = other_pokemon.name))
                        print('Is not very effective!')
                        other_pokemon.lose_health(self.attack * 0.5)
                    elif  other_pokemon.type == 'Water' or  other_pokemon.type == 'Flying':
                        print('{my_pokemon} attacked {their_pokemon}'.format(my_pokemon = self.name, their_pokemon = other_pokemon.name))
                        print('Is super effective!')
                        other_pokemon.lose_health(self.attack * 2)
                    elif other_pokemon.type == 'Ground':
                        immune(other_pokemon.name, self.name)
                    else:
                        print('{my_pokemon} attacked {their_pokemon}'.format(my_pokemon = self.name, their_pokemon = other_pokemon.name))
                        other_pokemon.lose_health(self.attack)
                case 'Grass':
                    if other_pokemon.type == 'Fire' or other_pokemon.type == 'Grass' or  other_pokemon.type == 'Poison' or  other_pokemon.type == 'Flying' or  other_pokemon.type == 'Bug' or  other_pokemon.type == 'Dragon':
                        print('{my_pokemon} attacked {their_pokemon}'.format(my_pokemon = self.name, their_pokemon = other_pokemon.name))
                        print('Is not very effective!')
                        other_pokemon.lose_health(self.attack * 0.5)
                    elif  other_pokemon.type == 'Water' or  other_pokemon.type == 'Ground' or  other_pokemon.type == 'Rock':
                        print('{my_pokemon} attacked {their_pokemon}'.format(my_pokemon = self.name, their_pokemon = other_pokemon.name))
                        print('Is super effective!')
                        other_pokemon.lose_health(self.attack * 2)
                    else:
                        print('{my_pokemon} attacked {their_pokemon}'.format(my_pokemon = self.name, their_pokemon = other_pokemon.name))
                        other_pokemon.lose_health(self.attack)
                case 'Ice':
                    if other_pokemon.type == 'Water' or other_pokemon.type == 'Ice':
                        print('{my_pokemon} attacked {their_pokemon}'.format(my_pokemon = self.name, their_pokemon = other_pokemon.name))
                        print('Is not very effective!')
                        other_pokemon.lose_health(self.attack * 0.5)
                    elif other_pokemon.type == 'Grass' or other_pokemon.type == 'Ground' or other_pokemon.type == 'Flying' or other_pokemon.type == 'Dragon':
                        print('{my_pokemon} attacked {their_pokemon}'.format(my_pokemon = self.name, their_pokemon = other_pokemon.name))
                        print('Is super effective!')
                        other_pokemon.lose_health(self.attack * 2)
                    else:
                        print('{my_pokemon} attacked {their_pokemon}'.format(my_pokemon = self.name, their_pokemon = other_pokemon.name))
                        other_pokemon.lose_health(self.attack)
                case 'Fighting':
                    if other_pokemon.type == 'Poison' or  other_pokemon.type == 'Flying' or  other_pokemon.type == 'Psychic' or other_pokemon.type == 'Bug':
                        print('{my_pokemon} attacked {their_pokemon}'.format(my_pokemon = self.name, their_pokemon = other_pokemon.name))
                        print('Is not very effective!')
                        other_pokemon.lose_health(self.attack * 0.5)
                    elif other_pokemon.type == 'Normal' or  other_pokemon.type == 'Ice' or  other_pokemon.type == 'Rock':
                        print('{my_pokemon} attacked {their_pokemon}'.format(my_pokemon = self.name, their_pokemon = other_pokemon.name))
                        print('Is super effective!')
                        other_pokemon.lose_health(self.attack * 2)
                    elif other_pokemon.type == 'Ghost':
                        immune(other_pokemon.name, self.name)
                    else:
                        print('{my_pokemon} attacked {their_pokemon}'.format(my_pokemon = self.name, their_pokemon = other_pokemon.name))
                        other_pokemon.lose_health(self.attack)
                case 'Poison':
                    if  other_pokemon.type == 'Poison' or  other_pokemon.type == 'Ground' or  other_pokemon.type == 'Rock' or  other_pokemon.type == 'Ghost':
                        print('{my_pokemon} attacked {their_pokemon}'.format(my_pokemon = self.name, their_pokemon = other_pokemon.name))
                        print('Is not very effective!')
                        other_pokemon.lose_health(self.attack * 0.5)
                    elif  other_pokemon.type == 'Grass' or  other_pokemon.type == 'Bug':
                        print('{my_pokemon} attacked {their_pokemon}'.format(my_pokemon = self.name, their_pokemon = other_pokemon.name))
                        print('Is super effective!')
                        other_pokemon.lose_health(self.attack * 2)
                    else:
                        print('{my_pokemon} attacked {their_pokemon}'.format(my_pokemon = self.name, their_pokemon = other_pokemon.name))
                        other_pokemon.lose_health(self.attack)
                case 'Ground':
                    if other_pokemon.type == 'Grass' or other_pokemon.type == 'Bug':
                        print('{my_pokemon} attacked {their_pokemon}'.format(my_pokemon = self.name, their_pokemon = other_pokemon.name))
                        print('Is not very effective!')
                        other_pokemon.lose_health(self.attack * 0.5)
                    elif other_pokemon.type == 'Fire' or other_pokemon.type == 'Electric' or other_pokemon.type == 'Poison' or other_pokemon.type == 'Rock':
                        print('{my_pokemon} attacked {their_pokemon}'.format(my_pokemon = self.name, their_pokemon = other_pokemon.name))
                        print('Is super effective!')
                        other_pokemon.lose_health(self.attack * 2)
                    elif other_pokemon.type == 'Flying':
                        immune(other_pokemon.name, self.name)
                    else:
                        print('{my_pokemon} attacked {their_pokemon}'.format(my_pokemon = self.name, their_pokemon = other_pokemon.name))
                        other_pokemon.lose_health(self.attack)
                case 'Flying':
                    if other_pokemon.type == 'Electric' or other_pokemon.type == 'Rock':
                        print('{my_pokemon} attacked {their_pokemon}'.format(my_pokemon = self.name, their_pokemon = other_pokemon.name))
                        print('Is not very effective!')
                        other_pokemon.lose_health(self.attack * 0.5)
                    elif other_pokemon.type == 'Grass' or other_pokemon.type =='Fighting' or other_pokemon.type == 'Bug':
                        print('{my_pokemon} attacked {their_pokemon}'.format(my_pokemon = self.name, their_pokemon = other_pokemon.name))
                        print('Is super effective!')
                        other_pokemon.lose_health(self.attack * 2)
                    else:
                        print('{my_pokemon} attacked {their_pokemon}'.format(my_pokemon = self.name, their_pokemon = other_pokemon.name))
                        other_pokemon.lose_health(self.attack)
                case 'Psychic':
                    if other_pokemon.type == 'Psychic':
                        print('{my_pokemon} attacked {their_pokemon}'.format(my_pokemon = self.name, their_pokemon = other_pokemon.name))
                        print('Is not very effective!')
                        other_pokemon.lose_health(self.attack * 0.5)
                    elif other_pokemon.type == 'Fighting' or other_pokemon.type == 'Poison':
                        print('{my_pokemon} attacked {their_pokemon}'.format(my_pokemon = self.name, their_pokemon = other_pokemon.name))
                        print('Is super effective!')
                        other_pokemon.lose_health(self.attack * 2)
                    else:
                        print('{my_pokemon} attacked {their_pokemon}'.format(my_pokemon = self.name, their_pokemon = other_pokemon.name))
                        other_pokemon.lose_health(self.attack)
                case 'Bug':
                    if other_pokemon.type == 'Fire' or other_pokemon.type == 'Fighting' or other_pokemon.type == 'Flying' or other_pokemon.type == 'Ghost':
                        print('{my_pokemon} attacked {their_pokemon}'.format(my_pokemon = self.name, their_pokemon = other_pokemon.name))
                        print('Is not very effective!')
                        other_pokemon.lose_health(self.attack * 0.5)
                    elif other_pokemon.type == 'Grass' or other_pokemon.type == 'Poison' or other_pokemon.type == 'Psychic':
                        print('{my_pokemon} attacked {their_pokemon}'.format(my_pokemon = self.name, their_pokemon = other_pokemon.name))
                        print('Is super effective!')
                        other_pokemon.lose_health(self.attack * 2)
                    else:
                        print('{my_pokemon} attacked {their_pokemon}'.format(my_pokemon = self.name, their_pokemon = other_pokemon.name))
                        other_pokemon.lose_health(self.attack)
                case 'Rock':
                    if other_pokemon.type == 'Fighting' or other_pokemon.type == 'Ground':
                        print('{my_pokemon} attacked {their_pokemon}'.format(my_pokemon = self.name, their_pokemon = other_pokemon.name))
                        print('Is not very effective!')
                        other_pokemon.lose_health(self.attack * 0.5)
                    elif other_pokemon.type == 'Fire' or other_pokemon.type == 'Ice' or other_pokemon.type == 'Flying' or other_pokemon.type == 'Bug':
                        print('{my_pokemon} attacked {their_pokemon}'.format(my_pokemon = self.name, their_pokemon = other_pokemon.name))
                        print('Is super effective!')
                        other_pokemon.lose_health(self.attack * 2)
                    else:
                        print('{my_pokemon} attacked {their_pokemon}'.format(my_pokemon = self.name, their_pokemon = other_pokemon.name))
                        other_pokemon.lose_health(self.attack)
                case 'Ghost':
                    if other_pokemon.type == 'Normal' or other_pokemon.type == 'Psychic':
                        immune(other_pokemon.name, self.name)
                    elif other_pokemon.type == 'Ghost':
                        print('{my_pokemon} attacked {their_pokemon}'.format(my_pokemon = self.name, their_pokemon = other_pokemon.name))
                        print('Is super effective!')
                        other_pokemon.lose_health(self.attack * 2)
                    else:
                        print('{my_pokemon} attacked {their_pokemon}'.format(my_pokemon = self.name, their_pokemon = other_pokemon.name))
                        other_pokemon.lose_health(self.attack)
                case 'Dragon':
                    if other_pokemon.type == 'Dragon':
                        print('{my_pokemon} attacked {their_pokemon}'.format(my_pokemon = self.name, their_pokemon = other_pokemon.name))
                        print('Is super effective!')
                        other_pokemon.lose_health(self.attack * 2)
                    else:
                        print('{my_pokemon} attacked {their_pokemon}'.format(my_pokemon = self.name, their_pokemon = other_pokemon.name))
                        other_pokemon.lose_health(self.attack)


        
def immune(pokemon_attacked, attacker):
    print ('{pokemon_attacked} is immune to {attacker} attacks! Try attacking with other Pokemon'.format(pokemon_attacked = pokemon_attacked, attacker = attacker))

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
        level = randint(5,15)
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
    # turn = 1
    # Create logic for turn base combat between both trainers
    combat = True
    while combat == True:
        if turn == 1:
            decision = int(input('It\'s your turn {trainer1} your current active pokemon is {active_pokemon} what do you want to do?\n1. Attack\n2. Use potion\n3. Change Pokemon\n'.format(trainer1 = player_one.name, active_pokemon = player_one.pokemons[player_one.current_pokemon].name)))
            match decision:
                case 1:
                    player_one.attack_other_player(player_two)
                case 2: 
                    potion_was_used = player_one.use_potion()
                    if not potion_was_used: continue
                case 3: 
                    player_one.switch_pokemon()
            turn = 2
        elif turn == 2:
            decision = int(input('It\'s your turn {trainer2} your current active pokemon is {active_pokemon} what do you want to do?\n1. Attack\n2. Use potion\n3. Change Pokemon\n'.format(trainer2 = player_two.name, active_pokemon = player_two.pokemons[player_two.current_pokemon].name)))
            match decision:
                case 1: 
                    player_two.attack_other_player(player_one)
                case 2:
                    potion_was_used = player_two.use_potion()
                    if not potion_was_used: continue
                case 3: 
                    player_two.switch_pokemon()
            turn = 1
            # combat = False



menu()

