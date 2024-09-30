# objeto = [[66,30], [60,50], [30,20], [40,40], [20,10] ]
# objeto1 = sorted(objeto, reverse=True)

# capacidad = 100
# ganancia = 0
# #debe dar 145
# print("'Mochila's problem con Fraccionamiento \n", objeto)

# for items in objeto1:
#   if items[1] <= capacidad:
#     print(items)
#     ganancia += items[0]
#     capacidad -= items[1]
#     print('La capacidad es: ',capacidad)
#   else:
#     ganancia = ganancia + (capacidad/items[1])*items[0]
#     break

# print('La ganancia: ',ganancia)

#AHORA LA INVERSA

# Da 156

# Da ya esta ordenado, tiene el valor completo y de segundo esta el peso

objeto = [[10,20], [20,30], [30,66], [40,40], [50,60] ]
objeto1 = objeto
print(objeto1)
capacidad = 100
ganancia = 0

print("'Mochila's problem con Fraccionamiento \n")

for items in objeto1:
  if items[0] <= capacidad:
    ganancia += items[1]
    capacidad -= items[0]
    print('La capacidad es: ',capacidad)
  else:
    ganancia = ganancia + (capacidad/items[0])*items[1]
    break

print('La ganancia: ',ganancia)

