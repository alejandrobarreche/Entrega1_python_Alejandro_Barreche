import random

al = random.randint(0,100)

num = int(input("Dime un numero del 0 al 99 incluidos: "))
while (num < 0) or (num > 99):
    print("Este número no sirve")
    num = int(input("Vuelve a decirme un número, pero esta vez que esté entre 0 y 99 incluidos: "))

i = 1
while True:
    if al < num:
        print("¡Demasiado alto!")
        print("Tu número,", num, "está por encima del que yo estaba pensando")
        
    elif al > num:
        print("¡Demasiado bajo!")
        print("Tu número,", num, "está por debajo del que yo estaba pensando")
        
    elif num == al:
        print("¡Enhorabuena! El número que estaba pensando era el", num)
        print("Número de intentos: ", i)
        break
    
    print("Número de intentos: ", i)
    num = int(input("Vuelve a decirme un número que esté entre 0 y 99 incluidos: "))
    i = i+1
