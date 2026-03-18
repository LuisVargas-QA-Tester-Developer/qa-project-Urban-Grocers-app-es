#IMPORTACIÓN DE ARCHIVOS REQUERIDOS PARA LAS SOLICITUDES
import configuration
import data
import requests


#FUNCIÓN PARA CREAR UN NUEVO USUARIO
def post_create_new_user():
    #Solicitud crear nuevo usuario
    response =  requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json = data.user_body, headers=data.headers)
    #Almacenar respuesta
    response = response.json()
    #Obtener el token
    token_user = response["authToken"]
    return token_user

#FUNCIÓN PARA CREAR UN NUEVO KIT INCLUYENDO UN TOKEN DE USUARIO EXISTENTE EN EL ENCABEZADO DE LA SOLICITUD
def post_create_new_kits(body_kit, token_user):
    #Copiar el token del usuario registrado, pegarlo entre las comillas vacías en el encabezado: Ejemplo:
    #headers={"Content-Type": "application/json", "Authorization": "Bearer " + "39b3ed99-9e32-440f-ab05-ce9556f58f73"
    response = requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
    json=body_kit, headers={"Content-Type": "application/json", "Authorization": "Bearer " + f"{token_user}"})
    return response

#FUNCIÓN PARA OBTENER LOS KITS DE UN USUARIO ESPECÍFICO
def get_all_kits(token_user):
    response = requests.get(configuration.URL_SERVICE + configuration.KITS_PATH, headers={"Content-Type": "application/json", "Authorization": "Bearer " + f"{token_user}"})
    return response