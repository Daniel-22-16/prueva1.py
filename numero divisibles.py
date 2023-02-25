# realizando l ejercicio 
A = int(input("ingrese el limite inferior del rango ")) #10
C = int(input("ingrese el limite superior del rango ")) #55
vector = []

for i in range (A,C, 1):
    if i % 2 == 0 and i % 5 == 0: 
        vector.append(i)
print(f"vector números divisibles entre 2 y 5 en un rango {A} , {C} ->{vector}")
 
 
 
 #"""vector = [numero for numeo in range (A, C, 2 ) if numero % 2 == 0 and numero  % 5 == 0]"""
