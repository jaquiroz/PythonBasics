mylist = []

#El metodo append agrega valores a la cola de la lista
mylist.append(5)
mylist.append(27)
mylist.append(3)
mylist.append(12)
print("Metodo append: ",mylist)

# El metodo insert agrega un valor en el indice especifico
mylist.insert(1, 12)
print("Metodo insert: ",mylist)

#Cuenta la veces que se repite el dato asociado a la funcion
print("Metodo count: ",mylist.count(12))
print(mylist.count(5))

#Retorna la primera posicion del dato asociado en la list
print("Metodo index: ",mylist.index(3))

#Voltea las posicones de la list
mylist.reverse()
print("Metodo reverse: ",mylist)

#Ordena la list de menor a mayor
mylist.sort()
print("Metodo sort: ",mylist)

#Remove el dato asociado de la list
mylist.remove(5)
print("Metodo remove: ",mylist)

#Remueve y devuelve el valor de ultmo item en la list
lastitem = mylist.pop()
print("Metodo pop: ",lastitem)
print("Final list: ",mylist)
