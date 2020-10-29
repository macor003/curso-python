import random


def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input('Elige un numero del 1 al 100: '))
    vidas = 5
    while numero_aleatorio != numero_elegido:
        if numero_aleatorio < numero_elegido:
            print("Elige un numero mas pequeño.")
            vidas -= 1
        elif numero_aleatorio > numero_elegido:
            print("Elige un numero mas grande.")
            vidas -= 1
        if vidas == 0:
            print("GAME OVER :'(")
            break
        print("Tienes", vidas, "vidas")
        numero_elegido = int(input("Introduce otro numero: "))
    if numero_aleatorio == numero_elegido:
        print("¡FELICIDADES GANASTE!")


if __name__ == '__main__':
    run()
