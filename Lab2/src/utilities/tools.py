


def parseInt(element):
    """
    -----------------------------------------------------------
    funcion que intenta convertir un elemento a su forma entera
        '58' -> 58.
    Sino se puede, solo se regresa el valor ingresado 

        :param element: element -> str
    
    :return: int | elemento ingresado
    """
    try:
        return int(element)
    except:
        return element





def onlytInt(array):
    """
    -----------------------------------------------------------
    funcion que elimina solo los elementos del tipo str de un
    array.
        :param array: array -> array. Conjunto de elementos entrantes
    
    :return: arreglo ingresado
    """

    for element in array:
        try:
            if element.isalpha():
                array.remove(element)
        except:
            pass
    return array


def getDataByUser():

    '''
    Funcion que obtiene los valores de entrada del usuario.
    los convierte en enteros o en flotantes segun lo que ingrese el usuario.
    Si alguna entrada no coincide con las reglas, se volvera a pedir

    :param height: int. Valor entregado por el usuario.

    :param diameter: int. Valor entregado por el usuario.

    :param firmness: int. Valor entregado por el usuario.

    :param coverage: int. Valor entregado por el usuario.

    '''


    # Altura
    while True:
        print('Ingrese el valor de la ALTURA en "mm" dentro del valor [18,32] : ')
        height = input()
        try:
            height = int(height)
            if height < 18 or height > 32:
                print('El valor ingresado está fuera del rango aceptado')
            else:
                break
        except ValueError:
            try:
                height = float(height)
                if height < 18 or height > 32:
                    print('El valor ingresado está fuera del rango aceptado')
                else:
                    break
            except ValueError:
                print ("El valor ingresado NO es un numero")

    # Diametro
    while True:
        print('Ingrese el valor de la DIAMETRO en "mm" dentro del valor [18,32] : ')
        diameter = input()
        try:
            diameter = int(diameter)
            if diameter < 18 or diameter > 32:
                print('El valor ingresado está fuera del rango aceptado')
            else:
                break
        except ValueError:
            try:
                diameter = float(diameter)
                if diameter < 18 or diameter > 32:
                    print('El valor ingresado está fuera del rango aceptado')
                else:
                    break
            except ValueError:
                print ("El valor ingresado NO es un numero")
    
    # Firmeza
    while True:
        print('Ingrese el valor de la FIRMEZA DE LA PULPA en "%" dentro del valor [0,100] : ')
        firmness = input()
        try:
            firmness = int(firmness)
            if firmness < 0 or firmness > 100:
                print('El valor ingresado está fuera del rango aceptado')
            else:
                break
        except ValueError:
            try:
                firmness = float(firmness)
                if firmness < 0 or firmness > 100:
                    print('El valor ingresado está fuera del rango aceptado')
                else:
                    break
            except ValueError:
                print ("El valor ingresado NO es un numero")
    

    # Covertura
    while True:
        print('Ingrese el valor de la COBERTURA DE MANCHAS en "%" dentro del valor [0,100] : ')
        coverage = input()
        try:
            coverage = int(coverage)
            if coverage < 0 or coverage > 100:
                print('El valor ingresado está fuera del rango aceptado')
            else:
                break
        except ValueError:
            try:
                coverage = float(coverage)
                if coverage < 0 or coverage > 100:
                    print('El valor ingresado está fuera del rango aceptado')
                else:
                    break
            except ValueError:
                print ("El valor ingresado NO es un numero")
    
    return height,diameter,firmness,coverage
    


