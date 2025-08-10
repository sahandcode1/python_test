def Addition(first_number,second_number):
    return first_number + second_number
def subtraction(first_number,second_number):
    return first_number - second_number
def multiplication(first_number, second_number):
    return first_number * second_number
def division(first_number,second_number):
    return first_number / second_number

print('1. Addition')
print('2. subtraction')
print('3. multiplication')
print('4. divide')

while True:
    choice = input('Enter choice(1/2/3/4 or n to cancel):')
    if choice in ('1','2','3','4'):
        first_number = float(input('Enter first number:'))
        second_number = float(input('Enter second number:'))

        if choice == '1':
            print(first_number,'+',second_number,'=',Addition(first_number,second_number))
        elif choice == '2':
            print(first_number,'-',second_number,subtraction(first_number,second_number))
        elif choice == '3':
            print(first_number,'*',second_number,multiplication(first_number,second_number))
        elif choice == '4':
            print(first_number,'/',second_number,division(first_number,second_number))
    elif choice == 'n':
        print('your are successfuly logged out')
        break
    else:
        print('Please enter correct input among these 1/2/3/4')
        
