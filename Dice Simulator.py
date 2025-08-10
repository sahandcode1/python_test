import random 

def Dice_simulator():
    return random.randint(1,6)

def Dice():
    while True:
        choice = input('\n1. Rolling the dice \n2. Exit\nchoose: ')
        if choice == '1':
            print(f'you rolled the dice: {Dice_simulator()}')
        elif choice == '2':
            print('Goodbye!')
            break
        else:
            print('Invalid choice.')
if __name__ == '__main__':
    Dice()
