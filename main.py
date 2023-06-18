import secrets

# Generar una cadena de caracteres aleatoria como contraseña
password = secrets.token_hex(16) 

from app import app