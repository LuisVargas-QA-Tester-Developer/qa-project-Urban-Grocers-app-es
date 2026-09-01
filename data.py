#ENCABEZADO DE LA SOLICITUD
headers = {
    "Content-Type": "application/json"
}
#DICIONARIO PARA SOLICITUD CREAR NUEVO USUARIO. SE INCLUIRÁ COMO CUERPO DE LA SOLICITUD.

user_body = {
    "firstName": "Mayawai",
    "email": "max@example.com",
    "phone": "+10005553535",
    "comment": "Cuidado con el perro",
    "address": "8042 Lancaster Ave.Hamburg, NY"
}

#CAMPO "name". ESTRUCTURA POR DEFECTO PRUEBAS POSITIVAS

kit_body = {
    "name": "Miprimerkit"
}

# Campo "name" con 511 caracteres: máximo permitido.
# Caso límite positivo: se espera código 201.

kit_name_511 = 'a' * 511

# Campo "name" con 512 caracteres: supera el máximo permitido.
# Caso límite negativo: se espera código 400.

kit_name_512 = 'a' * 512
