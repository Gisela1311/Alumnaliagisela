
letras=['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
dni=input("Introducir el DNI >")
try:
    num = int(dni[:-1])
    indice_letra = num % 23
    if letras[indice_letra] == dni[-1].upper():
        print(f"El DNI >{dni}< es correcto")
    else:
        print(f"El DNI >{dni}< es incorrecto")
except:
    print("no se ha introducido un DNI")