from random import shuffle
from lib.definiciones import *

shuffle(eventos)
while negras != 1000 and 0 < sum(campo) < 1000:
    while len(mano) < 5 and eventos: mano += [ eventos.pop() ]

    for _ in range(100): print("")
    print(f"Ovejas negras: {negras}.")
    print(f"Cartas de eventos: {len(eventos)}.")
    print(f"Elementos del campo: {len(campo)}.")
    print(f"Campo: {campo} (total: {sum(campo)}).\n")
    for i, carta in enumerate(mano): print(f"{i + 1}: {carta}")
    elegida = mano.pop(int(input("\nIngrese una carta: ")) - 1)
    for _ in range(100): print("")
    print(f"Campo: {campo} (total: {sum(campo)}).\n")
    for i, carta in enumerate(mano): print(f"{i + 1}: {carta}")
    print("")

    if elegida == allPurposeSheep and mano:
        descarte += [ elegida ]
        elegida = mano[ int(input("Elija una carta a imitar: ")) - 1 ]
    if elegida == crowding and len(campo) > 2:
        campo  = [ int(input("Ingrese ovejas a conservar: ")) ]
        campo += [ int(input("Ingrese mas ovejas a conservar: ")) ]
    elif elegida == fallingRock and campo:
        campo.remove(int(input("Ingrese ovejas a retirar del campo: ")))
    elif elegida == fillTheEarth and len(campo) < 7:
        cantidad = input("Ingrese cantidad de ovejas a agregar: ")
        campo += [1] * (int(cantidad) if cantidad else 7)
    elif elegida == flourish and 0 < len(campo) < 7:
        cantidad = int(input("Ingrese cantidad de ovejas: "))
        cantidad = (cantidad // 10) * 3 if cantidad % 3 else cantidad // 3
        if cantidad: campo += [ cantidad ] * 3
    elif elegida == goldenHooves:
        for i, ovejas in enumerate(campo):
            if ovejas != max(campo):
                if input(f"Desea incrementar {ovejas} ovejas? (S/N): ") != "N":
                    campo[i] = ovejas*3 if ovejas % 3 else (ovejas//3) * 10
    elif elegida == inspiration and eventos:
        for i, carta in enumerate(eventos): print(f"{i + 1}: {carta}")
        mano += [ eventos.pop(int(input("\nAgregue una carta: ")) - 1) ]
        shuffle(eventos)
    elif elegida == lightning and campo:
        campo.remove(max(campo))
    elif elegida == meteor and campo:
        campo.remove(int(input("Elimine ovejas: ")))
        if campo: campo.remove(int(input("Elimine mas ovejas: ")))
        if campo: campo.remove(int(input("Elimine aun mas ovejas: ")))
    elif elegida == multiply and len(campo) < 7:
        campo += [3]
    elif elegida == plague and campo:
        cantidad = int(input("Ingrese cantidad de ovejas: "))
        while cantidad in campo: campo.remove(cantidad)
    elif elegida == planningSheep and mano:
        mano.pop(int(input("Elimine una carta: ")) - 1)
    elif elegida == sheepDog and mano:
        descarte += [ mano.pop(int(input("Descarte una carta: ")) - 1) ]
    elif elegida == shephion:
        campo = []
    elif elegida == slump and campo:
        cantidad = len(campo) // 2
        for _ in range(cantidad):
            campo.remove(int(input("Ingrese ovejas a eliminar: ")))
    elif elegida == storm and campo:
        campo.remove(int(input("Ingrese ovejas a eliminar: ")))
        if campo: campo.remove(int(input("Ingrese mas ovejas a eliminar: ")))
    elif elegida == wolves and campo:
        maximo = max(campo)
        if maximo != 1:
            campo += [ (maximo // 10) * 3 if maximo % 3 else maximo // 3 ]
        campo.remove(maximo)
    elif elegida == beFruitful and 0 < len(campo) < 7:
        campo += [ int(input("Ingrese cantidad de ovejas: ")) ]
    elif elegida == dominion and campo:
        total = 0
        for ovejas in campo[:]:
            if input(f"Desea sumar {ovejas} ovejas? (S/N): ") != "N":
                total += ovejas
                campo.remove(ovejas)

        ovejas = int(input("Cuantas ovejas desea agregar: "))
        if 0 < ovejas <= total: campo += [ ovejas ]

    campo = campo[:7]
    if elegida not in descarte and elegida != meteor:
        descarte += [ elegida ]

    if not mano:
        negras *= 10
        eventos = descarte[:]
        shuffle(eventos)
        descarte = []

print(f"\nOvejas negras: {negras}.")
print(f"Ovejas blancas: {sum(campo)}.")
print("Ganaste!" if sum(campo) >= negras else "Perdiste!")
