from funcs import suma

# Imprimir en la consola un mensaje de bienvenida
print("Hello World!")

# Numbers (integers, floats)
num = 3
# Strings
string = "Hola"
string_1 = "Hola Pancho"
# Booleans
bool = True
bool_1 = False
# Lists
list_1 = [1, 2, 3]
list_2 = ["Hola", 1, True]
# Dictionaries
dict = {
    "1": "Juanita",
    "2": "Pedro",
}
# if: Si pasa esta condición, entonces ejecuta el bloque de código (==, !=, >, <, >=, <=)
if num == 1:
    print("Es verdadero que es 1")
# elif: Si no pasa la condición anterior, pero pasa esta, entonces ejecuta el bloque de código
elif num == 2:
    print("Es verdadero que es 2")
# else: Si no pasa ninguna de las condiciones anteriores, entonces ejecuta el bloque de código
else:
    print("No es verdadero que sea 1 o 2")

# for: Itera sobre una lista, rango o diccionario
sum = 0
for number in list_1:
    sum += number
print(sum)

for i in range(1, 10):
    print(i)

# while: Mientras la condición sea verdadera, ejecuta el bloque de código
while num < 20:
    print(num)
    num += 1


# Funciones
def add_strings(string_1, string_2):
    return string_1 + string_2


string_3 = add_strings(string, string_1)
print(string_3)

if __name__ == "__main__":
    print("Este es el bloque principal del código")
