nmk = input().split()

n = int(nmk[0]) # n copas
m = int(nmk[1]) # numero de huecos
k = int(nmk[2]) # numero de cambios

dic = {}
x = 1


holes = input().split() # posicion de los huecos


for i in range(0, m):
    dic.setdefault(int(holes[i]), 1) # lleno este diccionario con los huecos


for i in range(0, k):

    #if dic.get(x, 0):
    #    break

    uv = input().split() #posiciones de cambio
    u = int(uv[0])
    v = int(uv[1])


    if(dic.get(v) == 1 and x == u):
        x = v
        break

    if(dic.get(u) == 1 and x == v):
       x = u
       break

    if(u == x):
        x = v
        continue

    if(v == x):
       x = u


print(x)
