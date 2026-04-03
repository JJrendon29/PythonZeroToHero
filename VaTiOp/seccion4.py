''' Seccion 4: Loops: for y while '''

'''

    #   for loop

        for i in range(5):
            print(i)
        
            # Output: 0
            # Output: 1
            # Output: 2 
            # Output: 3
            # Output: 4

        #   for elemento in lista
            frutas = ["Manzana","Platano","Naranja"]

            for fruta in frutas:
                print(f"La fruta es {fruta}")

    #   while loop

        contador = 0
        
        while contador < 3:
            print(contador)
            contador += 1

            # Output: 0
            # Output: 1
            # Output: 2

'''

""" EJERCICIOS """

for i in range(10):
    print(i + 1)

nombres = ["Juan","Jose","Cata","Lupe"]
for nombre in nombres:
    print(nombre)

contador = 1
while contador < 6:
    print(contador)
    contador += 1