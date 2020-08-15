
def writefile(output,height_input,diameter_input,firmness_input,coverage_input,shape_out,firmness_out,coverage_out,comerce_out):
    '''
    Funcion que crea un archivo y lo escribe (o sobreescribe) con todos los datos obtenidos despues del computo.

    :param output: int. Valor correspondiente a la salida dada por un calibre.

    :param height_input: int. Valor de Altura ingresado por el usuario.

    :param diameter_input: int. Valor de Diametro ingresado por el usuario.

    :param firmness_input: int. Valor de Firmeza ingresado por el usuario.

    :param coverage_input: int. Valor de Covertura ingresado por el usuario.

    :param shape_out: str. Texto correspondiente cual es la division de Forma dada por el valor
                                ingresado por el usuario.

    :param firmness_out: str. Texto correspondiente cual es la division de Firmeza dada por el valor
                                ingresado por el usuario.

    :param coverage_out: str. Texto correspondiente cual es la division de Covertura dada por el valor
                                ingresado por el usuario.
                                
    :param comerce_out: str. Texto correspondiente cual es la division de Exportacion dada por el valor
                                computado. 
    

    '''
    f= open("Cereza_"+str(height_input)+"_"+str(diameter_input)+"_"+str(firmness_input)+"_"+str(coverage_input)+".txt","w")

    f.write("Niveles capturados:\n")
    f.write("\tCalibre: "+str(diameter_input)+"mm \n")
    f.write("\tForma: "+shape_out+"\n")
    f.write("\tFirmeza de la pulpa: "+firmness_out+"\n")
    f.write("\tCobertura de manchas: "+coverage_out+"\n")
    f.write("Comercialización: "+comerce_out+"\n")
    f.write("Número salida: "+str(output)+"\n")
    f.close()