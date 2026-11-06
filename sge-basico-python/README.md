# Sistema de Gestión de Estudiantes (SGE) básico

Aplicación de consola en Python para registrar estudiantes, consultar el listado, buscar por ID y calcular un resumen académico.

## Requisitos

- Python 3.11 o superior recomendado.
- No requiere paquetes externos.

## Funcionalidades

1. Registrar uno o varios estudiantes.
2. Mostrar todos los registros en orden ascendente.
3. Buscar un estudiante por su ID.
4. Calcular cantidad, sumatoria y promedio general.
5. Mostrar los registros en orden descendente.
6. Salir del sistema.

Cada estudiante se guarda como un diccionario dentro de una lista dinámica. Los datos se conservan solo mientras se ejecuta el programa; al cerrarlo, se eliminan porque esta versión introductoria no utiliza archivos ni base de datos.

## Ejecución

Abre una terminal en esta carpeta y ejecuta:

```bash
python main.py
```

## Pruebas unitarias

```bash
python -m unittest -v
```

## Estructuras de programación demostradas

- `if`, `elif`, `else` y decisiones anidadas.
- `match-case` como decisión múltiple equivalente en propósito a `switch`.
- `while` para mantener el menú y validar entradas.
- `while True` con `break` al final de cada intento para simular un ciclo hacer-mientras.
- `for` con recorrido ascendente y `range()` con recorrido descendente.
- Variables especiales de conteo (`contador_estudiantes`), sumatoria (`sumatoria_promedios`) y bandera (`bandera_salir`).
- Lista de diccionarios y funciones reutilizables.

## Contenido del repositorio

```text
sge-basico-python/
├── main.py
├── test_sge.py
├── README.md
├── .gitignore
├── diagrama_flujo_sge.png
├── docs/
│   └── SGE_Documentacion_Tecnica.pdf
└── evidencias/
    ├── capturas PNG de las ejecuciones
    └── transcripciones TXT de las pruebas
```

## Publicar en GitHub

1. Crea en GitHub un repositorio vacío llamado `sge-basico-python`.
2. Abre una terminal dentro de esta carpeta.
3. Ejecuta los siguientes comandos y reemplaza `TU-USUARIO` por tu usuario de GitHub:

```bash
git init
git add .
git commit -m "Primera versión del Sistema de Gestión de Estudiantes"
git branch -M main
git remote add origin https://github.com/TU-USUARIO/sge-basico-python.git
git push -u origin main
```

Antes de entregar, completa en el PDF los campos de institución, asignatura, grupo, instructor y fecha.
