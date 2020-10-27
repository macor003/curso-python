def conversor(tipo_moneda, valor_dolar):
    pesos = float(input('Cuantos pesos ' + tipo_moneda + ' tienes?: '))
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $' + dolares + ' Dolares')


menu = """
Bienvenido al conversor de monedas

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opcion (numero): """

opcion = int(input(menu))

if opcion == 1:
    conversor('Colombianos', 3870)
elif opcion == 2:
    conversor('Argentinos', 65)
elif opcion == 3:
    conversor('Mexicanos', 25)
else:
    print('Ingresa una opcion correcta por favor')
