"""
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""
num = 0

"""
while num <= 100:
    num+=1

    if num % 3 == 0:
        print(f"{num} fizz")
    if num % 5 == 0:
        print(f"{num} buzz")
    if num % 3 == 0 and num % 5 == 0:
        print(f"{num} fizzbuzz")
"""

for num in range(100):
    if num % 3 == 0 and num % 5 == 0:
        print(f"{num} - fizzbuzz")
    elif num % 3 == 0:
       print(f"{num} - izz")
    elif num % 5 == 0:
        print(f"{num} - buzz")
    else:
        print(num)