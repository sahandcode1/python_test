from random import randint

number = randint(0,100)
count = 0

while True:
    guess = input('Gusse the number: ')
    if guess.isdigit():    
        intnumber = int(guess)
        print('You entered:',intnumber)
        
        if intnumber > number:
           print('Lower')
        elif intnumber < number:
            print('Higher')
        else:
            (print('Tou win! The number is ' + guess + '!'),quit())
        count += 1
    else:
        print('Please enter an integer number.')
