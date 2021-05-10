def conversor(tipo_moneda, valor_dolar):
    pesos = input("¿Cuantos " + tipo_moneda + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares= round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")

menu = """
¡Bienvenida al conversor de monedas! 💎💎

1 - Pesos Colombianos
2 - Euro
3 - Pesos Argentinos

Elige una opción: """

opcion = int(input(menu))
if opcion == 1:
    conversor("pesos colombianos", 3875)

elif opcion == 2:
    conversor("euros", 1.19)

elif opcion == 3:
    conversor("pesos argentinos", 0.013)

else:
    print("Ingresa una opcion correcta")


