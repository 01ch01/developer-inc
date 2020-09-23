from os import name, system
from random import randint, sample

# define global variables
inventory = {
    "health": 10,
    "money": 10,
    "social": 10,
    "fame": 10,
}

scenario01 = """\n
    Você recebeu uma proposta para dar manutenção num sistema de
    supermercado que existe há mais de 10 anos e ninguém nunca mexeu,
    pois "não se mexe em time que está ganhando."
"""

scenario02 = """\n
    Abrir um MEI para formalizar seus serviços, considerando os
    impostos a serem pagos.
"""


scenario03 = """\n
    Comprar um MacBook para aumentar drasticamente a produtividade
    (e diminuir drasticamente no bolso, consequentemente).
"""


scenario04 = """\n
    Ir naquela festa f0d@ da faculdade que só acontece uma vez por ano,
    sabendo que precisa entregar um relatório mega importante pro
    seu principal cliente amanhã, e você nem começou a fazer ainda.
"""


scenario05 = """\n
    Ir ao médico urgentemente numa quarta-feira porque você está com
    muita ansiedade e estresse acumulados.
"""


scenario06 = """\n
    Ir almoçar na casa dos seus pais no final de semana.
"""


scenario07 = """\n
    Neste período da faculdade você tem 8 disciplinas, e surgiu uma
    oportunidade de trabalho remoto.
"""


scenario08 = """\n
    Seu PC queimou e você precisa terminar e entregar um site ainda hoje.
    Sua única salvação é comprar um notebook usado que custa os olhos da cara.
"""

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


def clear_console():
    if name == 'posix':
        system('clear')
    elif name == 'nt':
        system('cls')
    else:
        pass


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
            # clear_console()
            print('\n\t⚠️ Por favor, digite apenas "true" ou "false" ⚠️\n')


def presentation():
    clear_console()
    print("""\n
      Olá! Boas-vindas ao Developer, Inc., o jogo aonde você
      exerce a função de uma pessoa desenvolvedora de software!
      Você estará à mercê de vários desafios que fazem parte do
      cotidiano de alguém que trabalha nesse ramo. O jogo consiste
      em situações em que você deverá decidir se aceita ou não (true ou false),
      e sua resposta ditará o próximo desafio, até o final do game.

      Você terá 4 itens em sua mochila:
      Saúde, Dinheiro, Vida Social e Fama, começando tudo com 10.

      O propósito final é chegar no fim do game com
      NENHUM ITEM ZERADO EM SUA MOCHILA.

      Bom jogo, e que a sorte esteja sempre a seu favor! ❤️

  """)

    input('> Aperte qualquer tecla para continuar...')
    clear_console()


def showMenu():
    print("""\n
      ********************
      ** DEVELOPER, INC. **
      ********************
      --------------------
      | 0 - Iniciar Jogo |
      | 1 - Créditos     |
      | 2 - Sair         |
      --------------------
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


def game_over():
    print("""
        ************************    GAME OVER 👾    ************************
         Infelizmente, você não conseguiu sobreviver até o final da jornada.
            Mas não se preocupe, nunca é um fim, e sempre um recomeço!
        ********************************************************************
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


def show_credits():
    print(f"""\n
        {'*'*48}
            Desenvolvido com ❤️ por Cláudio Henrique
        {'*'*48}
    """)


def end_game():
    print(f"""
    {'*'*28} 💥 VOCÊ CONSEGUIU!! 💥 {'*'*28}
    Meus parabéns, não é tão fácil conciliar todos esses pontos, não é mesmo? hahaha
    \t\tEspero que tenha gostado dessa pequena simulação! ^-^
    {'*'*80}
    """)


def bye():
    print("""\n
        Até mais tarde! 👋
    """)


def reset_inventory(inventory):
    for item in inventory.values():
        item = 10


def main():
    while True:
        showMenu()
        menu_option = input("\n\tEscolha uma opção: ")

        if menu_option == '0':
            presentation()
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
