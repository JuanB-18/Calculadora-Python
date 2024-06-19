#este es el archivo python donde trabajaremos de manera colaborativa
#hola
def sumar (num1,num2):
    resultado= num1+num2
    return resultado
def restar(num1,num2):
    resultado= num1-num2
    return resultado
def multiplicar(num1,num2):
    resultado= num1*num2
    return resultado
def dividir(num1,num2):
    resultado= num1/num2
    return resultado
while True:
    try:
        operacion=int(input("¿Que operacion desea realizar?\n1.-Sumar\n2.-Restar\n3.-Multiplicar\n4.-Dividir\n5.-Salir\n"))
    except ValueError as e:
        print("Seleccione correctamente")
        continue
    numero1=int(input("Ingrese un numero:\n"))
    numero2=int(input("Ingrese otro numero:\n"))
    if operacion == 1:
        print(sumar(numero1,numero2))
    elif operacion==2:
        print(restar(numero1,numero2))
    elif operacion==3:
        print(multiplicar(numero1,numero2))
    elif operacion == 4:
        print(dividir(numero1,numero2))
    print("chao")