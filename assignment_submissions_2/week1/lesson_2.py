#Q1: Create a function, that repeats the first 2 letters of a word,
#followed by 3 dots, a space after and the full name. The string should be ended with a question mark.

# def stutter(name):
#     name_stutter = (name[:2] + ('... '))*2
#     print(f'{name_stutter}{name}?')

# stutter('mariam')
# stutter('ayo')

# #Q2: Perform a for loop that searches through a string and prints only distinct vowel letters.

# def vowels(name):
#     for char in name.lower():
#         vowels= 'aeiou'
#         if char in vowels:
#             print(char)
#         else:
#             continue

# vowels('mariam')

# #Q3: Perform a while loop that requests for a name, if that name is entered, it will be printed,
# # else if user types “end” (this command should be case insensitive), the while loop is terminated

# your_name = input("type your name ").lower()
# while your_name != 'end':
#     print(your_name)
#     break
