
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


def presentation():
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


def game_over():
    print("""
        ************************    GAME OVER 👾    ************************
         Infelizmente, você não conseguiu sobreviver até o final da jornada.
            Mas não se preocupe, nunca é um fim, é sempre um recomeço!
        ********************************************************************
    """)


def show_credits():
    print(f"""\n
        {'*'*48}
            Desenvolvido com ❤️  por Cláudio Henrique
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
