import random

while True:
    choice= input("\n1 -> Rolling the dice  \n2 -> Exit \nChoose: ").strip()
    if choice == '1':
        print("You rolled the dice:",random.randint(1,6))
    elif choice == '2':
        print("Goodbye")
        break
    else:
        print("Wrong Input")
        