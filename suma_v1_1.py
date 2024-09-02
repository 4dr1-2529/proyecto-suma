def ingresoNumeros():

numero1= float (input("ingese sumando uno:  "))
numero2= float (input("ingese sumando dos:  "))
    return numero1,numero2
def suma(numero1,numero2):
   return  numero1+numero2

num1,num2, = ingresoNumeros()
    print(f"{numero1} +{numero2} = {suma}")

if __name__ == '__main__ ':
    num1, num2, = ingresoNumeros()
    print(f"{numero1} +{numero2} = {suma}")