from cryptography.fernet import Fernet
from django.conf import settings
from datetime import date


# Función de encriptación
def encrypt_data(data) -> str:
    """
    Encripta datos utilizando Fernet.
    Soporta cadenas, fechas y números.
    """
    fernet = settings.FERNET
    
    # Si es una fecha, la convertimos a cadena en formato 'YYYY-MM-DD'
    if isinstance(data, date):  # Si es una instancia de 'date'
        data = data.strftime('%Y-%m-%d')  # Convertimos a cadena
    
    # Si es un número, lo convertimos a cadena
    elif isinstance(data, (int, float)):  # Si es un número entero o flotante
        data = str(data)  # Convertimos a cadena
    
    return fernet.encrypt(data.encode()).decode()  # Encriptamos y devolvemos como cadena

# Función de desencriptación
def decrypt_data(data: str):
    """
    Desencripta datos utilizando Fernet.
    Devuelve el tipo original de los datos (cadena, fecha o número).
    """
    fernet = settings.FERNET
    decrypted_data = fernet.decrypt(data.encode()).decode()  # Desencriptamos y convertimos a cadena
    
    # Intentamos convertir el valor desencriptado en una fecha, si tiene el formato 'YYYY-MM-DD'
    try:
        # Intentamos convertir a fecha usando el formato 'YYYY-MM-DD'
        return date.fromisoformat(decrypted_data)  # Intenta convertir a 'date'
    except ValueError:
        pass  # No es una fecha, lo dejamos como está

    # Intentamos convertirlo a un número
    try:
        return int(decrypted_data)  # Si se puede, convertimos a entero
    except ValueError:
        try:
            return float(decrypted_data)  # Si no, lo intentamos convertir a flotante
        except ValueError:
            pass  # Si no es número, lo dejamos como cadena
    
    return decrypted_data  # Si no es ni fecha ni número, devolvemos la cadena tal cual


