def fibonacci():
    x = 1
    y = 1
    z = 0

    lista = [x,y]
    while len(str(z)) < 1000:
        z = x + y
        x = y
        y = z
        lista.append(z)


    print(len(lista))


fibonacci()