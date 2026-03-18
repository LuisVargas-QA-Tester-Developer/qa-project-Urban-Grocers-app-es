# Proyecto Urban Grocers
# _Pruebas para el campo "name", función crear nuevo kit por medio de un token de un usuario existente.
# _Archivo cofiguration.py, contiene url para solicitudes a la API.
# _Archivo send_stand_request.py, contiene funciones principales para crear nuevos usuarios y nuevos kits.
# _Archivo create_kit_name_kit_test.py, contiene funciones de pruebas para el campo "name".
# CONCLUSIONES
# Pruebas 3, 4, 8 y 9 fallan. Ejecución de pruebas con pytest y validadas con función assert.
# Prueba 3 falla: assert Validación campo vacio "name"={""}. Resultado esperado: Código 400 Bad request. Resultado actual: Código 201.
# Prueba 4 falla: assert Validación campo "name" permite más de 511 caracteres. Resultado esperado: Código 400 Bad request. Resultado actual: Código 201.
# Prueba 8 falla: assert Validación campo "name" ausente en la solicitud. Resultado esperado: Código 400 Bad reques.  Resultado actual: Código 500.
# Prueba 9 falla: assert Validación campo "name" acepta valores tipo número. Resultado esperado: Código 400 Bad request. Resultado actual: Código 201.