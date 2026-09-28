# Proyecto Urban Grocers

## Sobre Urban Grocers

Urban Grocers es una aplicación de compra de productos de abarrotes que permite a sus usuarios organizar productos mediante kits.

Un kit representa un conjunto de productos agrupados bajo un nombre, por ejemplo, un kit de desayuno que puede incluir leche, pan y huevos. Cada kit se crea asociado a un usuario específico.

Dentro del flujo probado en este proyecto, se crea un usuario, se obtiene su token de autenticación y se utiliza ese token para solicitar la creación de un kit.

## Objetivo de las pruebas

Este proyecto automatiza pruebas de API sobre la creación de kits, enfocándose específicamente en las validaciones del campo `name`.

La suite utiliza diferentes valores y tipos de datos para comprobar el comportamiento del campo según los requisitos definidos.

## Tecnologías

- Python
- Pytest
- Requests

## Instalación

Instala las dependencias del proyecto desde la raíz del repositorio:

```powershell
py -m pip install -r requirements.txt
```

Las versiones utilizadas para comprobar el funcionamiento del proyecto están declaradas en `requirements.txt`.

## Configuración de la API

La URL del servidor no se almacena directamente en el código porque el entorno de pruebas utiliza una URL temporal.

Antes de ejecutar las pruebas, configura la variable de entorno `URL_SERVICE`.

En PowerShell:

```powershell
$env:URL_SERVICE="https://URL-ACTUAL-DEL-SERVIDOR"
```

Para comprobar que la variable está configurada:

```powershell
echo $env:URL_SERVICE
```

Si `URL_SERVICE` no está configurada, el proyecto detendrá la ejecución e indicará que falta la variable de entorno.

## Ejecución de las pruebas

Desde la raíz del proyecto:

```powershell
py -m pytest -v -s
```

Para comprobar únicamente el descubrimiento de las pruebas sin ejecutarlas:

```powershell
py -m pytest --collect-only -q
```

## Casos de prueba

La suite contiene 9 casos de prueba para el campo `name`, incluyendo:

- Límite mínimo válido de 1 carácter.
- Límite máximo válido de 511 caracteres.
- Cadena vacía.
- Valor de 512 caracteres.
- Caracteres especiales.
- Texto con espacios.
- Cadena compuesta por números.
- Ausencia del parámetro `name`.
- Valor de tipo numérico.

## Estructura del proyecto

- `configuration.py`: obtiene la URL del servidor desde la variable de entorno y contiene las rutas de la API.
- `data.py`: contiene los datos utilizados en las solicitudes y los casos de prueba.
- `sender_stand_request.py`: contiene las funciones para realizar las solicitudes a la API.
- `tests/test_create_kit_name.py`: contiene las pruebas automatizadas para el campo `name`.
- `requirements.txt`: declara las dependencias y versiones utilizadas en el proyecto.

## Resultados conocidos

Durante la ejecución de la suite se identificaron cuatro comportamientos diferentes a los resultados esperados:

- Campo `name` vacío: devuelve código 201; se esperaba 400.
- `name` de 512 caracteres: devuelve código 201; se esperaba 400.
- Ausencia del campo `name`: devuelve código 500; se esperaba 400.
- Valor numérico en `name`: devuelve código 201; se esperaba 400.

Estos resultados se mantienen visibles en la suite para evidenciar las diferencias entre el comportamiento actual de la API y los resultados esperados.
