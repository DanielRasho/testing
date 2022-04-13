#EJEMPLO LISTA TELEFONICA

# REQUERIMIENTOS:
## Necesito guardar el nombre de una persona con su telefono
## necesito consultar el nombre de una persona y mostrar su telefono
## Necesito modificar el nombre o telefono
## Necesito eliminar una persona

#Analisis y Disenio

## Datos
## un diccionario que utilize la llave numero y almacene el nombre
## variable nombre para que el agregue su nombre
## variable numero para que el agregue el numero
## utilizar variable numero como un id

## Disenio
## crear variables (diccionario y nombre, telefono)
## funcion para pedir datos
### ingresar variables (nombre, telefono)
### hacer validaciones de datos... (opcional)

### funciones para agregar, eliminar y buscar
### funcion agregar
#### preguntar si desea agregar y pedir datos y guardar en lista
### funcion eliminar
#### pedir numero de telefno a elimnar, buscar en lista y eliminar posicion en ambas listas
### funcion buscar
#### funcion buscar el nombre para obtener telefono

##Codigo
## variables
listaTelefonica = {}
nombre =''
telefono = ''

menu = True

def mostrarMenu():
    print("Bienvenido")
    print("Seleccione Opcion")
    print("1- Agregar")
    print("2- Eliminar")
    print("3- Buscar")
    print("4- Mostrar Lista")
    
def agregar(listaTelefonica):
    nombre = input("Agregar nombre: ")
    telefono = input("Agregar numero: ")
    
    if telefono in listaTelefonica:
        print('contacto existente')
    else:        
        listaTelefonica[telefono] = nombre;
    return listaTelefonica

def eliminar(listaTelefonica):
    telefono = input("Numero del contacto a eliminar:")

    if telefono in listaTelefonica:
        listaTelefonica.pop(telefono)
    else:
        print("Ese telefono no esta encontrado.")
    return listaTelefonica

def mostrar(listaTelefonica):
    for key in listaTelefonica:
        print( listaTelefonica[key], key )

def buscar(listaTelefonica):
    nombre = input("Agregar nombre: ")
    if nombre in listaTelefonica.values():
        print 

while menu:
    mostrarMenu()
    opcion = int(input("Ingrese respuesta: "))
    
    if opcion == 1:
        listaTelefonica = agregar(listaTelefonica)
    elif opcion == 2:
        listaTelefonica = eliminar(listaTelefonica)
    elif opcion == 3:
        print('buscar')
        listaTelefonica[numero]
    elif opcion == 4:
        mostrar(listaTelefonica)
    else:
        print("opcion no valida")
    


