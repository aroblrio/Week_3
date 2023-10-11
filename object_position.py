H = float(input("Introduce la altura inicial: "))            #Pido al usuario la altura desde donde se lanza el objeto
t = float(input("Introduce el tiempo: "))                   #Pido al usuario en que instante quiere que se le calcule la posición
g = float(input("Introduce la gravedad del planeta: "))    #Pido al usuario en que planeta se encuentra para calcular la gravedad
#Aquí calculo la posicion del objeto en cualquier momento
X = H-(0.5*g*(t**2))
if (X<0):
    print("Ha atravesado el suelo, pruebe con otros valores")
else:
    print(X)