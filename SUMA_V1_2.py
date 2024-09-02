class OperacionesArimeticas():
    def ingresoNumeros(self):

        numero1= float (input("ingese sumando uno:  "))
        numero2= float (input("ingese sumando dos:  "))
        return numero1,numero2
    def suma(self,numero1,numero2):
       return  self,numero1+numero2

    if __name__ == '__main__ ':
        operacion = OperacionesArimeticas():
        num1, num2 = operacion.ingresoNumeros()
        print(f"{num1} +{num2} = {suma} = {operacion.suma(num1, num2)}")