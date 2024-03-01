#  python before checkpoint 5
# 31 - Project Requirements: Build FizzBuzz in Python

# So we're going to write a program that prints the numbers 
# from 1 to 100 but for multiples of 3 it prints Fizz. 
# So it prints a string of fizz instead of the number and 
# for the multiples of five it prints Buzz 
# for the numbers which are multiples of both 5 and 3 then 
# you're going to print out fizz buzz. And so just to give an idea of 
# what this is going to look like you're going to print out something 
# that is 1, 2, 3, 4, and 5. But instead of 
# where we have a number 3 right here, 
# this instead is going to be the string Fizz and 
# instead of the number 5 this is going to be Buzz.

# 1
# 2
# Fizz
# 4
# Buzz

# SOLUTION 1: WHAT IS ASKED
print('SOLUTION 1: WHAT IS ASKED')
def fizzbuzz(max_range):
    for num in range(1,max_range):
        if num % 3 == 0 and num % 5 == 0:
            print('FizzBuzz')
        elif num % 3 == 0:
            print('Fizz')
        elif num % 5 == 0:
            print('Buzz')
        else:
            print(num)

fizzbuzz(100)

# SOLUTION 1: EXTENSION TO CHECK OUT WHETHER IS RIGHT
print('SOLUTION 1: EXTENSION TO CHECK OUT WHETHER IS RIGHT')
def fizzbuzz_check(max_range):
    check_list_threefive = []
    check_list_three = []
    check_list_five = []
    check_list_others = []
    for num in range(1,max_range):
        if num % 3 == 0 and num % 5 == 0:
            check_list_threefive.append(num)
        elif num % 3 == 0:
            check_list_three.append(num)
        elif num % 5 == 0:
            check_list_five.append(num)
        else:
            check_list_others.append(num)
    
    check_dictionary = {
        '3-5': check_list_threefive,
        '3': check_list_three,
        '5': check_list_five,
        '!3-5': check_list_others
    }
    check_dictionary_log = {}
    for pos, lista in check_dictionary.items():
        guion = pos.find('-')
        output = True
        if guion<0:
            for value in lista:
                if value % int(pos) !=0:
                    output = False
        else:
            min_max = pos.split('-')    
            exclamacion = pos.find('!')
            if exclamacion <0:                 
                for value in lista:
                    if value % int(min_max[0]) !=0 and value % int(min_max[1]) !=0:
                        output = False     
            else:
                minimo = min_max[0].replace('!','')
                for value in lista:
                    if value % int(minimo) ==0 or value % int(min_max[1]) ==0:
                        output = False                                           
        check_dictionary_log[pos]=output           


    return check_dictionary_log

print(fizzbuzz_check(100))


# SOLUTION 2: WHAT IS ASKED + *ARGS
print('SOLUTION 2: WHAT IS ASKED + *ARGS')
def fizzbuzz(max_range, *args):
    for num in range(1,max_range):
        if num % int(args[0]) == 0 and num % int(args[1]) == 0:
            print('FizzBuzz')
        elif num % int(args[0]) == 0:
            print('Fizz')
        elif num % int(args[1]) == 0:
            print('Buzz')
        else:
            print(num)

fizzbuzz(100,
         3,5)

# SOLUTION 2: EXTENSION TO CHECK OUT WHETHER IS RIGHT + 2 FUNCTIONS
print('SOLUTION 2: EXTENSION TO CHECK OUT WHETHER IS RIGHT + 2 FUNCTIONS')
def fizzbuzz_check_pattern(max_range, *args):
    check_list_threefive = []
    check_list_three = []
    check_list_five = []
    check_list_others = []
    for num in range(1,max_range):
        if num % int(args[0]) == 0 and num % int(args[1]) == 0:
            check_list_threefive.append(num)
        elif num % int(args[0]) == 0:
            check_list_three.append(num)
        elif num % int(args[1]) == 0:
            check_list_five.append(num)
        else:
            check_list_others.append(num)
    
    intervalo = f'{str(args[0])}-{str(args[1])}'
    check_dictionary_pattern = {
        intervalo: check_list_threefive,
        args[0]: check_list_three,
        args[1]: check_list_five,
        '!' + str(intervalo): check_list_others
    }
    return check_dictionary_pattern

def fizzbuzz_check(check_dictionary):
    check_dictionary_log = {}
    for pos, lista in check_dictionary.items():
        guion = str(pos).find('-')
        output = True
        if guion<0:
            for value in lista:
                if value % int(pos) !=0:
                    output = False
        else:
            min_max = pos.split('-')     
            exclamacion = pos.find('!')
            if exclamacion <0:                 
                for value in lista:
                    if value % int(min_max[0]) !=0 and value % int(min_max[1]) !=0:
                        output = False     
            else:
                minimo = min_max[0].replace('!','')
                for value in lista:
                    if value % int(minimo) ==0 or value % int(min_max[1]) ==0:
                        output = False                                           
        check_dictionary_log[pos]=output           


    return check_dictionary_log


check_dictionary = fizzbuzz_check_pattern(100,
                                          3,5)
print('pattern function first: it returns the dictionary to check')
print(check_dictionary)

print(fizzbuzz_check(check_dictionary))