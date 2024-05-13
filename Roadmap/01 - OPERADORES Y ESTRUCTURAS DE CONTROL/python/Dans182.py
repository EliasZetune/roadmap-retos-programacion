"""
* EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */
"""

# Operadores

## Operadores aritméticos

suma = 2 + 2
print("Suma: 2 + 2 =", suma)

resta = 2 - 2
print("Resta: 2 - 2 =", resta)

multiplicación = 2 * 2
print("Multiplicación: 2 * 2 =", multiplicación)

division = 2 / 2
print("Division: 2 / 2 =", division)

modulo = 10 % 3 #El resto de la división
print("Módulo: 10 % 3 =", modulo)

potencia = 10 ** 3
print("Exponente: 10 ** 3 =", potencia)

division_entera = 10 // 3 #El resultado nos tiene que dar un n1 redondeado, entero. Evita la parte decimal.
print("Division Entera: 10 / 3 =", division_entera)

## Operadores de comparación

print(f"Operador de igualdad: 10 == 3: {10 == 3}")
print(f"Operador de desigualdad: 10 != 3: {10 != 3}")
print(f"Mayor que: 10 > 3: {10 > 3}")
print(f"Menor que: 10 < 3: {10 < 3}")
print(f"Mayor o igual que: 10 >= 3: {10 >= 3}")
print(f"Menor o igual que : 10 <= 3: {10 <= 3}")

## Operadores lógicos

print(f"And &&: 10 > 3 and 8 < 19: {10 > 3 and 8 < 19}")
print(f"Or ||: 10 > 3 and 8 > 19: {10 > 3 or 8 > 19}")
print(f"NOT !: 10 + 3 = 14: {not 10 + 3 == 14}")

### Operadores de asignación

my_number = 18 #asignacion
print(my_number)

my_number += 1 #suma y asignacion
print(my_number)

my_number -= 1 #resta y asignacion
print(my_number)

my_number *= 1 #multiplicacion y asignacion
print(my_number)

my_number /= 1 #division y asignacion
print(my_number)

my_number %= 1 #modulo y asignacion
print(my_number)

my_number **= 1 #exponente y asignacion
print(my_number)

my_number //= 1 #division entera y asignacion
print(my_number)

### Operadores de identidad
#Los valores de identidad lo que buscan es comparar es el valor en memoria.
#Por eso dando el mismo valor, da false. Porque tienen direcciones en la memoria distintas
my_new_number = 0.0
print(my_number)
print(f"my_number is my_new_number es {my_number is my_new_number}")
print(f"my_new_number is my_new_number es {my_new_number is my_new_number}")

### Operadores de pertenencia
print(f" 'd' in 'dans182' = {'d' in 'dans182'}")
print(f" 'd' not in 'dans182' = {'d' not in 'dans182'}")

### Operadores bit a bit

### Operadores de pertenencia