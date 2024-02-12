# Exercise 1: Create a string, number, list, and boolean, each stored in their own variable.
variable_string = "Books are a good choice"
variable_number = 3
variable_list = ['The Lord of the rings', 'Ulises' ,'1984']
variable_boolean = True
print('Exercise 1')
print(variable_string)
print(variable_number)
print(variable_list)
print(variable_boolean)

# Exercise 2: Use an index to grab the first 3 letters in your string, store that in a variable. 
three_letters = variable_string[0:3]
print('Exercise 2')
print(three_letters)

# Exercise 3: Use an index to grab the first element from your list.
list_first_element = variable_list[0]
print('Exercise 3')
print(list_first_element)

# Exercise 4: Create a new number variable that adds 10 to your original number.
variable_new_number = variable_number + 10
print('Exercise 4')
print(variable_new_number)

# Exercise 5: Use an index to get the last element in your list.
list_last_element = variable_list[-1]
print('Exercise 5')
print(list_last_element)

# Exercise 6: Use split to transform the following string into a list.
# 	names = 'harry,alex,susie,jared,gail,conner'
names = 'harry,alex,susie,jared,gail,conner'
names_list = names.split(",")
print('Exercise 6')
print(names_list)

# Exercise 7: Get the first word from your string using indexes. Use the upper function to transform the letters into uppercase. Create a new string that takes the uppercase word and the rest of the original string.
string_first_word = variable_string[0:5].upper()
new_string = string_first_word + variable_string[5:]
print('Exercise 7')
print(new_string)

# Exercise 8: Use string interpolation to print out a sentence that contains your number variable.
interpolation_example = f'''
    Reading {variable_number} books a week is very good
    '''
print('Exercise 8')
print(interpolation_example)

# Exercise 9: Print “hello world”.
print('Exercise 9')
print('“hello world”')
print('hello world') # In case is misunderstood