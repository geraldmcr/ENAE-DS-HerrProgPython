def is_prime (y): #esta función identifica si un numero es primo
  for x in range (2, y):
    if y%x == 0:
        result = False
        break
  if y == x + 1:
    result = True
  return result

contador = 0
last_prime = 1
next_number = 2
print(next_number)

while contador<72:# con este loop se identifican los 73° numeros primos
    next_number = next_number + 1
    if is_prime (next_number):
        contador = contador + 1
        last_prime = next_number
        print(last_prime)