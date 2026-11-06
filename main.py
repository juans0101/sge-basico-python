"""Sistema de Gestión de Estudiantes (SGE) básico.

Aplicación de consola para registrar, listar, buscar y consultar estudiantes
"""


def leer_entero(mensaje, minimo=None, maximo=None):
    """Solicita un número entero y repite la entrada hasta que sea válida."""
    while True:
        try:
            valor = int(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"El valor debe ser mayor o igual a {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"El valor debe ser menor o igual a {maximo}.")
                continue
            return valor
        except ValueError:
            print("Entrada no válida. Digite un número entero.")


def leer_texto(mensaje):
    """Solicita texto no vacío y elimina espacios innecesarios."""
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("Este campo no puede quedar vacío.")


def leer_promedio(mensaje):
    """Lee un promedio numérico dentro del rango académico de 0.0 a 5.0."""
    while True:
        try:
            valor = float(input(mensaje).replace(",", "."))
            if 0.0 <= valor <= 5.0:
                return valor
            print("El promedio debe estar entre 0.0 y 5.0.")
        except ValueError:
            print("Entrada no válida. Digite un número, por ejemplo 4.2.")


def leer_confirmacion(mensaje):
    """Devuelve True para sí y False para no; valida la respuesta."""
    while True:
        respuesta = input(mensaje).strip().lower()
        if respuesta in ("s", "si", "sí"):
            return True
        if respuesta in ("n", "no"):
            return False
        print("Respuesta no válida. Escriba S para sí o N para no.")


def buscar_estudiante_por_id(estudiantes, identificacion):
    """Busca secuencialmente un estudiante. Devuelve el registro o None."""
    for estudiante in estudiantes:
        if estudiante["id"] == identificacion:
            return estudiante
    return None


def mostrar_estudiante(estudiante):
    """Imprime la información de un estudiante en formato uniforme."""
    print("-" * 52)
    print(f"ID:             {estudiante['id']}")
    print(f"Nombre:         {estudiante['nombre']}")
    print(f"Edad:           {estudiante['edad']}")
    print(f"Programa:       {estudiante['programa']}")
    print(f"Promedio:       {estudiante['promedio']:.2f} / 5.00")
    print("-" * 52)


def agregar_estudiantes(estudiantes, contador_estudiantes):
    """Registra uno o varios estudiantes y actualiza el contador.

    El while True ejecuta primero el registro y consulta al final si se repite,
    simulando un ciclo condicionado al final (hacer-mientras).
    """
    while True:
        print("\n--- REGISTRO DE ESTUDIANTE ---")
        identificacion = leer_entero("ID (entero positivo): ", minimo=1)

        # Decisión simple: impedir que se registren identificaciones repetidas.
        if buscar_estudiante_por_id(estudiantes, identificacion) is not None:
            print("No se puede registrar: ya existe un estudiante con ese ID.")
        else:
            nuevo_estudiante = {
                "id": identificacion,
                "nombre": leer_texto("Nombre completo: "),
                "edad": leer_entero("Edad: ", minimo=5, maximo=120),
                "programa": leer_texto("Programa académico: "),
                "promedio": leer_promedio("Promedio (0.0 a 5.0): "),
            }
            estudiantes.append(nuevo_estudiante)
            contador_estudiantes += 1
            print("Estudiante registrado correctamente.")

        # La pregunta se hace después de realizar al menos un intento de registro.
        continuar_agregando = leer_confirmacion(
            "¿Desea registrar otro estudiante? (S/N): "
        )
        if not continuar_agregando:
            break

    return contador_estudiantes


def mostrar_estudiantes(estudiantes, contador_estudiantes, descendente=False):
    """Muestra todos los estudiantes en orden ascendente o descendente."""
    if contador_estudiantes == 0:
        print("No hay estudiantes registrados.")
        return

    orden = "descendente" if descendente else "ascendente"
    print(f"\n--- LISTA DE ESTUDIANTES (ORDEN {orden.upper()}) ---")

    if descendente:
        # Iteración descendente: comienza en el último índice y termina en cero.
        for indice in range(contador_estudiantes - 1, -1, -1):
            mostrar_estudiante(estudiantes[indice])
    else:
        # Iteración ascendente: recorre desde el índice cero.
        for indice in range(0, contador_estudiantes):
            mostrar_estudiante(estudiantes[indice])

    print(f"Total de estudiantes: {contador_estudiantes}")


def buscar_y_mostrar_estudiante(estudiantes):
    """Solicita un ID y presenta el resultado de la búsqueda."""
    print("\n--- BÚSQUEDA POR ID ---")
    identificacion = leer_entero("Ingrese el ID que desea buscar: ", minimo=1)
    estudiante = buscar_estudiante_por_id(estudiantes, identificacion)

    # Decisión simple para diferenciar búsqueda exitosa y búsqueda fallida.
    if estudiante is not None:
        print("Estudiante encontrado:")
        mostrar_estudiante(estudiante)
    else:
        print(f"No se encontró un estudiante con el ID {identificacion}.")


def mostrar_resumen_academico(estudiantes, contador_estudiantes):
    """Calcula el promedio general usando una variable de sumatoria."""
    print("\n--- RESUMEN ACADÉMICO ---")
    if contador_estudiantes == 0:
        print("No hay datos suficientes para generar el resumen.")
    else:
        sumatoria_promedios = 0.0
        for estudiante in estudiantes:
            sumatoria_promedios += estudiante["promedio"]

        promedio_general = sumatoria_promedios / contador_estudiantes
        print(f"Estudiantes registrados: {contador_estudiantes}")
        print(f"Sumatoria de promedios: {sumatoria_promedios:.2f}")
        print(f"Promedio general: {promedio_general:.2f} / 5.00")

        # Decisión anidada: primero valida aprobación general y luego clasifica.
        if promedio_general >= 3.0:
            if promedio_general >= 4.5:
                nivel = "alto"
            elif promedio_general >= 4.0:
                nivel = "sobresaliente"
            else:
                nivel = "satisfactorio"
            print(f"Resultado general: aprobado ({nivel}).")
        else:
            print("Resultado general: promedio por debajo del mínimo aprobatorio.")


def mostrar_menu():
    """Presenta las opciones disponibles en el sistema."""
    print("\n" + "=" * 52)
    print("       SISTEMA DE GESTIÓN DE ESTUDIANTES")
    print("=" * 52)
    print("1. Agregar estudiante(s)")
    print("2. Mostrar todos los estudiantes (ascendente)")
    print("3. Buscar estudiante por ID")
    print("4. Ver resumen académico")
    print("5. Mostrar estudiantes (orden descendente)")
    print("6. Salir")
    print("=" * 52)


def ejecutar_sistema():
    """Controla el ciclo principal y distribuye las opciones del menú."""
    estudiantes = []  # Lista dinámica de diccionarios.
    contador_estudiantes = 0  # Variable de conteo sincronizada con la lista.
    bandera_salir = False  # Bandera que controla la terminación del menú.

    # while condicionado al comienzo: el menú se repite mientras la bandera sea False.
    while not bandera_salir:
        mostrar_menu()
        opcion = leer_entero("Seleccione una opción (1-6): ", minimo=1, maximo=6)

        # match-case cumple la función de una decisión múltiple tipo switch.
        match opcion:
            case 1:
                contador_estudiantes = agregar_estudiantes(
                    estudiantes, contador_estudiantes
                )
            case 2:
                mostrar_estudiantes(estudiantes, contador_estudiantes)
            case 3:
                buscar_y_mostrar_estudiante(estudiantes)
            case 4:
                mostrar_resumen_academico(estudiantes, contador_estudiantes)
            case 5:
                mostrar_estudiantes(
                    estudiantes, contador_estudiantes, descendente=True
                )
            case 6:
                bandera_salir = True
                print("\nGracias por utilizar el Sistema de Gestión de Estudiantes.")


if __name__ == "__main__":
    ejecutar_sistema()
