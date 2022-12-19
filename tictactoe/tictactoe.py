# print('''
# X O X
# O X O
# X X O
# ''')

# compare = ['X','O','_']
# print("Enter cells:")
# user_input = input()
# while user_input.count(compare[0])+user_input.count(compare[1])+user_input.count(compare[2])!=9 and len(user_input)!=9:
#     print("Enter cells:")
#     user_input = input()
# user_input = list(user_input)
# field =[
# [user_input[0],user_input[1],user_input[2]],
# [user_input[3],user_input[4],user_input[5]],
# [user_input[6],user_input[7],user_input[8]]
# ]
#
# print(f'''
# -----
# |{"".join(field[0])}|
# |{"".join(field[1])}|
# |{"".join(field[2])}|
# -----
# ''')

# compare = ['X','O','_']
# print("Enter cells:")
# user_input = input()
# while user_input.count(compare[0])+user_input.count(compare[1])+user_input.count(compare[2])!=9 and len(user_input)!=9:
#     print("Enter cells:")
#     user_input = input()
# field =[
# [user_input[0],user_input[1],user_input[2]],
# [user_input[3],user_input[4],user_input[5]],
# [user_input[6],user_input[7],user_input[8]]
# ]
#
# print(f'''
# -----
# |{"".join(field[0])}|
# |{"".join(field[1])}|
# |{"".join(field[2])}|
# -----
# ''')
# xwin = (field[0][0] + field[0][1] + field[0][2]).count('XXX') + (field[1][0] + field[1][1] + field[1][2]).count('XXX') + (field[2][0] + field[2][1] + field[2][2]).count('XXX') + (field[0][0] + field[1][1] + field[2][2]).count('XXX') + (field[0][2] + field[1][1] + field[2][0]).count('XXX') + (field[0][0] + field[1][0] + field[2][0]).count('XXX') + (field[0][1] + field[1][1] + field[2][1]).count('XXX') +(field[0][2] + field[1][2] + field[2][2]).count('XXX') == 1
# owin = (field[0][0] + field[0][1] + field[0][2]).count('OOO') + (field[1][0] + field[1][1] + field[1][2]).count('OOO') + (field[2][0] + field[2][1] + field[2][2]).count('OOO') + (field[0][0] + field[1][1] + field[2][2]).count('OOO') + (field[0][2] + field[1][1] + field[2][0]).count('OOO') + (field[0][0] + field[1][0] + field[2][0]).count('OOO') + (field[0][1] + field[1][1] + field[2][1]).count('OOO') +(field[0][2] + field[1][2] + field[2][2]).count('OOO') == 1
# while True:
#     if xwin + owin >1 or abs(user_input.count('X')-user_input.count('O')) >1:
#         print("Impossible")
#         break
#     if xwin == 1:
#         print("X Wins")
#         break
#     if owin == 1:
#         print("O Wins")
#         break
#     if '_'not in user_input  :
#         print("Draw")
#         break
#     else:
#         print("Game not finished")
#         break

# compare = ['X','O','_']
# print("Enter cells:")
# user_input = input()
# while user_input.count(compare[0])+user_input.count(compare[1])+user_input.count(compare[2])!=9 and len(user_input)!=9:
#     print("Enter cells:")
#     user_input = input()
# field =[
# [user_input[0],user_input[1],user_input[2]],
# [user_input[3],user_input[4],user_input[5]],
# [user_input[6],user_input[7],user_input[8]]
# ]
#
# print(f'''
# -----
# |{"".join(field[0])}|
# |{"".join(field[1])}|
# |{"".join(field[2])}|
# -----
# ''')
#
# while True:
#     user_input = input().split(' ')
#     if user_input[0].isnumeric() == False or user_input[1].isnumeric() == False:
#         print("You should enter numbers!")
#         continue
#     if int(user_input[0]) <1 or int(user_input[0]) >3 or int(user_input[1]) <1 or int(user_input[1]) >3:
#         print("Coordinates should be from 1 to 3!")
#         continue
#     if field[int(user_input[0])-1][int(user_input[1])-1] != "_":
#         print("This cell is occupied! Choose another one!")
#         continue

symbol = ['X','O']
field =[
['_','_','_'],
['_','_','_'],
['_','_','_']
]

print(f'''
-----
|{"".join(field[0])}|
|{"".join(field[1])}|
|{"".join(field[2])}|
-----
''')
turn = 'X'
while True:
    user_input = input().split(' ')
    if user_input[0].isnumeric() == False or user_input[1].isnumeric() == False:
        print("You should enter numbers!")
        continue
    if int(user_input[0]) <1 or int(user_input[0]) >3 or int(user_input[1]) <1 or int(user_input[1]) >3:
        print("Coordinates should be from 1 to 3!")
        continue
    if field[int(user_input[0])-1][int(user_input[1])-1] != "_":
        print("This cell is occupied! Choose another one!")
        continue
    field[int(user_input[0])-1][int(user_input[1])-1] = turn
    print(f'''
    -----
    |{"".join(field[0])}|
    |{"".join(field[1])}|
    |{"".join(field[2])}|
    -----
    ''')
    win = (field[0][0] + field[0][1] + field[0][2]).count(turn*3) + (field[1][0] + field[1][1] + field[1][2]).count(
        turn*3) + (field[2][0] + field[2][1] + field[2][2]).count(turn*3) + (
                       field[0][0] + field[1][1] + field[2][2]).count(turn*3) + (
                       field[0][2] + field[1][1] + field[2][0]).count(turn*3) + (
                       field[0][0] + field[1][0] + field[2][0]).count(turn*3) + (
                       field[0][1] + field[1][1] + field[2][1]).count(turn*3) + (
                       field[0][2] + field[1][2] + field[2][2]).count(turn*3) == 1

    if win == 1:
        print(turn,'Win')
        break
    turn = symbol[symbol.index(turn)-1]
