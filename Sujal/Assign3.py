transaction = 0

while True:
    print('\n1. Deposit')
    print('2. Withdraw')
    print('3. Quit')

    Input = input('Enter the number : ')

    if Input == '1':
        amount = int(input('Enter Deposit Amount : '))
        transaction += amount
        print('Your Current Amount : ', transaction)

    elif Input == '2':
        withdraw = int(input('Enter Withdraw Amount : '))
        transaction -= withdraw
        print('Your Current Amount : ', transaction)

    elif Input == '3':
        break

    else:
        print('Wrong Input !!!')
