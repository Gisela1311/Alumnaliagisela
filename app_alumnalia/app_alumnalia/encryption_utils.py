from cryptography.fernet import Fernet
from django.conf import settings
from datetime import date, datetime


# Función de encriptación
def encrypt_data(data) -> str:
    """
    Encripta datos utilizando Fernet.
    Soporta cadenas, fechas y números.
    """
    fernet = settings.FERNET
    
    # Si es una fecha, convertirla a cadena en formato ISO
    if isinstance(data, (date, datetime)):  # Detectar fechas
        data = data.isoformat()
    
    # Si es un número, convertirlo a cadena
    elif isinstance(data, (int, float)):  # Detectar números
        data = str(data)
    
    # Encriptar siempre como cadena
    return fernet.encrypt(data.encode()).decode()

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
        pass  # No es entero, continuar
    
    # Detectar si es un número flotante
    try:
        return float(decrypted_data)  # Si es un número flotante, convertir
    except ValueError:
        pass  # No es flotante, continuar
    
    # Si no es fecha ni número, devolver como cadena
    return decrypted_data


