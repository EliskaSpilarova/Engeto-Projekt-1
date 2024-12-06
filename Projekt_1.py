"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Eliška Špilarová
email: eliska.spilarova@gmail.com
discord: eliska_spilarova
"""
# Creating a dictionary with usernames and passwords
list_usernames_passwords = {
    "bob": "123", 
    "ann": "pass123", 
    "mike": "password123", 
    "liz": "pass123"}

while True:
    username = input("username: " )
    password = input("password: ")
    print(40 * "-")

# Checking whether the data from the user correspond with any registered user
    if username in list_usernames_passwords and list_usernames_passwords[username] == password:
        print(f"Welcome to the app, {username}\nWe have 3 texts to be analyzed.")
        break
    elif username in list_usernames_passwords:
        print("Incorrect password. Please try again.")
    else:
        print("Unregistered user, terminating the program.")
        exit()
       
print(40 * "-")

# Asking the user to enter a number
text_choice = input("Enter a number btw. 1 and 3 to select: ")

# Verifying whether the input is a number
if not text_choice.isdigit():
    print("Invalid input. The program is terminating.")  
    exit()

# Verifying whether the number is 1, 2, or 3
if int(text_choice) not in [1, 2, 3]:
    print("The number is out of range. The program is terminating.")  
    exit()

#Texts
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# Choosing a text
selected_text = TEXTS[int(text_choice) - 1]
words = selected_text.split()

# Counters
word_count = 0
title_case_count = 0
uppercase_count = 0
lowercase_count = 0
number_count = 0
number_sum = 0
word_lengths = {}

# Analysing the text
for word in words:
    cleaned_word = word.strip(".,!?")
    word_count += 1
    
    if cleaned_word.istitle():
        title_case_count += 1
    elif cleaned_word.isupper():
        uppercase_count += 1
    elif cleaned_word.islower():
        lowercase_count += 1
    elif cleaned_word.isdigit():
        number_count += 1
        number_sum += int(cleaned_word)
    
    word_length = len(cleaned_word)
    if word_length > 0:
        if word_length not in word_lengths:
            word_lengths[word_length] = 1
        else:
            word_lengths[word_length] += 1

# Analysis results
print("-" * 40)
print(f"There are {word_count} words in the selected text.")
print(f"There are {title_case_count} titlecase words.")
print(f"There are {uppercase_count} uppercase words.")
print(f"There are {lowercase_count} lowercase words.")
print(f"There are {number_count} numeric strings.")
print(f"The sum of all numbers {number_sum}")
print("-" * 40)

# Printing the chart
print("LEN | OCCURRENCES | NR.")
print("-" * 40)
for length in sorted(word_lengths):
    occurrences = word_lengths[length]
    stars = '*' * occurrences
    print(f"{length:>3} |{stars:<13}|{occurrences:>2}")