from os import name, system
from variables import *

# define global variables
inventory = {
    "health": 10,
    "money": 10,
    "social": 10,
    "fame": 10,
}

scenarios = [
    scenario01,
    scenario02,
    scenario03,
    scenario04,
    scenario05,
    scenario06,
    scenario07,
    scenario08,
]


def clear_console(): system('cls' if name == 'nt'else'clear')


def choose():
    decision = 'null'

    while(decision != 'false' and decision != 'true'):
        decision = input((f'\n\tVocê aceita (true) ou recusa (false)? '))
        decision = decision.lower().strip()

        if decision == 'true':
            return True
        elif decision == 'false':
            return False
        else:
            print('\n\t⚠️ Por favor, digite apenas "true" ou "false" ⚠️\n')


def showMenu():
    print("""\n
      *********************
      ** DEVELOPER, INC. **
      *********************
      ---------------------
      | 0 - Iniciar jogo  |
      | 1 - Créditos      |
      | 2 - Sair          |
      ---------------------
    \n""")


def is_player_alive(inventory):
    flag = True

    for item_value in inventory.values():
        if item_value <= 0:
            flag = False

    return flag


def show_inventory():
    global inventory

    print(f"""\n
        STATUS ATUAL:

        Saúde: {inventory['health']}
        Dinheiro: {inventory['money']}
        Vida social: {inventory['social']}
        Fama: {inventory['fame']}
    """)


def start_game():
    global scenarios
    global inventory

    reset_inventory(inventory)

    for scenario in scenarios:
        if is_player_alive(inventory) == False:
            game_over()
            break

        print(scenario)
        boolean_answer = choose()

        if scenario == scenario01:
            if boolean_answer:
                inventory['health'] -= 2
                inventory['money'] += 2
                inventory['social'] -= 3
                inventory['fame'] += 1
            else:
                inventory['health'] += 1
                inventory['money'] -= 4
                inventory['social'] += 1
                inventory['fame'] -= 1

            clear_console()
            show_inventory()

        elif scenario == scenario02:
            if boolean_answer:
                inventory['health'] += 2
                inventory['money'] -= 4
                inventory['social'] -= 0
                inventory['fame'] += 2
            else:
                inventory['health'] -= 2
                inventory['money'] += 4
                inventory['social'] += 0
                inventory['fame'] -= 2

            clear_console()
            show_inventory()

        elif scenario == scenario03:
            if boolean_answer:
                inventory['health'] += 1
                inventory['money'] -= 5
                inventory['social'] += 2
                inventory['fame'] += 2
            else:
                inventory['health'] -= 3
                inventory['money'] += 4
                inventory['social'] -= 4
                inventory['fame'] -= 3

            clear_console()
            show_inventory()

        elif scenario == scenario04:
            if boolean_answer:
                inventory['health'] -= 9
                inventory['money'] -= 6
                inventory['social'] += 8
                inventory['fame'] += 5
            else:
                inventory['health'] += 4
                inventory['money'] += 8
                inventory['social'] -= 4
                inventory['fame'] -= 3

            clear_console()
            show_inventory()

        elif scenario == scenario05:
            if boolean_answer:
                inventory['health'] += 9
                inventory['money'] -= 8
                inventory['social'] -= 0
                inventory['fame'] += 0
            else:
                inventory['health'] -= 9
                inventory['money'] += 8
                inventory['social'] += 0
                inventory['fame'] -= 0

            clear_console()
            show_inventory()

        elif scenario == scenario06:
            if boolean_answer:
                inventory['health'] += 5
                inventory['money'] += 2
                inventory['social'] += 8
                inventory['fame'] -= 8
            else:
                inventory['health'] -= 3
                inventory['money'] -= 2
                inventory['social'] -= 4
                inventory['fame'] += 3

            clear_console()
            show_inventory()

        elif scenario == scenario07:
            if boolean_answer:
                inventory['health'] -= 10
                inventory['money'] += 8
                inventory['social'] -= 11
                inventory['fame'] += 10
            else:
                inventory['health'] += 5
                inventory['money'] -= 7
                inventory['social'] += 2
                inventory['fame'] -= 5

            clear_console()
            show_inventory()

        elif scenario == scenario08:
            if boolean_answer:
                inventory['health'] -= 2
                inventory['money'] -= 10
                inventory['social'] -= 3
                inventory['fame'] += 5
            else:
                inventory['health'] += 1
                inventory['money'] += 4
                inventory['social'] += 1
                inventory['fame'] -= 8

            clear_console()
            show_inventory()

        # clear_console()
        pass

    clear_console()
    end_game()


def reset_inventory(inventory):
    for item in inventory.values():
        item = 10


def main():
    while True:
        showMenu()
        menu_option = input("\n\tEscolha uma opção: ")

        if menu_option == '0':
            clear_console()
            presentation()
            clear_console()
            start_game()
        elif menu_option == '1':
            clear_console()
            show_credits()
        elif menu_option == '2':
            clear_console()
            bye()
            break
        else:
            print('\n\tFavor inserir uma opção válida!\n')


if __name__ == "__main__":
    main()
