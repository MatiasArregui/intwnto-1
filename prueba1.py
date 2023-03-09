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
    entrada1=int(input("Ingrese el valor a restar:\n"))
    entrada2=int(input("Ingrese el valor que restarara:\n"))
    resta3=entrada1-entrada2
    return resta3

def multiplicacion():
    Resultado=0
    valor1=int(input("Ingrese el valor a multiplicar:\n"))
    valor2=int(input("Ingrese el multiplicador:\n"))
    resultado=valor1*valor2
    return resultado
    
    




    
muestraMenu()
oper=operacion()
if oper == 2:
    print(suma())
if oper ==1:
    print(multiplicacion())
if oper ==3:
    print(resta())
if oper ==4:
    print()

