from sys import exit
import random
import time

print('')
print('welcome to the dice roll simulator')
time.sleep(1)

while True:
    while True:
        print('')
        roll = input('type and enter roll to get a number in the dice: ')
        
        if roll == 'roll' or roll == 'Roll':
            break
        elif roll == 'ROll':
            break
        else:
            print('Just type roll')
    
    dice_roll = random.randint(1, 6)

    if dice_roll == 1:
        print('')
        print(' ___________ ')
        print('|           |')
        print('|           |')
        print('|     *     |')
        print('|           |')
        print('|___________|')
    elif dice_roll == 2:
        print('')
        print(' ____________ ')
        print('|            |')
        print('|            |')
        print('|    *  *    |')
        print('|            |')
        print('|____________|')
    elif dice_roll == 3:
        print('')
        print(' ___________ ')
        print('|           |')
        print('|      *    |')
        print('|     *     |')
        print('|    *      |')
        print('|___________|')
    elif dice_roll == 4:
        print('')
        print(' ___________ ')
        print('|           |')
        print('|  *      * |')
        print('|           |')
        print('|  *      * |')
        print('|___________|')
    elif dice_roll == 5:
        print('')
        print(' ____________ ')
        print('|            |')
        print('|  *       * |')
        print('|      *     |')
        print('|  *       * |')
        print('|____________|')
    elif dice_roll == 6:
        print('')
        print(' _____________ ')
        print('|             |')
        print('|   *     *   |')
        print('|   *     *   |')
        print('|   *     *   |')
        print('|_____________|')
    
    print('')
    print('Do you want to play this simulator again')
    simulator = input('>> ')
    if simulator == 'no' or simulator == 'No':
        exit()
    elif simulator == 'NO':
        exit()