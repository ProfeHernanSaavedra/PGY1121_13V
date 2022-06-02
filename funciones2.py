def iva(precio):
  calculoIva = precio * 0.19
  print("El IVA es: ",calculoIva)

def calculoDcto(precio,descuento):
  descuento = (precio * descuento/100)
  return descuento

def calculoIMC(peso, estatura):
  imc = (peso/(estatura**2))
  print("Su IMC es: ",imc)
  if imc < 18.5:
    print("Bajo peso")
  else:
    if imc >18.5 and imc <= 24.9:
      print("Peso Adecuado")
    else:
      if imc >= 25 and imc <=29.9:
        print("Sobrepeso")
      else:
        if imc >= 30 and imc <= 34.9:
          print("Obesidad grado 1")
        else:
          if imc >=35 and imc <= 39.9:
            print("Obesidad grado 2") 
          else:
            if imc >=40:
              print("Obesidad grado 3")