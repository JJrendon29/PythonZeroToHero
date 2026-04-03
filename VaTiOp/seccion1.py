''' Seccion 1: variables, tipos y operadores '''

'''

    #   Ejemplo 1: Variables basicas

        edad = 23   #Variable int (entero)
        nombre = "Juan" #Variable str (texto)
        altura = 1.80   #Variable float (decimal)
        es_estudiante = True    #Variable bool (verdadero/falso)

        forma de saber el tipo de cualquier variable:
            print(type(variable)) #Output: <class 'int'>

    #   Operadores 
        +   | 5 + 3   | 8
        -   | 10 - 4  | 6
        *   | 3 * 4   | 12
        /   | 10 / 2  | 5
        //  | 10 // 3 | 3
        %   | 10 % 3  | 1

    #   Concatenacion de Strigs 
        nombre = "Juan"
        edad = 23

        #   Forma 1: con +
            print("Mi nombre es" + nombre + "y tengo" + edad + "anios") #Output: Mi nombre es Juan y tengo 23 anios

        #   Forma 2: con f-strings
            print(f"Mi nombre es {nombre} y tengo {edad} anios") #Output: Mi nombre es Juan y tengo 23 anios

'''

""" EJERCICIOS """

valor = 100
cantidad = 5
total = valor * cantidad
print(total)

nombre = 'Juan'
apellido = 'Rodiguez'
print(f"Mi nombre completo es {nombre} {apellido}")

# 7 / 2 arrojara 3.5 que es la divicion normal, y 7 // 2 arrojara cuantas veces cabe 2 en el 7, pero solo completo lo cual dara 3



