#act.1
print ("Hola Mundo ")


#act.2
saludo="Hola mi nombre es Luis"
#act.3
x=5
y=6
print(x+y)


#act.4
a=18
b=2
suma=a+b
print(suma)


#act.5
print("Hola,¿Cual es tu nombre?")
nombre=str(input("Ingresar nombre:"))
print(str(nombre)+",mucho gusto.")


#act.6
print("Programa que calcula el area de un triangulo\n")

base=float(input("Ingresar base del triangulo:\n"))
altura=float(input("Ingresar la altura del triangulo:\n"))

if(base>0 and altura>0):
  area=(base*altura)/2
  print("El area es:"+str(area))
else:
  print("Ingresa medidas validas")