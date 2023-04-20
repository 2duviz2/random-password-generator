import random

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

a = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
times = input("Cuantos caracteres quieres? ")
alltext = "error!"
error = False

if times.isnumeric() == False:
    print("error!")
    error = True

if error == False:
    if int(times) > 9999:
        aceptar = input("HEY HEY HEY, eso son muchos numeros, podria haber un problema si lo ejecutas, deseas ponerlo a 9999? (N/Y) ")
        if aceptar == "Y" or aceptar == "y":
            times = "9999"
    if int(times) > 0:
        alltext = ""
    for i in range(int(times)):
        randomItem = random.choice(a)
        alltext = alltext + randomItem
    print(alltext)
