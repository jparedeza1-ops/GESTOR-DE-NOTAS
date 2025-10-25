
cursos = []
notas = []
Historial = []
Promedios = []

def ordenamiento_burbuja_nota(lista):
    n = len(lista)
    lista_copia = lista.copy()
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_copia[j]['nota'] < lista_copia[j + 1]['nota']:
                lista_copia[j], lista_copia[j + 1] = lista_copia[j + 1], lista_copia[j]
    return lista_copia

def ordenamiento_insercion_nombre(lista):
    n = len(lista)
    lista_copia = lista.copy()

    for i in range(1, n):
        key_curso = lista_copia[i]
        j = i - 1
        
        while j >= 0 and key_curso['nombre'].lower() < lista_copia[j]['nombre'].lower():
            lista_copia[j + 1] = lista_copia[j]
            j -= 1
        lista_copia[j + 1] = key_curso
        
    return lista_copia

def menu():
    print("Bienvenido al menu")
    print("˚˖𓍢🌷✧˚.🎀⋆"*30)
    print("1. Registrar nuevo curso")
    print("2. Mostrar todos los cursos y notas")
    print("3. Calcular promedio general")
    print("4. Contar cursos aprobados y reprobados")
    print("5. Buscar curso por nombre")
    print("6. Actualizar nota de un curso")
    print("7. Eliminar un curso")
    print("8. Ordenar cursos por nota")
    print("9. Ordenar cursos por nombre")
    print("10. Buscar curso por nombre (binaria)")
    print("11. Simular cola de solicitudes de revisión")
    print("12. Mostrar historial de cambios")
    print("13. Salir")

def registrar_nuevo_curso():
    nombre_curso = input("Escriba el nombre del curso que va agregar: ")
    try:
        nota_curso = float(input(f"Ingrese la nota para {nombre_curso}: "))
        curso = {'nombre': nombre_curso, 'nota': nota_curso}
        cursos.append(curso)
        notas.append(nota_curso)
        Historial.append(f"Se agregó nuevo curso: {nombre_curso} - Nota: {nota_curso}")
        print(f"Curso '{nombre_curso}' registrado con nota {nota_curso}")
    except ValueError:
        print("Error: La nota debe ser un número válido")

def mostrar_todos_los_cursos_y_notas():
    if not cursos:
        print("No hay cursos registrados")
        return
    print("\n--- Todos los cursos y notas ---")
    for i, curso in enumerate(cursos, 1):
        print(f"{i}. {curso['nombre']} - Nota: {curso['nota']:.2f}")

def promedio_general():
    if not notas:
        print("No hay notas para calcular promedio")
        return
    promedio = sum(notas) / len(notas)
    print(f"Promedio general: {promedio:.2f}")
    Historial.append(f"Se calculó promedio general: {promedio:.2f}")

def cursos_aprobados_y_reprobados():
    if not cursos:
        print("No hay cursos registrados")
        return
    
    aprobados = 0
    reprobados = 0
    
    for curso in cursos:
        if curso['nota'] >= 61:
            aprobados += 1
        else:
            reprobados += 1
    
    print(f"Cursos aprobados: {aprobados}")
    print(f"Cursos reprobados: {reprobados}")
    Historial.append(f"Se contaron cursos: {aprobados} aprobados, {reprobados} reprobados")

def buscar_curso_lineal():
    if not cursos:
        print("No hay cursos para buscar")
        return
        
    nombre_buscado = input("Ingrese el nombre del curso que busca: ").strip().lower()
    
    for curso in cursos:
        if nombre_buscado in curso['nombre'].lower():
            print(f"Curso encontrado: {curso['nombre']} - Nota: {curso['nota']:.2f}")
            Historial.append(f"Búsqueda lineal: {curso['nombre']}")
            return
    
    print("Curso no encontrado")

def actualizar_nota_curso():
    if not cursos:
        print("No hay cursos para actualizar")
        return
        
    nombre_curso = input("Ingrese el nombre del curso a actualizar: ").strip().lower()
    
    for i, curso in enumerate(cursos):
        if nombre_curso in curso['nombre'].lower():
            try:
                nueva_nota = float(input(f"Ingrese la nueva nota para {curso['nombre']}: "))
                nota_anterior = curso['nota']
                curso['nota'] = nueva_nota
                notas[i] = nueva_nota
                Historial.append(f"Actualización: {curso['nombre']} - Nota anterior: {nota_anterior}, Nueva nota: {nueva_nota}")
                print(f"Nota actualizada correctamente")
                return
            except ValueError:
                print("Error: La nota debe ser un número válido")
                return
    
    print("Curso no encontrado")

