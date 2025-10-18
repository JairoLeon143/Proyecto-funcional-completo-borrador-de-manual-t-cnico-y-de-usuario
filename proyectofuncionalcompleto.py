# ===============================
# GESTOR DE NOTAS ACADÉMICAS
# ===============================

# Listas principales
nombres = []
notas = []
historial_cambios = []  # pila de cambios

# 1. Registrar nuevo curso
# no permiete agregar un curso, el que se desea registrar
def registrar_curso():
    nombre = input("Ingresar nombre del curso: ").strip()
    if nombre in nombres:
        print("Este curso ya se ha registrado.")
        return
    try:
        nota = float(input("Ingrese la nota obtenida (0-100): "))
        if 0 <= nota <= 100:
            nombres.append(nombre)
            notas.append(nota)
            historial_cambios.append(f"Se registró el curso '{nombre}' con nota {nota}.")
            print("El curso se registró con éxito.")
        else:
            print("La nota debe estar entre 0 y 100.")
    except ValueError:
        print("Ingrese un valor numérico válido.")

# 2. Mostrar cursos registrados
# Si no hay cursos, lo indica. Si existen, los recorre con un bucle for.
def mostrar_cursos():
    if not nombres:
        print("No hay cursos registrados.")
    else:
        print("\nCursos registrados:")
        for i in range(len(nombres)):
            print(f"{i+1}. {nombres[i]} - Nota: {notas[i]}")

# 3. Calcular promedio general
# Suma todas las notas y las divide entre la cantidad de cursos.
# Usa f-string con formato .2f para mostrar 2 decimales.

def calcular_promedio():
    if not notas:
        print("No se han registrado cursos.")
    else:
        promedio = sum(notas) / len(notas)
        print(f"Promedio general: {promedio:.2f}")

# 4. Contar cursos aprobados y reprobados
# Considera aprobado si la nota >= 60.
# Usa un bucle for y condicionales if-else.

def contar_aprobados_reprobados():
    if not notas:
        print("No se han registrado cursos.")
    else:
        aprobados = sum(1 for n in notas if n >= 60)
        reprobados = len(notas) - aprobados
        print(f"Cursos aprobados: {aprobados}")
        print(f"Cursos reprobados: {reprobados}")

# 5. Búsqueda lineal de curso
# Solicita el nombre del curso, convierte a minúsculas y busca coincidencias parciales.
# Si lo encuentra, lo muestra. Si no, informa que no existe.
def buscar_curso_lineal():
    nombre = input("Ingrese el nombre del curso: ").strip().lower()
    for i in range(len(nombres)):
        if nombre in nombres[i].lower():
            print(f"Curso encontrado: {nombres[i]} - Nota: {notas[i]}")
            return
    print("Curso no encontrado.")

# 6. Actualizar nota de un curso
# Solicita el nombre del curso y una nueva nota (validada entre 0 y 100).
# # Si lo encuentra, reemplaza la nota en la lista.

def actualizar_nota():
    nombre = input("Ingrese el nombre del curso: ").strip()
    if nombre in nombres:
        try:
            nueva_nota = float(input("Ingrese la nueva nota (0-100): "))
            if 0 <= nueva_nota <= 100:
                indice = nombres.index(nombre)
                notas[indice] = nueva_nota
                historial_cambios.append(f"Se actualizó la nota de '{nombre}' a {nueva_nota}.")
                print("Nota actualizada correctamente.")
            else:
                print("La nota debe estar entre 0 y 100.")
        except ValueError:
            print("Ingrese un dato numérico válido.")
    else:
        print("No se ha podido encontrar el curso.")

# 7. Eliminar un curso
# Solicita el nombre del curso.
# Pide confirmación antes de eliminar.
# Elimina el curso si se confirma.
def eliminar_curso():
    if not nombres:
        print("No hay cursos registrados.")
        return
    
    curso = input("Ingrese el curso a eliminar: ").strip()
    if curso in nombres:
        confirmacion = input(f"¿Está seguro que desea eliminar '{curso}'? (s/n): ").strip().lower()
        if confirmacion == "s":
            indice = nombres.index(curso)
            nombres.pop(indice)
            notas.pop(indice)
            historial_cambios.append(f"Se eliminó el curso '{curso}'.")
            print("Curso eliminado correctamente.")
        else:
            print("Operación cancelada.")
    else:
        print("El curso no existe en la lista.")

