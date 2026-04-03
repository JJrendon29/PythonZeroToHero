tareas = []

def agregar_tareas(string_tarea):
    tareas.append(string_tarea)
    print("Tarea agregada")

    return tareas

def eliminar_tareas(number_tarea):
    tareas.pop(number_tarea)
    print("Tarea eliminada")

    return tareas

def mostrar_tareas(tareas):
    print(tareas)

    return tareas

while True:
    print("Estas son las tareas que puedes hacer: \n Opcion 1: Agregar tarea \n Opcion 2: Mostrar y eliminar tarea " \
    "\n Opcion 3: Mostrar tarea/s  \n Opcion 4: Cerrar programa")

    opcion = int(input("Inserte un numero: "))

    if opcion == 1:
        string_tarea = input("Escriba la tarea que desea agregar: ")
        agregar_tareas(string_tarea)

    elif opcion == 2:
        mostrar_tareas(tareas)
        number_tarea = int(input(f"Escriba el numero de la tarea que desea eliminar (inicia en 0 la lista)"))
        eliminar_tareas(number_tarea)

    elif opcion == 3:
        mostrar_tareas(tareas)

    elif opcion == 4:
        break
    
    else:
        print("Inserte un numero valido")