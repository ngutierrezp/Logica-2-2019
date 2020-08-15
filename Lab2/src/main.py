#################################################################################
# Para el primer apartado , se necesitan algunas librerias como :
#
#   Numpy -> pip install numpy || pip install scipy || pip install -U numpy
#   Scikit-fuzzy -> pip install -U scikit-fuzzy
#

# NOTA: los tildes de las palabras han sido suprimidos para guardar la compatibilidad
#       en los editores de texto.



from modules.fusification import fusification
from modules.inference import inferenceRules, computeInference, customInference
from utilities.tools import getDataByUser
from modules.desfusification import desfuzzy
from utilities.readCSV import getOutput
from utilities.writeFile import writefile
import skfuzzy as fuzz 


###############################################################################################
# MAIN

# Ejecutar desde desde .py


## fusificacion
sha, fir, cor, com = fusification('../knowledge/salidas.csv')

## generacion de reglas
rules = inferenceRules('../knowledge/tabla_inferencia.csv', sha, fir, cor, com)

## obtencion de los datos del usuario
height_input, diameter_input, firmness_input, coverage_input = getDataByUser()

## calculo de forma
shape_input = float(diameter_input) / height_input

## obtencion de salida dado el calibre
output = getOutput("../knowledge/salidas.csv",diameter_input)

## inicio del computo dadas las reglas y entradas de usuario
comerce_out, computeResult = computeInference(rules, shape_input, firmness_input, coverage_input)

## grafio de resultado
com.view(sim=computeResult)

## ontencion de los valores predominantes de cada categoria
sha_out,firm_out,cov_out,com_out = customInference([sha,shape_input],[fir,firmness_input],[cor,coverage_input],[com,comerce_out])

## escritura del arhivo de salida
writefile(output,height_input,diameter_input,firmness_input,coverage_input,sha_out,firm_out,cov_out,com_out)


print( "Presione enter para terminar... ")
input()