# 8. Ordenar cursos por nota (burbuja)
# Ordena los cursos en orden descendente según las notas.
# Usa el método de ordenamiento burbuja.
def ordenar_por_nota():
    n = len(notas)
    for i in range(n):
        for j in range(0, n - i - 1):
            if notas[j] < notas[j + 1]:  # de mayor a menor
                notas[j], notas[j + 1] = notas[j + 1], notas[j]
                nombres[j], nombres[j + 1] = nombres[j + 1], nombres[j]
    print("\nCursos ordenados por nota (de mayor a menor):")
    mostrar_cursos()

# 9. Ordenar cursos por nombre (inserción)
# Ordena los cursos alfabéticamente aplicando el método de inserción.
def ordenar_por_nombre():
    for i in range(1, len(nombres)):
        key_nombre = nombres[i]
        key_nota = notas[i]
        j = i - 1
        while j >= 0 and nombres[j].lower() > key_nombre.lower():
            nombres[j + 1] = nombres[j]
            notas[j + 1] = notas[j]
            j -= 1
        nombres[j + 1] = key_nombre
        notas[j + 1] = key_nota
    print("\nCursos ordenados alfabéticamente:")
    mostrar_cursos()

# 10. Búsqueda binaria por nombre
# Solo se puede usar si los cursos están ordenados por nombre.
# Busca el curso más rápido dividiendo la lista a la mitad cada vez.
def buscar_curso_binario():
    if not nombres:
        print("No hay cursos registrados.")
        return

    if nombres != sorted(nombres, key=lambda x: x.lower()):
        print("Primero debe ordenar los cursos por nombre antes de usar la búsqueda binaria.")
        return

    nombre_buscar = input("Ingrese el nombre del curso a buscar: ").strip().lower()
    inicio, fin = 0, len(nombres) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if nombres[medio].lower() == nombre_buscar:
            print(f"Curso encontrado: {nombres[medio]} - Nota: {notas[medio]}")
            return
        elif nombres[medio].lower() < nombre_buscar:
            inicio = medio + 1
        else:
            fin = medio - 1
    print("Curso no encontrado.")

# 11. Simular cola de revisión
# Aquí se simula una cola de cursos que van a revisión.
# El usuario ingresa varios cursos y al final se muestran en el mismo orden.
def simular_cola_revision():
    cola = []
    print("Ingrese curso para revisión (escriba 'fin' para terminar):")
    while True:
        curso = input("> ").strip()
        if curso.lower() == "fin":
            break
        cola.append(curso)

    print("\nProcesando solicitudes:")
    for curso in cola:
        print(f"Revisando: {curso}")

# 12. Mostrar historial de cambios (pila)
# Muestra los últimos cambios realizados (actualizaciones o eliminaciones)
# en orden inverso, como una pila.
def mostrar_historial():
    if not historial_cambios:
        print("No hay cambios registrados aún.")
    else:
        print("\nHistorial de cambios recientes:")
        for i, cambio in enumerate(reversed(historial_cambios), 1):
            print(f"{i}. {cambio}")

# 13. Salir
# Termina el programa mostrando un mensaje de despedida.
def salir():
    print("\nGracias por usar el Gestor de Notas Académicas. ¡Hasta pronto!")
    exit()

###MENU PRINCIPAL.
#En este menu de opciones, nos permite seleccionar la opcion que deseamos que el programa realice y ejecute. 
def menu():
    while True:
        print("\n====== GESTOR DE NOTAS ACADÉMICAS ======")
        print("1. Registrar nuevo curso")
        print("2. Mostrar todos los cursos y notas")
        print("3. Calcular promedio general")
        print("4. Contar cursos aprobados y reprobados")
        print("5. Buscar curso por nombre (búsqueda lineal)")
        print("6. Actualizar nota de un curso")
        print("7. Eliminar un curso")
        print("8. Ordenar cursos por nota (ordenamiento burbuja)")
        print("9. Ordenar cursos por nombre (ordenamiento inserción)")
        print("10. Buscar curso por nombre (búsqueda binaria)")
        print("11. Simular cola de solicitudes de revisión")
        print("12. Mostrar historial de cambios (pila)")
        print("13. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_curso()
        elif opcion == "2":
            mostrar_cursos()
        elif opcion == "3":
            calcular_promedio()
        elif opcion == "4":
            contar_aprobados_reprobados()
        elif opcion == "5":
            buscar_curso_lineal()
        elif opcion == "6":
            actualizar_nota()
        elif opcion == "7":
            eliminar_curso()
        elif opcion == "8":
            ordenar_por_nota()
        elif opcion == "9":
            ordenar_por_nombre()
        elif opcion == "10":
            buscar_curso_binario()
        elif opcion == "11":
            simular_cola_revision()
        elif opcion == "12":
            mostrar_historial()
        elif opcion == "13":
            salir()
        else:
            print("Opción inválida. Intente de nuevo.")


menu()
