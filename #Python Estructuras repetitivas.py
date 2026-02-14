#Python Estructuras repetitivas

#Suma de los primeros N números
# Pedir el numero al usuario
n = int(input("¿Hasta qué número quieres sumar?: "))
suma_total = 0

# Hacemos el ciclo sumando cada numero
for i in range(1, n + 1):
    suma_total = suma_total + i

print("El resultado de la suma es:", suma_total)


# El factorial se multiplica, por eso empezamos en 1
num = int(input("Dame un número para sacar su factorial: "))
res = 1

for x in range(1, num + 1):
    res = res * x

print("El factorial de", num, "es:", res)


#Tabla de multiplicar

n_tabla = int(input("¿Qué tabla de multiplicar quieres ver?: "))

print("--- Tabla del", n_tabla, "---")
for i in range(1, 11):
    # Imprimimos directo la multiplicacion
    print(n_tabla, "x", i, "=", n_tabla * i)

sumita = 0
cuantas = 0

print("Ve poniendo las notas. Si quieres terminar, pon un -1")

for i in range(100): # Ponemos 100 por si son muchos alumnos
    calif = float(input("Nota: "))
    
    if calif < 0:
        break # Si es negativo, se sale del ciclo


#Promedio de notas     
    sumita = sumita + calif
    cuantas = cuantas + 1

if cuantas > 0:
    promedio = sumita / cuantas
    print("El promedio final es de:", promedio)


#Potencia
b = int(input("Dime la base: "))
e = int(input("Dime el exponente: "))
total = 1
10
# Multiplicamos la base la cantidad de veces que diga el exponente
for i in range(e):
    total = total * b

print("El resultado de la potencia es:", total)

#Suma de pares en rango

inicio = int(input("Pon el primer número (A): "))
fin = int(input("Pon el segundo número (B): "))
acumulado = 0

for n in range(inicio, fin + 1):
    # Si el residuo de dividir entre 2 es 0, es par
    if n % 2 == 0:
        acumulado = acumulado + n

print("La suma de todos los pares es:", acumulado)