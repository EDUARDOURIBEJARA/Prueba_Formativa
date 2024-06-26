import os
import time

def limpiar_pantalla():
    # Limpiar la pantalla
    os.system('cls')

def registrar_trabajador(trabajadores):
    nombre = input("Ingrese Nombre y Apellido: ")
    cargo = input("Ingrese Cargo (CEO, Desarrollador, Analista de datos): ")
    while True:
        try:
            sueldo_bruto = float(input("Ingrese Sueldo Bruto: "))
            break
        except ValueError:
            print("Por favor, ingrese un valor numérico válido para el sueldo bruto.")
    
    descuento_salud = 0
    descuento_afp = 0
    sueldo_liquido = 0

    if cargo == "CEO":
        descuento_salud = 70000
        descuento_afp = 120000
    elif cargo == "Desarrollador":
        descuento_salud = 50000
        descuento_afp = 100000
    elif cargo == "Analista de datos":
        descuento_salud = 60000
        descuento_afp = 110000
    else:
        descuento_salud = sueldo_bruto * 0.07
        descuento_afp = sueldo_bruto * 0.12

    sueldo_liquido = sueldo_bruto - descuento_salud - descuento_afp
    
    trabajador = {
        "nombre": nombre,
        "cargo": cargo,
        "sueldo_bruto": sueldo_bruto,
        "descuento_salud": descuento_salud,
        "descuento_afp": descuento_afp,
        "sueldo_liquido": sueldo_liquido
    }
    
    trabajadores.append(trabajador)
    print("Trabajador registrado con éxito.\n")

def listar_trabajadores(trabajadores):
    print("Lista de Trabajadores:\n")
    for trabajador in trabajadores:
        print(f"Nombre: {trabajador['nombre']}, Cargo: {trabajador['cargo']}, Sueldo Bruto: {trabajador['sueldo_bruto']}, Desc. Salud: {trabajador['descuento_salud']}, Desc. AFP: {trabajador['descuento_afp']}, Líquido a pagar: {trabajador['sueldo_liquido']}\n")

def imprimir_planilla(trabajadores):
    opcion = input("¿Desea imprimir todos los trabajadores o por cargo específico? (todos/cargo): ")
    if opcion == "cargo":
        cargo = input("Ingrese el cargo (CEO, Desarrollador, Analista de datos): ")
        trabajadores_a_imprimir = [trabajador for trabajador in trabajadores if trabajador['cargo'] == cargo]
    else:
        trabajadores_a_imprimir = trabajadores

    with open(f"planilla_{opcion}.txt", "w") as archivo:
        for trabajador in trabajadores_a_imprimir:
            archivo.write(f"Nombre: {trabajador['nombre']}, Cargo: {trabajador['cargo']}, Sueldo Bruto: {trabajador['sueldo_bruto']}, Desc. Salud: {trabajador['descuento_salud']}, Desc. AFP: {trabajador['descuento_afp']}, Líquido a pagar: {trabajador['sueldo_liquido']}\n")
    print(f"Planilla guardada en 'planilla_{opcion}.txt'\n")

trabajadores = []

while True:
    limpiar_pantalla()
    print("1. Registrar trabajador")
    print("2. Listar todos los trabajadores")
    print("3. Imprimir planilla de sueldos")
    print("4. Salir del programa")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_trabajador(trabajadores)
    elif opcion == "2":
        listar_trabajadores(trabajadores)
    elif opcion == "3":
        imprimir_planilla(trabajadores)
    elif opcion == "4":
        print("Saliendo del programa.")
        time.sleep(1)
        break
    else:
        print("Opción no válida, intente de nuevo.\n")
        time.sleep(1)

