# Names:        Hormuz Buhariwalla
#               Walter Dance
#               Owen Soper
#               Ashton Hull
# 
# Title:        Pokemon Game
# Date:         11/18/2022

import random  # random module used in minigame and for catching pokemon

player_change = 'no'  # preset variable, changed in the main loop at the bottom based on input
quit_game = 'no'

pokemon_file = open('PokeList_v2.csv', 'r')  # opens, then reads the pokemon list csv file
pokemon_file_list = pokemon_file.readlines()


def candy_received():
    '''Randomly generate 3, 5 or 10 candies. Returns a value of 3, 5 or 10 for the candy obtained.'''
    num = random.randint(1, 3)
    if num == 1:
        candy = 3
    elif num == 2:
        candy = 5
    else:
        candy = 10

    return candy


def mini_game():
    '''Called when the player chooses to try and catch a new pokemon. It is a game where the player must guess an
    integer chosen at random (either 1, 2, or 3) and, if successful, will return a value that is used by
    generate_new_pokemon().'''

    number = random.randint(1, 3)
    try:  # try-except blocks used for potential erron in minigame input, i.e. not an integer
        guess = int(
            input('There is a secret integer between 1 & 3 (inclusive). Guess what it is to get a new pokemon: '))
        print()
        if guess == number:
            print('You guessed the number!')
            return 1

        else:
            print('Incorrect, the number was', number)
            return

    except:
        print('That is not an integer!')
        return


def generate_new_pokemon():
    '''Checks if current player’s list is empty. If so, the random pokemon is added to the list,
    otherwise, prints text that indicates the user is in an encounter, causing the user to enter an
    event where mini_game() is called so that the user may attempt to catch the pokemon. If mini_game
    returns the correct value, the randomly generated pokemon is added to the list. Also calls candy_received()'''
    random_pokemon_num = random.randint(1, len(pokemon_file_list) - 1)  # random pokemon
    pokemon_line_split = pokemon_file_list[random_pokemon_num].split(',')  # splits csv file
    random_pokemon = pokemon_line_split[1]
    if len(current_player_list) == 0:  # gives player a pokemon to start off with
        current_player_list.append(random_pokemon)
        pokemon_CP = random.randint(int(pokemon_line_split[2]), int(pokemon_line_split[3]) + 1)
        current_player_CP_list.append(pokemon_CP)
        pokemon_type = pokemon_line_split[9]
        current_player_type_list.append(pokemon_type)
        new_candy = 0
    else:
        print(f"You have entered a battle encounter with {random_pokemon}!")  # starts the battle
        if mini_game() == 1:  # if player wins the minigame
            new_candy = candy_received()  # receives candy amount from candy_received()
            print(f"You caught {str(random_pokemon)} and earned {new_candy} candies!")
            current_player_list.append(random_pokemon)
            pokemon_CP = random.randint(int(pokemon_line_split[2]), int(pokemon_line_split[3]) + 1)
            current_player_CP_list.append(pokemon_CP)
            pokemon_type = pokemon_line_split[9]
            current_player_type_list.append(pokemon_type)
        else:
            print(f"You did not catch {str(random_pokemon)}!")
            new_candy = 0

    return new_candy  # returns how much candy was awarded for the total candy count shown in the menus


def current_pokemon_menu(candy_count):
    '''Views the currently selected pokemon and displays its name, CP, and type. Also accesses the global candy_count
    variable to display the player's total candies. Pokemon information is accessed from lists that are created for
    each respective statistic, which is handled in generate_new_pokemon().'''
    print('---------------------------      Current Pokemon     ---------------------------')
    print(f'Pokemon Name: {current_player_list[0]}\nPokemon CP: {current_player_CP_list[0]}\nPokemon Type: {current_player_type_list[0]}')  # displays current pokemon statistics
    print()
    print(f"Candies: {candy_count}")
    print()

    print("--------------------------------------------------------------------------------\n")


def pokemon_selection_menu(candy_count, current_player_list):
    '''Displays all of a player’s collected pokemon, the currently selected pokemon, and the total candies.'''
    print("---------------------------  Pokemon Selection Menu  ---------------------------")
    print(f"Current Pokemon: {current_player_list[0]}")
    print()
    print(f"Candies: {candy_count}")
    print()
    x = 0
    for pokemon in current_player_list:  # loop for displaying each pokemon in the player's possession
        x += 1
        print(f'{x}. \nPokemon Name: {pokemon}\nPokemon CP: {current_player_CP_list[current_player_list.index(pokemon)]}\nPokemon Type: {current_player_type_list[current_player_list.index(pokemon)]}')

    print("--------------------------------------------------------------------------------\n")


def main_menu():
    '''Displays the main menu and player input options available.'''
    print()
    print("----------------------------       MAIN MENU       -----------------------------")
    print()

    print("1. View current Pokemon")
    print("2. Catch a new Pokemon")
    print("3. View all Pokemon")
    print("4. Change current player")
    print("5. Quit game")
    print()

    print("--------------------------------------------------------------------------------\n")


while True:  # loop that continuously runs the game when the program starts

    if quit_game == 'yes':   # breaks loop and closes program
        break
    current_player_list = []
    current_player_CP_list = []
    current_player_type_list = []
    if player_change != 'yes':  # asks for player name inputs
        player_1 = input('Enter the name of player 1: ')
        player_2 = input('Enter the name of player 2: ')
    player_selection = input(f'Enter 1 to play as {player_1}, or enter 2 to play as {player_2}: ')
    print()
    if player_selection == '1':
        player = player_1
    elif player_selection == '2':
        player = player_2
    else:
        player = player_1
        print(f'Invalid input, {player_1} selected by default.')

    print('Current player:', player)

    candy_count = 0  # global variable to store total candies collected by a player
    current_player_list = []  # sets up the pokemon list

    generate_new_pokemon()  # called in order to give the player a starting pokemon

    while True:  # loop that runs as long as the selected player does not change
        main_menu()  # calls main menu and asks for input on which action to take
        menu_select = int(input('Please select what action you would like to take (1, 2, 3, 4, 5): '))
        print()
        if menu_select == 1:  # view current pokemon
            current_pokemon_menu(candy_count)
        elif menu_select == 2:  # get new pokemon
            candy_count += generate_new_pokemon()  # updates total number of candies
        elif menu_select == 3:  # view all pokemon
            pokemon_selection_menu(candy_count, current_player_list)
            new_current = int(input("If you would like to change your current pokemon, enter the number of that pokemon exactly as it appears.\nOtherwise, enter 1: "))
            if new_current != '':
                current_player_list.insert(0, current_player_list.pop(new_current - 1))
                current_player_CP_list.insert(0, current_player_CP_list.pop(new_current - 1))
                current_player_type_list.insert(0, current_player_type_list.pop(new_current - 1))
        elif menu_select == 4:  # change current player
            player_change = 'yes'
            break
        elif menu_select == 5:  # quit game
            quit_game = 'yes'
            break

pokemon_file.close()

