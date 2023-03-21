try:
    a = int(input('Enter a number: '))
    if a>0:
        print('Postive')
    elif a<0:
        print('Negative')
    elif a==0:
        print('Zero')
    else:
        print('I told a number, check or leave this program')
except:
    print('I told a number not rubbish, number is without spaces!!')
    print('check or leave this program')
    print('Koi itna ameer hei ki ye program run kar saktha hein, par 4th class fail kyu')
    print('NUMBER YAANI NUMBER!!!!!!!!!!!!!!!!!')
finally:
    input('\nPress ENTER to exit')
