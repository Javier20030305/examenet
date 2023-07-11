import os
import datetime

apartamento = []
for floor in range(1, 11):
    matrix = []
    for type in ["A", "B", "C", "D"]:
        matrix.append(1 if (floor, type) in apartamento else 0)
    apartamento.append(matrix)

precio = {"A": 3800, "B": 3000, "C": 2800, "D": 3500}

buyers = []

def validate_menu_option(option):
    if option < 1 or option > 5:
        print("Invalid menu option.")
        return False
    return True

def buy_apartment():
    floor = int(input("Enter the floor: "))
    type = input("ingrese su tipo de departamento : ")

    if apartamento[floor - 1][type] == 0:
        print("el departamento elejido no es valido .")
        return

    apartamento[floor - 1][type] = 0
    buyers.append((floor, type))

    print("El apartamento se ha vendido con éxito.")

def show_available_apartments():
    print("The available apartments are:")
    for floor in range(1, 11):
        for type in ["A", "B", "C", "D"]:
            if apartamento[floor - 1][type] == 1:
                print(f"{floor}-{type}")

def show_list_of_buyers():
    print("The list of buyers is:")
    for buyer in buyers:
        print(f"RUN: {buyer[2]}, Floor: {buyer[0]}, Type: {buyer[1]}")

def show_total_sales():
    total_sales = 0
    for apartment in buyers:
        total_sales += precio[apartment[1]]

    print(f"El precio total es de : {total_sales}")

def exit_system():
    print(f"System exit by {__author__} on {datetime.datetime.today()}")
    exit()

