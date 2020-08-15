#################################################################################
# Para el primer apartado , se necesitan algunas librerias como :
#
#   Numpy -> pip install numpy || pip install scipy || pip install -U numpy
#   Scikit-fuzzy -> pip install -U scikit-fuzzy
#


import numpy as np 
import skfuzzy as fuzz 
from skfuzzy import control as ctrl
from utilities.readCSV import getOutputs
from utilities.tools import onlytInt


def fusification(__csv_name__):

    """
        Funcion que obtiene la base de conocimiento del calibre de una fruta
        y crea las funciones de pertenencia triangular para cada caracteristica
        de una cereza.

        La funcion entrega 3 graficos ademas de retornar los datos correspondientes
        de las funciones.

        Por cada arreglo numero de dominio, existe 3 conjuntos difusos.

    """
    
    # Se debe saber que para la fusificacion se cuenta con varios tipos de
    # caracteristicas por fruto:
    #  
    #   - Forma: {Angosta, Normal, Ancha}
    #       La forma esta dada por :  Diametro(calibre)
    #                                 -----------------
    #                                      Altura   
    #
    #   - Firmeza de la pulpa: {Verde, Madura, Podrida}
    #       La firmeza de la pulpa esta dada en % por lo
    #       que su valor varia de [0,100] o [0,1]
    #
    #   - Cobertura: {Leve, Parcial, Completa}
    #       La covertura de manchas esta dada en % por lo
    #       que su valor varia entre [0,100] o [0,1]
    #
    #   - Comercializacion: {Exportable, Comercial, Desecho}.
    #       La comercializacion sera tomada como un porcentaje
    #       por lo que toma valores del [0,1]
    #

    # Con lo anterior podemos dejar el dominio de cada una de las caracteristicas

    # se importa la base de conocimiento:

    # Salidas y calibre -> obtenidas de la tabla de salidas
    _,caliber = getOutputs(__csv_name__)


    ################################################################################
    # FORMA
    # Dado que la forma se define como : diametro / altura .
    # La altura se asumira que tendra el mismo dominio que el diametro
    # esto quiere decir que tomará valores entre [18,32]
    

    # Ya la altura y el diametro cuentan con el mismo dominio, la división 
    # de estas tomará numeros entre el [0 , max/min] -> [0, 32/18]

    caliber = onlytInt(caliber)
    max_shape = max(caliber)/min(caliber)
    shape_domain = np.arange(0, max_shape, 0.01)
    shape = ctrl.Antecedent(shape_domain,"Shape")
    
    shape["Angosta"] = fuzz.trimf(shape.universe, [0, 0,max_shape/2])
    shape["Normal"] = fuzz.trimf(shape.universe, [0, max_shape/2, max_shape])
    shape["Ancha"] = fuzz.trimf(shape.universe, [max_shape/2, max_shape,max_shape])

    print(shape)


    ################################################################################
    # FIRMEZA DE LA PULPA

    # Dado que la firmeza de la pulpa es un porcentaje, estos toman valores de 
    # [0,100] o de [0,1]

    firmness_domain = np.arange(0, 101, 1)
    firmness = ctrl.Antecedent(firmness_domain, "Firmness")
    firmness["Verde"] = fuzz.trapmf(firmness.universe, [0, 0, 15, 45])
    firmness["Madura"] = fuzz.trimf(firmness.universe, [15, 45, 75])
    firmness["Podrida"] = fuzz.trapmf(firmness.universe,[60, 75, 100, 100])

    ################################################################################
    # COBERTURA DE MANCHAS

    # Dado que la coberturaa de manchas es un porcentaje, estos toman valores de 
    # [0,100] o de [0,1]
    
    coverage_domain = np.arange(0, 101, 1)
    coverage = ctrl.Antecedent(coverage_domain, "Coverage")
    
    coverage["Leve"] = fuzz.trapmf(coverage.universe, [0, 0, 15, 50])
    coverage["Parcial"] = fuzz.trimf(coverage.universe, [15, 50, 80])
    coverage["Completa"] = fuzz.trapmf(coverage.universe, [70, 80, 100, 100])

    ################################################################################
    # COMERCIALIZACION
    #
    comerce_domain = np.arange(0, 1.01, 0.01)
    comerce = ctrl.Consequent(comerce_domain, "Comerce")
    comerce["Desecho"] = fuzz.trimf(comerce.universe, [0, 0, 0.5])
    comerce["Comercial"] = fuzz.trimf(comerce.universe, [0, 0.5, 1])
    comerce["Exportacion"] = fuzz.trimf(comerce.universe, [0.5, 1, 1])


    # Graficos de los Antecedentes
    
    shape.view()
    firmness.view()
    coverage.view()
    
    return shape,firmness,coverage,comerce
