import random

# print('''HANGMAN
# The game will be available soon
# ''')
#
# print('''HANGMAN
# Guess the word:
# ''')
# user_input = input()
# if user_input == "python": print("You survived!")
#
# else: print("You lost!")
#
# library = ["python","java","javascript","php"]
# word = random.choice(library)
# print('''HANGMAN
# Guess the word:
# ''')
# user_input = input()
# if user_input == word: print("You survived!")
#
# else: print("You lost!")
#
# library = ["python","java","javascript","php"]
# word = random.choice(library)
# help = word[0:3] + "-"*(len(word)-3)
# print(f'''HANGMAN
# Guess the word:{help}
# ''')
# user_input = input()
# if user_input == word: print("You survived!")
#
# else: print("You lost!")
#
# library = ["python","java","javascript","php"]
# word = random.choice(library)
# help = ["-"]*len(word)
# lives = 8
# while lives > 0:
#
#     print(f'''HANGMAN
#     Guess the word:{"".join(help)}
#     ''')
#     user_input = input()
#     if user_input in word:
#         for i in range(0,len(word)):
#             if user_input == word[i]:
#                 help[i] = user_input
#     else: print("The letter doesn't appear in the word")
#     lives -=1
# print('''
# Thanks for playing!
# We'll see how well you did in the next stage
# ''')

# library = ["python","java","javascript","php"]
# letters = []
# word = random.choice(library)
# help = ["-"]*len(word)
# lives = 8
# while True:
#
#     print(f'''HANGMAN
#     Guess the word:{"".join(help)}
#     ''')
#     user_input = input()
#     if user_input in letters:
#         print("No improvements")
#         lives -= 1
#         if lives == 0:
#             print("You lost")
#             break
#         continue
#     if user_input in word:
#         for i in range(0,len(word)):
#             if user_input == word[i]:
#                 help[i] = user_input
#         if "-" not in help:
#             print("You won")
#             break
#     else:
#         print("The letter doesn't appear in the word")
#         lives -=1
#         if lives == 0:
#             print("You lost")
#             break
#     letters.append(user_input)
#
# print('''
# Thanks for playing!
# We'll see how well you did in the next stage
# ''')

# library = ["python","java","javascript","php"]
# letters = []
# word = random.choice(library)
# help = ["-"]*len(word)
# lives = 8
# while True:
#
#     print(f'''HANGMAN
#     Guess the word:{"".join(help)}
#     ''')
#     user_input = input()
#     if len(user_input) >1:
#         print("You should input a single letter.")
#         continue
#     if user_input <"a" or user_input >"z":
#         print("Please enter a lowercase English letter.")
#         continue
#     if user_input in letters:
#         print("You've already guessed this letter.")
#         continue
#     if user_input in word:
#         for i in range(0,len(word)):
#             if user_input == word[i]:
#                 help[i] = user_input
#         if "-" not in help:
#             print("You won")
#             break
#     else:
#         print("The letter doesn't appear in the word")
#         lives -=1
#         if lives == 0:
#             print("You lost")
#             break
#     letters.append(user_input)
#
# print('''
# Thanks for playing!
# We'll see how well you did in the next stage
# ''')

library = ["python","java","javascript","php"]
letters = []
while True:
    print('Type "play" to play the game, "exit" to quit:')
    user_input = input()
    while user_input != "play" and user_input != "exit":
        continue
    if user_input == "exit":
        break
    else:
        word = random.choice(library)
        help = ["-"]*len(word)
        lives = 8
        while True:

            print(f'''HANGMAN
            Guess the word:{"".join(help)}
            ''')
            user_input = input()
            if len(user_input) >1:
                print("You should input a single letter.")
                continue
            if user_input <"a" or user_input >"z":
                print("Please enter a lowercase English letter.")
                continue
            if user_input in letters:
                print("You've already guessed this letter.")
                continue
            if user_input in word:
                for i in range(0,len(word)):
                    if user_input == word[i]:
                        help[i] = user_input
                if "-" not in help:
                    print("You won")
                    break
            else:
                print("The letter doesn't appear in the word")
                lives -=1
                if lives == 0:
                    print("You lost")
                    break
            letters.append(user_input)

        print('''
        Thanks for playing!
        We'll see how well you did in the next stage
        ''')