while True:
    numero = int(input("Ingrese un número: "))
    
    if numero == 10:
        break
    print(numero)
    
    
for numero in range(100):
    
    if numero == 10:
        break
    
    print(numero, end=" ")
    
for numero in range(100):
    
    if numero % 2 == 0:
        continue
    
    print(numero, end=" ")