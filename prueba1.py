# hola gente
def muestraMenu():
    print("Bienenido, la siguiente es una calculadora basica por medio de python")
    print("Ingrese la operacion:\n1) Multiplicacion\n2) Suma\n3) Resta\n4) Division")

def operacion():
    entrada=int(input(""))
    return entrada

def suma():
    suma=0
    while True:
        entrada=int(input("Ingrese el valor a sumar:\n"))
        if entrada != 00:
            suma+=entrada
        else:
            break
    if suma>=0:
        return suma
    else:
        cadena="la suma es menor a cero"
        return cadena

def resta():
    resta1=resta2=0
    entrada=int(input("Ingrese el primer valor:\n"))
    resta= entrada
    entrada=int(input("Ingrese el primer valor:\n"))
    resta2=entrada
    resta3=resta1-resta2
    return resta3

    
    




    
muestraMenu()
oper=operacion()
if oper == 2:
    print(suma())
if oper ==1:
    print()
if oper ==3:
    print(resta())
if oper ==4:
    print()

