def validarDatoNumerico(mensaje):
    while True:
        try:
            datoNumerico = int(input(mensaje))
            break
        except:
            print("Debe ingresar un dato NUMERICO!")
    return datoNumerico

def validarDatoString(mensaje):
    while True:        
        try:
            dato = input(mensaje)
            if dato.isdigit():
                raise Exception
            else:
                break
        except:
            print("solo se permite texto")
    return dato

def validarDatoBool(mensaje):
    while True:        
        try:
            dato = str(input(mensaje))
            if dato.upper() == "S" or dato == "N":
                break
            else:
                raise Exception
        except:
            print("solo se permite S/N")
    return dato

def validarRut(Rut):
    #Validador de Rut
    rutValidado = False
    return rutValidado