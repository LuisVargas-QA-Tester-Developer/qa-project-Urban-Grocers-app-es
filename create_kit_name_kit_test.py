#IMPORTACIÓN DE ARCHIVOS REQUERIDOS
import sender_stand_request
import data
from sender_stand_request import post_create_new_user

#FUNCION PARA OBTENER CUERPO QUE SE INCLUIRÁ EN LA SOLICITUD PARA CREAR UN NUEVO KIT
def get_body_kit(name=None):
    body_kit = data.kit_body.copy()
    if name is not None:
        body_kit["name"] = name
    else:
        body_kit.pop("name", None)
    return body_kit

#FUNCIÓN PARA REALIZAR PRUEBAS POSITIVAS EN LA CREACIÓN DE NUEVOS KITS Y COMPROBAR CÓDIGO DE ESTADO 201

def possitive_assert_create_kit(name):

                        # token_user almacena token de usuario.
                        # body_kit almacena estructura json parametros para el nuevo kit
                        # response_kit almacena respuesta de la solicitud crear nuevo kit
                        # print() Imprime respuesta
                        # assert comprueba que el código de estado sea el correcto con criterio falso o verdadero

    token_user = sender_stand_request.post_create_new_user()
    print("------------------------------------------------------")
    body_kit = get_body_kit(name)
    response_kit = sender_stand_request.post_create_new_kits(body_kit, token_user)
    print(response_kit.json())
    print("RESPONSE REQUEST KITS: " + str(
    response_kit.json().get("user").get("authToken")) + " código de estado: " + str(response_kit.status_code))
    assert response_kit.status_code == 201
    assert response_kit.json().get("user").get("authToken") == token_user
    print("-----------------------------------------------------")

#FUNCIÓN PARA REALIZAR PRUEBAS NEGATIVAS EN LA CREACIÓN DE NUEVOS KITS Y COMPROBAR CÓDIGO DE ESTADO 400

def negative_assert_create_kit(name):

                        #token_user almacena token de usuario.
                        # body_kit almacena estructura json parametros para el nuevo kit
                        #response_kit almacena respuesta de la solicitud crear nuevo kit
                        #print() Imprime respuesta
                        #assert comprueba que el código de estado sea el correcto con criterio falso o verdadero

    token_user = sender_stand_request.post_create_new_user()
    body_kit = get_body_kit(name)
    response_kit = sender_stand_request.post_create_new_kits(body_kit, token_user)
    print("Response request kits: ", response_kit.text)
    print("Status code: ", response_kit.status_code)

    assert response_kit.status_code == 400

#PRUEBAS PARA EL CAMPO "name", VERIFICACIÓN DEL CÓDIGO DE ESTADO EN LA RESPUESTA DE LA SOLICITUD AL CREAR UN NUEVO KIT.

#----------------------------------------------------------

#Prueba 1-----------UN CARACTER EN LA PROPIEDAD "name"
def test_create_kit_name_1_character():
    possitive_assert_create_kit("f")

#--------------------------------------------------------

#Prueba 2---------511 caracteres maximo permitidos
def test_create_kit_name_511_character():
    possitive_assert_create_kit(data.kit_name_511)

#----------------------------------------------------------

#Prueba 3--------no se permite campo vacio
def test_create_kit_name_0_character():
    negative_assert_create_kit("")

#-------------------------------------------------------------

#Prueba 4------------512__caracteres, esta por fuera del rango permitido
def test_create_kit_name_512_character():
    negative_assert_create_kit(data.kit_name_512)

#---------------------------------------------------------------

#Prueba 5------------Se permite caracteres especiales en el campo
def test_create_kit_name_special_characters():
    possitive_assert_create_kit('№%@".-_,')

#---------------------------------------------------------------

#Prueba 6---------------Se permite espacios en el campo
def test_create_kit_empty_name():
    possitive_assert_create_kit("A aa")

#-----------------------------------------------------------------

#Prueba 7------------------Se permite numeros como string
def test_create_kit_name_numbers():
    possitive_assert_create_kit("123")

#-----------------------------------------------------------------

#Prueba 8---------------campo ausente, no se envia el parametro "name"
def test_create_kit_name_missing_parameter():
    negative_assert_create_kit(None)

#-------------------------------------------------------------------

#Prueba 9----------------No se valores numerico en el campo.
def test_create_kit_numbers_date_name():
    negative_assert_create_kit(123)

#---------------------------------------------------------------------


