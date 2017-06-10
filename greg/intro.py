
# This is the print statement

print("Hello world")

# This is a variable

message = "Level Two"

print(message)

# The variable above is called a string
# You can use single or double quotes (but must close them)
# You can ask Python what type a variable is. Try uncommenting the next line:
 print(type(message))


# Integer (a whole number)
a = 123
b = 654
c = a + b

# Try printing the value of c below to see the answer
print(c)

# 5. You can use other operators like subtract (-) and multiply (*)
# Try some below by replacing the word with the correct operator

# a times b
# b minus a
# 12 times 4
# 103 add 999

# GO!

# 6. Variables keep their value until you change it

a = 100
# print(a)  # think - should this be 123 or 100?

c = 50
# print(c)  # think - should this be 50 or 777?

d = 10 + a - c
# print(d)  # think - what should this be now?

# GO!

# You can also use '+' to add together two strings

greeting = 'Hi '
name = ''  # enter your name in this string

message = greeting + name
# print(message)

# GO!

#T ry adding a number and a string together and you get an error:

age = 16


print(name + ' is ' + age + ' years old')
# See the error? You can't mix types like that.
# But see how it tells you which line was the error?
#
# Now comment out that line so there is no error

# We can convert numbers to strings like this:

print(name + ' is ' + str(age) + ' years old')



# Another variable type is called a boolean
# This means either True or False

raspberry_pi_is_fun = True
raspberry_pi_is_expensive = False

# We can also compare two variables using ==

bobs_age = 15
your_age =  28

print(your_age == bobs_age)  # this prints either True or False

# We can use less than and greater than too - these are < and >

bob_is_older = bobs_age > your_age

print(bob_is_older)  # do you expect True or False?


# We can ask questions before printing with an if statement

money = 500
phone_cost = 200
tablet_cost = 200

total_cost = phone_cost + tablet_cost
can_afford_both = money > total_cost

if can_afford_both:
    message = "You have enough money for both"
else:
    message = "You can't afford both devices"

print(message)  # what do you expect to see here?


raspberry_pi = 25
pies = 3 * raspberry_pi

total_cost = total_cost + pies

if total_cost <= money:
    message = "You have enough money for 3 raspberry pies as well"
else:
    message = "You can't afford 3 raspberry pies"

print(message)  # what do you expect to see here?

# You can keep many items in a type of variable called a list

colours = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']

# You can check whether a colour is in the list

print('Black' in colours)  # Prints True or False

# You can add to the list with append
colours.append('Black')
colours.append('White')

print('Black' in colours)  # Should this be different now?

# You can add a list to a list with extend

more_colours = ['Gray', 'Navy', 'Pink']

colours.extend(more_colours)

print(colours)

# You can add two lists together in to a new list using +

primary_colours = ['Red', 'Blue', 'Yellow']
secondary_colours = ['Purple', 'Orange', 'Green']

main_colours = primary_colours + secondary_colours

print(main_colours)

# You can find how many there are by using len(your_list). Try it below
print(len(main_colours))

all_colours = colours + main_colours

# How many colours are there in all_colours?
#
# 16. You can make sure you don't have duplicates by adding to a set

even_numbers = [2, 4, 6, 8, 10, 12]
multiples_of_three = [3, 6, 9, 12]

numbers = even_numbers + multiples_of_three
print(numbers, len(numbers))
numbers_set = set(numbers)
print(numbers_set, len(numbers_set))

colour_set = set(all_colours)

# You can use a loop to look over all the items in a list

my_class = ['Sarah', 'Bob', 'Jim', 'Tom', 'Lucy', 'Sophie', 'Liz', 'Ed']

# Below is a multi-line comment
# Delete the ''' from before and after to uncomment the block

'''
for student in my_class:
    print(student)
'''


full_name = 'Dominic Adrian Smith'

first_letter = full_name[0]
last_letter = full_name[19]
first_three = full_name[:3]  # [0:3 also works]
last_three = full_name[-3:]  # [17:] and [17:20] also work
middle = full_name[8:14]

# Try printing these, and try to make a word out of the individual letters

# 19. You can also split the string on a specific character

my_sentence = "Hello, my name is Fred"
parts = my_sentence.split(',')

print(parts)
# print(type(parts))  # What type is this variable? What can you do with it?

my_long_sentence = "This is a very very very very very very long sentence"

# Now split the sentence and use this to print out the number of words

# GO! (Clues below if you're stuck)

# Clue: Which character do you split on to separate words?
# Clue: What type is the split variable?
# Clue: What can you do to count these?

# 20. You can group data together in a tuple

person = ('Bobby', 26)

# print(person[0] + ' is ' + str(person[1]) + ' years old')

# GO!

# (name, age)
students = [
    ('Dave', 12),
    ('Sophia', 13),
    ('Sam', 12),
    ('Kate', 11),
    ('Daniel', 10)
]

# Now write a loop to print each of the students' names and age

# GO!

# 21. Tuples can be any length. The above examples are 2-tuples.

# Try making a list of students with (name, age, favourite subject and sport)

# Now loop over them printing each one out

# Now pick a number (in the students' age range)
# Make the loop only print the students older than that number

# GO!

# 22. Another useful data structure is a dictionary

# Dictionaries contain key-value pairs like an address book maps name
# to number

addresses = {
    'Lauren': '0161 5673 890',
    'Amy': '0115 8901 165',
    'Daniel': '0114 2290 542',
    'Emergency': '999'
}

# You access dictionary elements by looking them up with the key:

# print(addresses['Amy'])

# You can check if a key or value exists in a given dictionary:

# print('David' in addresses)  # [False]
# print('Daniel' in addresses)  # [True]
# print('999' in addresses)  # [False]
# print('999' in addresses.values())  # [True]
# print(999 in addresses.values())  # [False]

# GO!

# Note that 999 was entered in to the dictionary as a string, not an integer

# Think: what would happen if phone numbers were stored as integers?

# Try changing Amy's phone number to a new number

# addresses['Amy'] = '0115 236 359'
# print(addresses['Amy'])

# GO!

# Delete Daniel from the dictinary

# print('Daniel' in addresses)  # [True]
# del addresses['Daniel']
# print('Daniel' in addresses)  # [False]

# GO!

# You can also loop over a dictionary and access its contents:

'''
for name in addresses:
    print(name, addresses[name])
'''

# GO!

# 23. A final challenge using the skills you've learned:
# What is the sum of all the digits in all the numbers from 1 to 1000?

# GO!

# Clue: range(10) => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Clue: str(87) => '87'
# Clue: int('9') => 9
