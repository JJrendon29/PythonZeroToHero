''' Seccion 2: control de flujo: if, elif, else '''

'''

    #   Operadores de comparacion
        ==  | Igual     | 5 == 5
        !=  | No igual  | 5 != 3
        >   | Mayor que | 5 > 3
        <   | Menor que | 3 < 5
        >=  | Mayor o igual | 5 >= 5
        <=  | Menor o igual | 3 <= 5

    #   Estructura if/elif/else

        #   Ejemplos:
            edad = 23

            #   Estructura basica: if-else
                if edad >= 18:
                    print("Eres mayor de edad")
                else:
                    print("Eres menor de edad")

            #   Estructura: if-elif-else
                if edad < 13:
                    print("Eres un ninio")
                elif edad < 18:
                    print("Eres un adolecente")
                else:
                    print("Eres un adulto")
    
                
    #   Operadores logicos
        and  | Cumplir ambas condiciones
        or   | Cumplir una condicion

        #   Ejemplos:
                edad = 23
                tiene_licencia = True

                if edad >= 18 and tiene_licencia:
                    print("Puedes conducir")

                if edad < 13 or fin_de_semana:
                    print("A jugar")

'''

""" EJERCICIOS """

edad = 15
if edad >= 18:
    print("Puedes votar")
else:
    print("Aun no puedes votar")

numero = 10
if numero % 2 == 0:
    print("Numero par")
else:
    print("Numero impar")

calificacion = 3.0
aprobado = True
if calificacion >= 3 and aprobado:
    print("Aprobaste el curso")
else:
    print("No aprobaste")
