from operacionesarimeticas import pythonProject1
if __name__ == '__main__ ':
    operacion = OperacionesArimeticas():
    num1, num2 = operacion.ingresoNumeros()
    print(f"{num1} +{num2} = {suma} = {operacion.suma(num1, num2)}")