from random import randint
Choice = ['Rock','Paper',"Scissors"]
computer = Choice[randint(0,2)]
player = False

while player == False:
    player = input('Rock,Paper,Scissors?')
    if computer == player:
        print('Equal')

    elif player == 'Rock':
        if computer == 'Paper':
            print('YOU LOSE!',computer,'covers',player)
        else:
            print('YOU WIN!',player,'smashes',computer)

    elif player == 'Paper':
        if computer == 'Scissors':
            print('YOU LOSE!',computer,'cut',player)
        else:
            print('YOU WIN',player,'covers',computer)
    
    elif player == 'Scissors':
        if computer == 'Rock':
            print('YOU LOSE!',computer,'smashes',player)
        else:
            print('YOU WIN',player,'cut',computer)
    
    else:
        print('Check your spelling!')

    
    #We want the player to be False so that the loop continues
    player = False
    computer = Choice[randint(0,2)]
