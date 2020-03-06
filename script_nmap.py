import os 



def creacion(lectura):
    ruta = "Creados/"
    nombre = raw_input("\n ESCRIBE EL NOMBRE DEL ARCHIVO: ")
    formato = ".txt"
    archivo = ruta + nombre + formato
    escritura = open(archivo, "w")
    escritura.writelines(lectura)
    escritura.close()
    os.system("color 7")  # Opcionar para retorna al color original >:V
    print "\n\n----------------- ARCHIVO CREADO CON EXITO. --------------------" # Esta correcto aunque aparesca el punto gordo.


def ejecucion():
    comando = "nmap "
    ip = raw_input(" INGRESE LA IP: ")
    concatenar = comando + ip
    os.system(concatenar)  # Este es opcional para que se muestre tambien en consola :v 
    conducto = os.popen(concatenar) # de la misma familia (tuvo) de os.system, pero este no muestra en la consola.
    lectura = conducto.readlines()
    creacion(lectura)



os.system("cls")  # Opcional para limpiar consola
os.system("color 4")  # Opcional para cambio de color de la consola :V
print "\n [[[[[[[[[[[[[[[[ ARCHIVO DE PUERTOS ESCANEADOS ]]]]]]]]]]]]]]]]\n"

ejecucion()
