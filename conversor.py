menu = """
Bienvenido al conversor de monedas

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opcion (numero): """

opcion = int(input(menu))

if opcion == 1:
    pesos = float(input('Cuantos pesos Colombianos tienes?: '))
    valor_dolar = 3875
    dolares = pesos/valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $' + dolares + ' Dolares')
elif opcion == 2:
    pesos = float(input('Cuantos pesos Argentinos tienes?: '))
    valor_dolar = 65
    dolares = pesos/valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $' + dolares + ' Dolares')

elif opcion == 3:
    pesos = float(input('Cuantos pesos Mexicanos tienes?: '))
    valor_dolar = 20
    dolares = pesos/valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $' + dolares + ' Dolares')
else:
    print('Ingresa una opcion correcta por favor')
