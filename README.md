# Proyecto Urban Grocers

Pruebas para el campo `name` de la función de creación de un nuevo kit mediante el token de un usuario existente.

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

Luego ejecuta las pruebas:

```powershell
py -m pytest -v -s
```

Si `URL_SERVICE` no está configurada, el proyecto detendrá la ejecución e indicará que falta la variable de entorno.

## Archivos del proyecto

- `configuration.py`: obtiene la URL del servidor desde la variable de entorno y contiene las rutas de la API.
- `sender_stand_request.py`: contiene las funciones para realizar las solicitudes a la API.
- `create_kit_name_kit_test.py`: contiene las pruebas para el campo `name`.

## Conclusiones

Las pruebas 3, 4, 8 y 9 presentan comportamientos diferentes a los resultados esperados.

- Prueba 3: el campo `name` vacío devuelve código 201; se esperaba 400.
- Prueba 4: un `name` de 512 caracteres devuelve código 201; se esperaba 400.
- Prueba 8: la ausencia del campo `name` devuelve código 500; se esperaba 400.
- Prueba 9: un valor numérico en `name` devuelve código 201; se esperaba 400.
