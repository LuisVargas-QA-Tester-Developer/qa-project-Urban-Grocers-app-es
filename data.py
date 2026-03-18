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

#CAMPO "name" CON 511 CARACTERES, LO MÁXIMO PERMITIDO PARA ESTE CAMPO. USARLO PARA PRUEBA POSITIVA
#DEBERÁ ARROJAR CÓDIGO 201.

kit_body511 = {"name":"Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
            "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
            "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
            "cdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
            "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
            "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
            "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"}

#CAMPO "name" CON 512 CARACTERES, UN CARACTER DE MAS POR ENCIMA DE LO PERMITIDO. USARLO EN PRUEBA NEGATIVA
#DEBERÁ ARROJAR CÓDIGO 400

kit_body512 = {"name":"Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
            "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
            "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
            "cdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
            "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
            "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
            "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"}

