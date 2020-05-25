print("problema #1")
num1 = int(input("digite un numero: "))
num2 = int(input("digite el segundo numero: "))

suma = (num1+num2)

print("la suma de los nuemros es: ",suma)

print("Problema #2")
numero = int(input("¿Cuántos valores va a introd
if numero <= 0:
        print("¡Imposible!")
else:
        suma = 0
        for i in range(1, numero + 1):
            valor = float(input(f"Escriba el número {i}: "))
            suma = suma + valor
        print("La suma de los números que ha escrito es:",suma)
