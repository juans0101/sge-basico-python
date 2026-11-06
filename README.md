# Sistema de Gestión de Estudiantes (SGE) básico

Aplicación de consola desarrollada en Python para registrar estudiantes, consultar el listado, buscar por ID y generar un resumen académico.

## Requisitos

- Python 3.10 o superior.
- No requiere instalar paquetes externos.

## Funcionalidades

1. Registrar uno o varios estudiantes.
2. Mostrar el listado completo en orden ascendente.
3. Buscar estudiantes por su ID.
4. Calcular la cantidad de estudiantes, la sumatoria de promedios y el promedio general.
5. Mostrar el listado en orden descendente.
6. Salir del sistema.

Los registros se almacenan en una lista de diccionarios durante la ejecución. Esta versión introductoria no utiliza archivos ni base de datos; por tanto, los datos se reinician al cerrar el programa.

## Cómo ejecutar el programa

Desde una terminal ubicada en la carpeta del proyecto, ejecutar:

```bash
python main.py
```

## Ejecutar las pruebas unitarias

```bash
python -m unittest -v
```

## Estructuras de control demostradas

- Decisiones simples y anidadas con `if`, `elif` y `else`.
- Decisión múltiple con `match-case`.
- Repetición condicionada al comienzo con `while`.
- Simulación de repetición condicionada al final mediante `while True` y `break`.
- Iteraciones ascendentes y descendentes con `for` y `range()`.
- Variables especiales de conteo, sumatoria y bandera.
- Funciones reutilizables y lista de diccionarios.

## Archivos principales

| Archivo | Descripción |
|---|---|
| `main.py` | Código fuente de la aplicación. |
| `test_sge.py` | Pruebas unitarias de funciones principales. |
| `diagrama_flujo_sge.png` | Diagrama de flujo del algoritmo principal. |

## Entrega académica

El documento técnico PDF y las evidencias de ejecución deben agregarse en las carpetas `docs/` y `evidencias/`, respectivamente, para completar la estructura de entrega.

Proyecto académico individual: Sistema de Gestión de Estudiantes (SGE) básico.
