from time import sleep

duration = int(input('Enter the duration in seconds: '))
count = 0

while count < duration:
    print(count,end='\r')  #Prints the current duration
    sleep(1)               #sleep for 1 second
    count +=1              #update the current duration
print('Time is up!')
