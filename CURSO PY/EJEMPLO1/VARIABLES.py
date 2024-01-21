'''#Esta es una practica solo

#Pedir números al usuario 

numero1 = int(input("Ingresa un número (1): " ))
numero2 = int(input("Ingresa un número (2): " ))

#Operaciones aritméticas 
print(f'La suma es: {numero1 + numero2}')
print(f'La multiplicación es: {numero1 * numero2}')

#Operaciones de comparación 
print(f'¿los números son iguales?: {numero1 == numero2}')
print(f'¿El primer número es menor que el segundo?: {numero1 < numero2}')
print(f'¿El segundo número es mayor o igual al primero?: {numero2 >= numero1}')'''


'''
Nombre= "Steven"
Apelli2= 'Perez'
Confirmacion="""Estoy Autorizando tratamiento de datos en Python"""
Edad= 40
Peso=80,5
Hijos= True
#print (Nombre + " " + Apelli2 + ", " + Confirmacion) #Es una manera de imprimir en pantalla
print(f'Esta persona tiene {Edad} años de edad y  su peso es de {Peso} kilos' #Esta es otra manera de imprimir en pantalla
)

thisset = (("Manzana", "Banana", "cereza", False, True, 0))
#print(thisset)
 
thisdict = {
  "Nombre ": "Mathias",
  "Edad": "6",
  "Hijo": True,
  "Peso": 12.2,}
i = thisdict["Hijo"]
x = thisdict.items()
print(x)
'''

'''#Solicitar información 

nombre = input("Ingrese el nombre del cliente: ")
valor_compra= float (input("Ingrese el valor de la compra: "))
#Establecer condiciones

if valor_compra <80:
     print(f'Hola, {nombre}. El valor a pagar es: $ {valor_Compra}')
elif 80<= valor_compra < 150:
      descuento=0.1
elif 150<= valor_compra <= 300:
      descuento=0.15
elif 300<= valor_compra < 500:
      descuento=0.2
      
precio_final=valor_compra - (valor_compra * descuento)
print(f'Compra sin descuento: {valor_compra} . \n Compra con descuento: {precio_final}')'''

'''def dolar(cantidad):
    vdolar=cantidad*3750
    return vdolar
total=dolar(10)
print(total)'''

def conversor (monedaActual,cantidad,monedaconv)
if monedaActual == "1":
            
            def dolar():
                  if monedaconv == "1":
                        print(f'{cantidad} dolares equivale a {cantidad*3750} pesos colombianos')
                  elif monedaconv == "2":
                        print(f'{cantidad} dolares equivale a {cantidad*6.37} yuanes')
                  elif monedaconv == "3":
                        print(f'{cantidad} dolares equivale a {cantidad*0.76} libras esterlinas')
                  else:
                        print("No se reconoce la moneda")
            dolar()
            
            if monedaActual== "2":
                  def euro():
                        if monedaconv == "1":
                              print(f'{cantidad} euro equivale a {cantidad*4000} pesos colombianos')
                        elif monedaconv == "2":
                              print(f'{cantidad} euro equivale a {cantidad*6.93} yuanes')
                        elif monedaconv == "3":
                              print(f'{cantidad} euro equivale a {cantidad*0.83} libras esterlinas')
            else:
                  print("No se reconoce la moneda")
            euro()
            
else:
              print("No se reconoce la moneda")
              
monedaActual=int(input("Ingrese la moneda a convertitir: \n 1. (Dolar) \n 2.(Euro) \n "))
cantidad=float(input("Ingresa Cantidad a convertir \n"))
monedaConv=int(input("Ingrese la moneda a cambio: \n 1. (Peso Colombiano) \n 2.(Yuenes) \n 3.(Libra Esterlina) \n"))