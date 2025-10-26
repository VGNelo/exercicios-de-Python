from time import sleep

def regressiva(numero):
    while numero > 0:
        print(numero)
        sleep(1)
        numero -= 1

    if numero == 0:
        print('BOOOMMM')

# Chamada da função fora da definição
regressiva(10)
