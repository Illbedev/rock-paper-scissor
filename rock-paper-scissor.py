from random import randint
running = True
while running:
    print('--------------')
    me = input('you choose: ')
    bot = randint(0, 2)
    if bot == 0:
        bot = 'rock'
    elif bot == 1:
        bot = 'paper'
    elif bot == 2:
        bot = 'scissor'
    print('bot choose: {}'.format(bot))

    if bot == me:
        print('=> draw')

    elif me == 'rock':
        if bot == 'paper':
            print('=> you lose')
        else:
            print('=> you win')
    elif me == 'paper':
        if bot == 'rock':
            print('=> you win')
        else:
            print('=> you lose')
    elif me == 'scissor':
        if bot == 'rock':
            print('=> you lose')
        else:
            print('=> you win')
    elif me == 'stop':
        print('--------------')
        print('turing off')
        running = False
    else:
        print('=> wrong input, please choose again')
# learn in 'dunglailaptrinh' (on youtube)