def eliminar_un_curso():
    if not cursos:
        print("No hay cursos para eliminar")
        return
        
    nombre_curso = input("Ingrese el nombre del curso a eliminar: ").strip().lower()
    
    for i, curso in enumerate(cursos):
        if nombre_curso in curso['nombre'].lower():
            curso_eliminado = cursos.pop(i)
            nota_eliminada = notas.pop(i)
            Historial.append(f"Eliminación: {curso_eliminado['nombre']} - Nota: {nota_eliminada}")
            print(f"Curso '{curso_eliminado['nombre']}' eliminado correctamente")
            return
    
    print("Curso no encontrado")

def ordenar_cursos_por_nota():
    if not cursos:
        print("No hay cursos para ordenar")
        return
        
    cursos_ordenados = ordenamiento_burbuja_nota(cursos)
    
    print("\n--- Cursos Ordenados por Nota (Descendente) ---")
    for i, curso in enumerate(cursos_ordenados, 1):
        print(f"{i}. {curso['nombre']} - Nota: {curso['nota']:.2f}")

def ordenar_cursos_por_nombre():
    if not cursos:
        print("No hay cursos para ordenar")
        return
        
    cursos_ordenados = ordenamiento_insercion_nombre(cursos)
    
    print("\n--- Cursos Ordenados Alfabéticamente ---")
    for i, curso in enumerate(cursos_ordenados, 1):
        print(f"{i}. {curso['nombre']} - Nota: {curso['nota']:.2f}")

def buscar_curso_binaria():
    if not cursos:
        print("No hay cursos para buscar")
        return
        
    cursos_ordenados = ordenamiento_insercion_nombre(cursos)
    nombre_buscado = input("Ingrese el nombre del curso a buscar: ").strip().lower()
    
    inicio = 0
    fin = len(cursos_ordenados) - 1
    encontrado = False
    
    while inicio <= fin:
        medio = (inicio + fin) // 2
        curso_medio = cursos_ordenados[medio]['nombre'].lower()
        
        if curso_medio == nombre_buscado:
            encontrado = True
            curso_encontrado = cursos_ordenados[medio]
            print(f"Curso encontrado: {curso_encontrado['nombre']} - Nota: {curso_encontrado['nota']:.2f}")
            Historial.append(f"Búsqueda binaria: {curso_encontrado['nombre']}")
            break
        elif curso_medio < nombre_buscado:
            inicio = medio + 1
        else:
            fin = medio - 1
    
    if not encontrado:
        print("Curso no encontrado")

def simular_cola():
    from collections import deque
    cola = deque()
    
    while True:
        print("\n--- Cola de Solicitudes ---")
        print("1. Agregar solicitud")
        print("2. Atender solicitud")
        print("3. Mostrar cola actual")
        print("4. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            solicitud = input("Ingrese la solicitud: ")
            cola.append(solicitud)
            print(f"Solicitud '{solicitud}' agregada a la cola")
            Historial.append(f"Solicitud agregada: {solicitud}")
        elif opcion == "2":
            if cola:
                atendido = cola.popleft()
                print(f"Solicitud '{atendido}' atendida")
                Historial.append(f"Solicitud atendida: {atendido}")
            else:
                print("No hay solicitudes en espera")
        elif opcion == "3":
            if cola:
                print("Solicitudes en cola:", list(cola))
            else:
                print("No hay solicitudes en espera")
        elif opcion == "4":
            break
        else:
            print("Opción no válida")

def mostrar_historial():
    if not Historial:
        print("No hay historial de cambios")
        return
        
    print("\n--- Historial de Cambios ---")
    for i, accion in enumerate(Historial, 1):
        print(f"{i}. {accion}")

def main():
    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_nuevo_curso()
        elif opcion == "2":
            mostrar_todos_los_cursos_y_notas()
        elif opcion == "3":
            promedio_general()
        elif opcion == "4":
            cursos_aprobados_y_reprobados()
        elif opcion == "5":
            buscar_curso_lineal()
        elif opcion == "6":
            actualizar_nota_curso()
        elif opcion == "7":
            eliminar_un_curso()
        elif opcion == "8":
            ordenar_cursos_por_nota()
        elif opcion == "9":
            ordenar_cursos_por_nombre()
        elif opcion == "10":
            buscar_curso_binaria()
        elif opcion == "11":
            simular_cola()
        elif opcion == "12":
            mostrar_historial()
        elif opcion == "13":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida")
        
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()
