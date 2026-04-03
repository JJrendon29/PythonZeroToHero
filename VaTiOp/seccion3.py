''' Seccion 3: Listas(lists) '''

'''
    #   Crear y accedeer a listas

        nombres = ["Juan","Maria","Pedro"]

        print(nombres[0]) #Output: Juan
        print(nombres[1]) #Output: Maria
        print(nombres[2]) #Output: Pedro
        
    #   Metodos de lista
        append  | Agregar al final
        insert  | Agregar posicion especifica
        remove  | eliminar
        len     | obtener longitud
        
       #   Ejemplos
            lista[1,2,3]

           lista.append(4)
            print(lista) #Output: [1,2,3,4]

            lista.insert(1,10)
            print(lista) #Output: [1,10,2,3,4]

            lista.remove(10)
            print(lista) #Output: [1,2,3,4]
                
            print(len(lista)) #Output: 4
            
'''

""" EJERCICIOS """

lista_num = [1,2,3,4,5]
print(lista_num[0])
print(lista_num[-1])
print(len(lista_num))

lista_fru = ["Mango"]

lista_fru.append("Manzana")
lista_fru.insert(0,"Naranja")
lista_fru.remove("Manzana")
print(lista_fru)

# append() inserta en el ultimo lugar la lista, e insert() es para insertar en un lugar especifico