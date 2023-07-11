import os
from Codi111 import buy_apartment, show_available_apartments, show_list_of_buyers, show_total_sales

op=0
matriz=[[],[],[],[]]

while True:
    os.system("cls")
    print("1. Comprar departamento")
    print("2. Mostrar departamentos disponibles")
    print("3. Ver listado de compradores")
    print("4. Mostar ganancias totales")
    print("5. Salir ")
    while True:
        try:
            op=int(input("ingresa una opcion 1-5: "))
            if op <1 or op > 5:
                print("ERROR,ingresa la opcion valida ya dicha")
            else:
                break
        except ValueError:
            print
            ("ERROR, intentar nuevamente ")
    if op == 1:
        buy_apartment(matriz)
    elif op == 2:
        show_available_apartments(matriz)
    elif op == 3:
        show_list_of_buyers(matriz)
    elif op == 4:
        show_total_sales(matriz)
    elif op == 5:
        break




