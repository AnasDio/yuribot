import random
import re
welcome = ["hello","good morning","good afternoon","hi"]
print("||call my name to start||"+"\t"+"||type quit to end||")
while 1:
    start = input()       # takes input from user to start.
    greeting = random.choice(welcome) 
    if "yuri" in start:   # check if the name in the list that user typed.
        print(greeting,", how can i help you?")
        break
    else:
        print("it would be nice if you use my name.")
while 1:
    question = input()
    if question == "quit":
        break
    elif "pick a number" in question:
        low_high=(re.findall('\d+', question))
        rannum=random.randint(low_high[0],low_high[1])
        print("your random number is",rannum)
    else:
        print("hello")
