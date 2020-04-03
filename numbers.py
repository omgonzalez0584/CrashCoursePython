#imprimir numeros del 1 al millon con una lista

numbers = list(range(1,1000001))
#for number in numbers:
#    print(number)

#generar minimo
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# numeros impares
print("Odd numbers 1 to 20")
odd_numbers = list(range(1,20,2))
for odd in odd_numbers:
    print(odd)

#Lista con multiplos de 3
print("Multiplos de 3")
threes = list(range(3,30,3))
for i in threes:
    print(i)
    

#Cubos
print("Cubos del 1 al 10")
cubes = []
for cube in range(1,11):
    cubes.append(cube**3)

for cube in cubes:
    print(cube)


#usando list comprehension
cubes = [cube **3 for cube in range(1,11)]
print(cubes)



    



