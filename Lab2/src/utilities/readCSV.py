import os
import csv
from utilities.tools import parseInt


def getOutputs(csv_name):
    """
    ------------------------------------------------------------------------
    funcion que lee un csv de salidas y retorna dos arreglos con las salidas
    y calibres 

        :param csv_name: csv_name -> str. Ubicacion relativa del archivo csv
    """

    with open(os.path.join(os.path.dirname(__file__), csv_name)) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        caliber = []
        output = []
        for row in csv_reader:
            if line_count == 0: # En este punto se estan leyendo los headers
                line_count += 1
            else:
                output.append(parseInt(row[0]))
                caliber.append(parseInt(row[1]))
                line_count += 1
        return output,caliber


def getInferenceTable(csv_name):
    """
    ------------------------------------------------------------------------
    funcion que lee el csv que posee las reglas de inferencia y retorna un arreglo
    con las reglas. Las reglas a su vez tambien son un arreglo.
        regla -> 

        :param csv_name: csv_name -> str. Ubicacion relativa del archivo csv
    """
    with open(os.path.join(os.path.dirname(__file__), csv_name)) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        rules=[]
        for row in csv_reader:
            if line_count == 0: # En este punto se estan leyendo los headers
                line_count += 1
            else:
                rules.append(row)
                line_count += 1
        return rules

def getOutput(csv_output_name,diameter):

    '''
    Funcion que dado el nombre del CSV que contiene los calibreas y las salidas
    obtiene el valor de la salida segun el calibre ingresado

        
    :param csv_output_name: str. Nombre del archivo csv

    :param diameter: int. Valor del calibre

    '''

    with open(os.path.join(os.path.dirname(__file__), csv_output_name)) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')

        for row in csv_reader:

            if row[1] == str(diameter):
                return int(row[0])
        return 0






