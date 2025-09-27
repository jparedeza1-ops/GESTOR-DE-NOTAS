
# este es el inicio de mi documentacion en donde empece una lista 
materias=["matematicas", "biologia", "quimica" ,"ingles" ]
# en esta primera funcion le damos la bienvenida   a el user  
def menu ():
    print("Bienvenido al menu")
    print("˚˖𓍢🌷✧˚.🎀⋆"*30)
    print(f"seleccione la materia donde ingresara las notas")
    print("¿cuantas notas ingresara?")
    print("el promedio de las notas  fue")

    #en esta segunda funcion ingresaremos notas a las materia seleccionada por el user
def ingreso_de_nota():

    materia = input(f"seleccione la materia {materias}")
    if materia in materias:
        print("materia valida")
    else:
        print("no existe esta materia ahora")


    #en este bloque de codigo le indico al user que puede ingresar las notas que desea y si ingresa erronamente -1 nota le informo que debe ingresar una o mas de una
    #utilizo try para que el codigo pueda estar corriendo de una forma mas ordena segun mi criterio  
    try: 
        notas_solicitadas=int(input("Cuantas notas desea ingresar"))
        if notas_solicitadas <= 0:
            print("debes ingresar una o mas notas ")
            return ()
    
        Notas=[] #creo una lista en donde guardare las N cantidades de notas 
        # en esta ocacion utilizo for para poder tener el numero de veces que mi user solicita
        for i in range(notas_solicitadas):
            while True:
                try:
                    calificacion = float(input(f"Ingrese la calificación {i+1}: "))
                    Notas.append(calificacion)
                    break
                except ValueError:
                    print("Por favor ingrese un número válido para la calificación.")

        if Notas:
            promedio = sum(Notas) / len(Notas)
            print(f"La calificación promedio en la materia {materia} es {promedio:.2f}")
        else:
            print("No se insertó ninguna nota")
    except ValueError :
        print("Por favor, ingrese un numero valido para la cantidad de notas.")


def main():

    while True: #creo un bucle
        menu() #llamo a la funcion menu
          #utilizo try para manejar errores de entrada del usuario si selecciona una opcion no valida mostrare un mensaje de error y el menu se mostrara de nuevo
    
        try :
            opcion = int(input("presione 1 si quiere ingresar notas o presiona un numero diferente si quieres salir ")) #int para convertir la entrada del usuario a un numero entero de str a int
            if opcion == 1:
                ingreso_de_nota()#llamo a la funcion ingresar nota
            
                break #rompo el ciclo while si el usuario selecciona la opcion 4
            else:
                print("Opcion invalida. Por favor, seleccione una opcion del 1 al 4.")
        except ValueError: #valueerror es una clausula para manejar errores de valor si el usuario ingresa un valor no valido
            print("Por favor, ingrese un numero valido para la opcion.")
        
      


if __name__ == "__main__":
    main() #llamo a la funcion main para ejecutar el programa
