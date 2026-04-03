''' Seccion 5: Funciones '''

'''

    #   Estructura basica
        
        def saludar():
            print("Hola Mundo")

        saludar()
        saludar()

    #   Funciones con parametro

        def saludar(nombre):
            print(f"Hola {nombre}")

        saludar("Juan") #Output: Hola Juan
        saludar("Maria") #Output: Hola Maria
    
    #   Funciones con return

        def suma(a,b):
            resultado = a + b
            return resultado
        
        total = suma(5,3)
        print(total)

'''

""" EJERCICIOS """

def multiplicar(a,b):
    resultado = a * b
    return resultado 
total = multiplicar(3,5)
print(total)

def es_mayor_de_edad(edad):
    if edad[0] >= 18:
        return True
    else:
        return False
print(es_mayor_de_edad(18))

def sumar_lista_for(lista):
    total = 0
    for numero in lista:
        total += numero
    return total
print(sumar_lista_for(lista=[2,3,5]))