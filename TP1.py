estudiantes = [    {"nombre": "Juan",  "apellido": "Funes", "edad": 12, "especialidad":"informatica" },
    {"nombre": "Ana",  "apellido": "Dorrego", "edad": 66, "especialidad":"electronica" },
    {"nombre": "Pedro",  "apellido": "Delgado", "edad": 14, "especialidad":"electronica" },
    {"nombre": "Laura",  "apellido": "Erdocia", "edad": 51, "especialidad":"informatica" },
    {"nombre": "Carlos",  "apellido": "Vaca", "edad": 33, "especialidad":"construcciones" },
    {"nombre": "Lucía",  "apellido": "Pons Lara", "edad": 18, "especialidad":"informatica" },
    {"nombre": "Marta",  "apellido": "Vergamota", "edad": 40, "especialidad":"construcciones" },
    {"nombre": "Luis",  "apellido": "Gonzales", "edad": 24, "especialidad":"electronica" },
    {"nombre": "Zimba", "apellido": "Torooo", "edad": 34, "especialidad":"informatica" },
    {"nombre": "Federico", "apellido": "Savedra", "edad": 10, "especialidad":"construcciones" },
]
# Función para mostrar los estudiantes
def mostrar_estudiantes():
    for i, estudiante in enumerate(estudiantes):
        print(f"{i + 1}. {estudiante['nombre']} {estudiante['apellido']} - Edad: {estudiante['edad']}, Especialidad: {estudiante['especialidad']}")

# Función para actualizar los datos de un estudiante
def actualizar_estudiante(indice):
    if indice < 0 or indice >= len(estudiantes):
        print("El índice del estudiante no es válido.")
        return

    estudiante = estudiantes[indice]
    print(f"Actualizando a {estudiante['nombre']} {estudiante['apellido']}")

    nuevo_nombre = input(f"Nuevo nombre (actual: {estudiante['nombre']}): ") or estudiante['nombre']
    nueva_edad = input(f"Nueva edad (actual: {estudiante['edad']}): ") or estudiante['edad']
    nueva_especialidad = input(f"Nueva especialidad (actual: {estudiante['especialidad']}): ") or estudiante['especialidad']

    # Actualizar el estudiante con los nuevos datos
    estudiante['nombre'] = nuevo_nombre
    estudiante['edad'] = int(nueva_edad)  # Convertir a entero la edad
    estudiante['especialidad'] = nueva_especialidad

    print("Estudiante actualizado correctamente.")

# Función para eliminar un estudiante
def eliminar_estudiante(indice):
    if indice < 0 or indice >= len(estudiantes):
        print("El índice del estudiante no es válido.")
        return
    
    eliminado = estudiantes.pop(indice)
    print(f"El estudiante {eliminado['nombre']} {eliminado['apellido']} ha sido eliminado.")

# Menú para gestionar la lista de estudiantes
def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Mostrar estudiantes")
        print("2. Actualizar estudiante")
        print("3. Eliminar estudiante")
        print("4. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            mostrar_estudiantes()
        elif opcion == "2":
            mostrar_estudiantes()
            indice = int(input("Introduce el número del estudiante a actualizar: ")) - 1
            actualizar_estudiante(indice)
        elif opcion == "3":
            mostrar_estudiantes()
            indice = int(input("Introduce el número del estudiante a eliminar: ")) - 1
            eliminar_estudiante(indice)
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecución del menú
menu()