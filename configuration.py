                    #URL_SERVICE, variable de entorno, almacena la url del servidor
                    #CREATE_USER_PATH, almacena la ruta para crear un nuevo usuario
                    #KITS_PATH, almacena la ruta para crear un nuevo kit

import os

URL_SERVICE = os.getenv("URL_SERVICE")

if not URL_SERVICE:
    raise RuntimeError("URL_SERVICE environment variable is not set")

CREATE_USER_PATH = "/api/v1/users"

KITS_PATH = "/api/v1/kits"


