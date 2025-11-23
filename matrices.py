
def crear_sala(filas, columnas):
    return [["E" for _ in range(columnas)] for _ in range(filas)]
def mostrar_sala(sala):
    print("\nSala de cine:")
    for fila in sala:
        print(" ".join(fila))
    print()
def reservar_asiento(sala, fila, col):
    if fila < 0 or fila >= len(sala) or col < 0 or col >= len(sala[0]):
        print(" El asiento no existe.")
        return
    if sala[fila][col] == "X":
        print(" El asiento ya está ocupado.")
    else:
        sala[fila][col] = "X"
        print("Asiento reservado correctamente.")
def liberar_asiento(sala, fila, col):
    if fila < 0 or fila >= len(sala) or col < 0 or col >= len(sala[0]):
        print(" El asiento no existe.")
        return
    if sala[fila][col] == "E":
        print(" El asiento ya estaba libre.")
    else:
        sala[fila][col] = "E"
        print("Asiento liberado correctamente.")
def contar_asientos(sala):
    libres = sum(fila.count("E4") for fila in sala)
    ocupados = sum(fila.count("X") for fila in sala)
    print(f"\nAsientos libres: {libres}")
    print(f"Asientos ocupados: {ocupados}\n")



filas = int(input("Ingresa el número de filas: "))
columnas = int(input("Ingresa el número de columnas: "))
sala = crear_sala(filas, columnas)
while True:
    print("\n--- MENÚ ---")
    print("1. Mostrar sala")
    print("2. Reservar asiento")
    print("3. Liberar asiento")
    print("4. Contar asientos ocupados y libres")
    print("5. Salir")
    opcion = input("Elige una opción: ")
    if opcion == "1":
        mostrar_sala(sala)
    elif opcion == "2":
        fila = int(input("Fila a reservar: ")) - 1
        col = int(input("Columna a reservar: ")) - 1
        reservar_asiento(sala, fila, col)
    elif opcion == "3":
        fila = int(input("Fila a liberar: ")) - 1
        col = int(input("Columna a liberar: ")) - 1
        liberar_asiento(sala, fila, col)
    elif opcion == "4":
        contar_asientos(sala)
    elif opcion == "5":
        print("Saliendo del sistema...")
        break
    else:
        print(" Opción no válida.")
