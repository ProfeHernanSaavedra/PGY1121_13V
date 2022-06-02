
import funciones2 as fn

op = 3
while op != 4:
  print("MENU")
  print("*"*5)
  print("1. Calcular IVA")
  print("2. Descuento")
  print("3. IMC")
  print("4. Salir")
  op = int(input("Por favor seleccione una opcion (1-4): "))
  if op == 1:
    precio = int(input("Ingrese precio del producto: "))
    fn.iva(precio)
  if op == 2:
    precio = int(input("Ingrese precio del producto: "))
    descuento = int(input("Ingrese el descuento (0-100): "))
    #decto = calculoDcto(precio,descuento)
    total = precio - fn.calculoDcto(precio,descuento)
    print("A pagar: $",total)
  if op == 3:
    peso = int(input("Ingrese su peso: "))
    estatura = float(input("Ingrese su estatura: "))
    fn.calculoIMC(peso,estatura)


