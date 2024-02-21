# Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.
print ('Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.')
list_ejemplo = ['Noticias', 'News', 'Breaking news']
tuple_ejemplo =('Noticias_tuple', 'News_tuple', 'Breaking news_tuple')
float_ejemplo = 10.25
integer_ejemplo = 10
decimal_ejemplo = 10.24999999999
dictionary_ejemplo = {
    'Madrid' : 'La Cibeles',
    'London' : 'Picadilly Circus',
    'Paris' : 'Montmartre'
}

print(list_ejemplo)
print(tuple_ejemplo)
print(float_ejemplo)
print(integer_ejemplo)
print(decimal_ejemplo)
print(dictionary_ejemplo)

# Exercise 2: Round your float up.
print ('Exercise 2: Round your float up.')
import math
float_ejemplo_up_rounded = math.ceil(float_ejemplo)
print(float_ejemplo_up_rounded)

# Exercise 3: Get the square root of your float.
print ('Exercise 3: Get the square root of your float.')
float_ejemplo_square_root = math.sqrt(float_ejemplo)
print(float_ejemplo_square_root)

# Exercise 4: Select the first element from your dictionary.
print ('Exercise 4: Select the first element from your dictionary.')
# 'A palo seco sería esto de abajo, pero si no sabemos el valor lo hacemos por claves
# dictionary_ejemplo_first = dictionary_ejemplo['Madrid']
key_value = list(dictionary_ejemplo.keys())[0]
dictionary_ejemplo_first = dictionary_ejemplo[key_value]
print(dictionary_ejemplo_first)
# también podría haber empleado la función get
print ('Exercise 4 - Using get function')
dictionary_ejemplo_first_get = dictionary_ejemplo.get(key_value, 'Not found')
print(dictionary_ejemplo_first)

# Exercise 5: Select the second element from your tuple.
print ('Exercise 5: Select the second element from your tuple.')
tuple_ejemplo_second_element = tuple_ejemplo[1]
print(tuple_ejemplo_second_element)

# Exercise 6: Add an element to the end of your list.
print ('Exercise 6: Add an element to the end of your list.')
# list_ejemplo = list_ejemplo + ['TV24h']
# print(list_ejemplo)
# or, using append
list_ejemplo.append('TV24h')
print(list_ejemplo)
# or, using extend
# list_ejemplo.extend(['TV24h'])
# print(list_ejemplo)

# Exercise 7: Replace the first element in your list.
print ('Exercise 7: Replace the first element in your list.')
list_ejemplo[0] ='New data'
print(list_ejemplo)

# Exercise 8: Sort your list alphabetically.
print ('Exercise 8: Sort your list alphabetically.')
list_ejemplo.sort()
print(list_ejemplo)

# Exercise 9: Use reassignment to add an element to your tuple.
print ('Exercise 9: Use reassignment to add an element to your tuple.')
tuple_ejemplo += ('This is the end',)
print(tuple_ejemplo)