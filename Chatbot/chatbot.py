print("Hello! My name is Magnus.")
print("I was created in 2022.")

user_input = input ("Please, remind me your name.\n")
print ("What a great name you have,",user_input,"!" )

print("Let me guess your age")
print("Enter reminders of dividing your age by 3, 5 and 7")
remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print ("Your age is",age,"that's a good time to start programing!")

print ("Now i will prove you that i can count to any number you want.")
max_number = int(input())
count = 0
while count <= max_number:
    print(count,"!")
    count += 1
print("Completed, have a nice day!")

print(''' Let's test your programming knowledge.
How do you insert COMMENTS in Python code?
1.#This is a comment
2./*this is a comment*/
3.//This is a comment
4.There's no way to comment
''')
answer = int(input())
while answer !=1:
    print("Please, try again.")
    answer = int(input())
print("Completed, have a nice day!")
print("Congratulations, have a nice day!")
