
import skfuzzy as fuzz 
from skfuzzy import control as ctrl
from utilities.readCSV import getInferenceTable

def inferenceRules(csv_rules_name,fuzzy_shape,fuzzy_firmness,fuzzy_coverage,fuzzy_comerce):
    '''
    ------------------------------------------------------------------------------------
    Funcion que lee un archivo CSV de la tabla de inferencias y genera una lista de
    reglas. Por defecto las 3 primeras son los Antecedentes, utilizando Mandani (& / |)
    y la ultima es el Consecuente o la implicancia

    :param csv_rules_name: str. Nombre del archivo CSV que tiene la tabla de inferencia.

    :param fuzzy_shape: skfuzzy.CtrlSystem. Modulo de 'control' con las funciones de pertecencias
                        para el Antedecente de 'Forma'
    
    :param fuzzy_firmness: skfuzzy.CtrlSystem. Modulo de 'control' con las funciones de pertecencias
                        para el Antedecente de 'Firmeza de la pulpa'

    :param fuzzy_overage: skfuzzy.CtrlSystem. Modulo de 'control' con las funciones de pertecencias
                        para el Antedecente de 'Covertura de Mancas'
    
    :param fuzzy_comerce: skfuzzy.CtrlSystem. Modulo de 'control' con las funciones de pertecencias
                        para el Consecuente de 'Exportacion'

    :return: lista de reglas.

    '''

    rules_set = []
    rules = getInferenceTable(csv_rules_name)
    for rule in rules:
        new_rule = ctrl.Rule(fuzzy_shape[rule[0]] & fuzzy_firmness[rule[1]] & fuzzy_coverage[rule[2]] , fuzzy_comerce[rule[3]])
        rules_set.append(new_rule)
    return rules_set

def computeInference(inference_rules,shape_value,firmness_value,coverage_value):

    '''
    -------------------------------------------------------------------------
    Funcion que se encarga de trabajar con las reglas de inferencia y computar
    sobre ellas los datos ingresados por un usuario. Los datos son ingresados
    como inputs.

    :param inference_rules: lista de reglas. Todas las reglas necesarias que
                            Se necesitan para computar.
    
    :param shape_value: int. Valor ingresado por un usuario.

    :param firmness_value: int. Valor ingresado por un usuario.

    :param coverage_value: int. Valor ingresado por un usuario.

    :return result: int. Valor en porcentaje que dice que tanto pertenece 
                        el comercio en su funcion de pertenencia

    :return compute: ControlSystemSimulation . Objeto de computo que posee
                                                todos los valores del computo
                                                realizado.

    '''

    compute_control = ctrl.ControlSystem(inference_rules)

    compute = ctrl.ControlSystemSimulation(compute_control)

    compute.input['Shape'] = shape_value
    compute.input['Firmness'] = firmness_value
    compute.input['Coverage'] = coverage_value

    compute.compute()

    result = compute.output['Comerce']
    
    return result,compute

def customInference(shape,firmness,coverage,comerce):
    '''
    Funcion que dados los objetos de control de skfuzzy, obtiene la valuacion en porentaje
    mas alta segun los datos ingresados por el usuario. Evalua cada valor de usuario en las 3
    funciones de pertencia por categoria y obtiene la el porcentaje evaluado mas alto entre las 3
    divisiones de la categoria, devolviendo el 'str' de la division

    :param shape:  tumpla con skfuzzy.CtrlSystem. Modulo de 'control' con las funciones de pertecencias
                        para el Antedecente de 'Forma', en la posicion 0 y el valor de entrada
                        del usuario (int) en la posicion 1.
    
    :param firmness:  tumpla con skfuzzy.CtrlSystem. Modulo de 'control' con las funciones de pertecencias
                        para el Antedecente de 'Firmeza de la pulpa', en la posicion 0 y el valor de entrada
                        del usuario (int) en la posicion 1.

    :param overage:  tumpla con skfuzzy.CtrlSystem. Modulo de 'control' con las funciones de pertecencias
                        para el Antedecente de 'Covertura de Mancas', en la posicion 0 y el valor de entrada
                        del usuario (int) en la posicion 1.
    
    :param comerce:  tumpla con skfuzzy.CtrlSystem. Modulo de 'control' con las funciones de pertecencias
                        para el Consecuente de 'Exportacion', en la posicion 0 y el valor de entrada
                        del usuario (int) en la posicion 1.

    :return shape_out: str. Division de la categoria de 'Forma' que segun su funcion es la mas alta.

    :return firmness_out: str. Division de la categoria de 'Firmeza' que segun su funcion es la mas alta.

    :return coverage_out: str. Division de la categoria de 'Covertura' que segun su funcion es la mas alta.

    :return comerce_out: str. Division de la categoria de 'Exportacion' que segun su funcion es la mas alta.

    '''
    
    
    Angosta = ('Angosta', fuzz.interp_membership(shape[0].universe, shape[0]['Angosta'].mf, shape[1]))
    Normal = ('Normal', fuzz.interp_membership(shape[0].universe, shape[0]['Normal'].mf, shape[1]))
    Ancha = ('Ancha', fuzz.interp_membership(shape[0].universe, shape[0]['Ancha'].mf, shape[1]))

    shape_list= [Angosta,Normal,Ancha]
    ## Maximo valor evaluado entre las 3 divisiones de Forma
    shape_out = max(shape_list,key=lambda item:item[1])[0]



    Verde = ('Verde', fuzz.interp_membership(firmness[0].universe, firmness[0]['Verde'].mf, firmness[1]))
    Madura = ('Madura', fuzz.interp_membership(firmness[0].universe, firmness[0]['Madura'].mf, firmness[1]))
    Podrida = ('Podrida', fuzz.interp_membership(firmness[0].universe, firmness[0]['Podrida'].mf, firmness[1]))

    firmness_list= [Verde,Madura,Podrida]
    ## Maximo valor evaluado entre las 3 divisiones de Firmeza
    firmness_out = max(firmness_list,key=lambda item:item[1])[0]

    Leve = ('Leve', fuzz.interp_membership(coverage[0].universe, coverage[0]['Leve'].mf, coverage[1]))
    Parcial = ('Parcial', fuzz.interp_membership(coverage[0].universe, coverage[0]['Parcial'].mf, coverage[1]))
    Completa = ('Completa', fuzz.interp_membership(coverage[0].universe, coverage[0]['Completa'].mf, coverage[1]))

    coverage_list=[Leve,Parcial,Completa]
    ## Maximo valor evaluado entre las 3 divisiones de Covertura
    coverage_out = max(coverage_list,key=lambda item:item[1])[0]

    Desecho = ('Desecho', fuzz.interp_membership(comerce[0].universe, comerce[0]['Desecho'].mf, comerce[1]))
    Comercial = ('Comercial', fuzz.interp_membership(comerce[0].universe, comerce[0]['Comercial'].mf, comerce[1]))
    Exportacion = ('Exportacion', fuzz.interp_membership(comerce[0].universe, comerce[0]['Exportacion'].mf, comerce[1]))

    comerce_list = [Desecho,Comercial,Exportacion]
    ## Maximo valor evaluado entre las 3 divisiones de Exportacion
    comerce_out = max(comerce_list,key=lambda item:item[1])[0]

    
    return shape_out,firmness_out,coverage_out,comerce_out
    

