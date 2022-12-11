import random

# friendlist = dict()
# print("Enter the number of friends joining (including you)")
# guests = int(input())
# if guests <= 0:
#     print("No one is joining for the party")
# else:
#     print("Enter the name of every friend (including you), each on a new line:")
#     for i in range(0,guests):
#         user_input = input()
#         friendlist[user_input] = 0
#     print(friendlist)

# friendlist = dict()
# print("Enter the number of friends joining (including you)")
# guests = int(input())
# if guests <= 0:
#     print("No one is joining for the party")
# else:
#     print("Enter the name of every friend (including you), each on a new line:")
#     for i in range(0, guests):
#         user_input = input()
#         friendlist[user_input] = 0
#     print("Enter the total amount:")
#     total_amount =  int(input())
#     amount = round(total_amount / guests,2)
#     for friend in friendlist:
#         friendlist[friend] = amount
#     print(friendlist)

# friendlist = dict()
# print("Enter the number of friends joining (including you)")
# guests = int(input())
# if guests <= 0:
#     print("No one is joining for the party")
# else:
#     print("Enter the name of every friend (including you), each on a new line:")
#     for i in range(0, guests):
#         user_input = input()
#         friendlist[user_input] = 0
#     print("Enter the total amount:")
#     total_amount =  int(input())
#     amount = round(total_amount / guests,2)
#     for friend in friendlist:
#         friendlist[friend] = amount
#     print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
#     user_input = input()
#     if user_input == 'Yes':
#         lucky = random.choice(list(friendlist))
#         print(lucky,"is the lucky one!")
#     else:
#         print("No one is going to be lucky")

friendlist = dict()
print("Enter the number of friends joining (including you)")
guests = int(input())
if guests <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(0, guests):
        user_input = input()
        friendlist[user_input] = 0
    print("Enter the total amount:")
    total_amount =  int(input())
    amount = round(total_amount / guests,2)
    for friend in friendlist:
        friendlist[friend] = amount
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    user_input = input()
    if user_input == 'Yes':
        lucky = random.choice(list(friendlist))
        amount = round(total_amount / (guests-1), 2)
        for friend in friendlist:
            friendlist[friend] = amount
        friendlist[lucky] = 0
        print(lucky,"is the lucky one!")
    else:
        print("No one is going to be lucky")
    print(friendlist)