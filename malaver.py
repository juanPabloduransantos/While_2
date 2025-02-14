# input
h = float(input("Introducir valor: "))

s = h / 5  # El valor límite es 1/5 de la altura inicial

saltos = 0  # Inicializar contador de saltos
valor_caida = h  # Inicializar valor de la caída con la altura inicial

# Bucle while para calcular los rebotes
while valor_caida >= s:
    saltos += 1  # Incrementar contador de rebotes
    valor_caida *= 0.9  # Reducir la altura en un 10%
    print(saltos)  # Imprimir el número de rebotes

# Imprimir el resultado final
print("La pelota no alcanzó la 5ª parte de la altura inicial después de", saltos, "rebotes.")