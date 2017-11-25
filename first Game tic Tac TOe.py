list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
row1 = [' ', "|", ' ', '|', ' ']
row2 = [' ', "|", ' ', '|', ' ']
row3 = [' ', "|", ' ', '|', ' ']
Rowmain = [row1[0], row2[0], row3[0], row1[2], row2[2], row3[2], row1[4], row2[4], row3[4]]


def table(n=" ", marktable="xxoo", Tot=0):
    if n == 1:
        row3[0] = marktable
    elif n == 2:
        row3[2] = marktable
    elif n == 3:
        row3[4] = marktable
    elif n == 4:
        row2[0] = marktable
    elif n == 5:
        row2[2] = marktable
    elif n == 6:
        row2[4] = marktable
    elif n == 7:
        row1[0] = marktable
    elif n == 8:
        row1[2] = marktable
    elif n == 9:
        row1[4] = marktable
    else:
        pass

    print(row1[0], "|", row1[2], '|', row1[4])
    str1 = (row1[0], "|", row1[2], '|', row1[4])
    print(('_' * len(str1)) + '____')
    print(row2[0], "|", row2[2], '|', row2[4])
    print(('_' * len(str1)) + '____')
    print(row3[0], "|", row3[2], '|', row3[4])

    resX = ['X', 'X', 'X']
    resO = ['O', 'O', 'O']

    Possibl1 = [row1[0], row2[0], row3[0]]
    Possibl2 = [row1[2], row2[2], row3[2]]
    Possibl3 = [row1[4], row2[4], row3[4]]
    Possibl4 = [row1[0], row1[2], row1[4]]
    Possibl5 = [row2[0], row2[2], row2[4]]
    Possibl6 = [row3[0], row3[2], row3[4]]
    Possibl7 = [row1[0], row2[2], row3[4]]
    Possibl8 = [row3[0], row2[2], row1[4]]

    POS = [Possibl1, Possibl2, Possibl3, Possibl4, Possibl5, Possibl6, Possibl7, Possibl8]
    Rowmain = [row1[0], row2[0], row3[0], row1[2], row2[2], row3[2], row1[4], row2[4], row3[4]]

    for z in range(Tot):
        if resX in POS:
            print("\nThe player 1 is winner")
            exit()
        elif resO in POS:
            print("\nthe player 2 is winner")
            exit()
        elif ' ' in Rowmain:
            break
        else:
            print("\nTHe game is draw")
            exit()


def innum(mark="mark", num=0, times=0):
    if mark == "X":

        table(num, mark, times)
        list.remove(num)
    elif mark == 'O':
        table(num, mark, times)
        list.remove(num)


print("\nWElCOME TO TIC TAC TOE")

table()

print("\nonly press numbers from 1to 9 on numpad. player1 has X and Player2 has O")
m1 = 0

for m in range(20):
    if m1 % 2 == 0:
        print("\nplayer 1 should enter the number/position now")
        number = int(input("\nenter the number on the numpad according to the place you want to mark:"))
        if number in list:
            innum("X", number, m1)
            m1 += 1
        else:
            print("\nenter the correct number again:")

    else:
        print("\nplayer 2 should enter the number/position now")
        number = int(input("\nenter the number on the numpad according to the place you want to mark:"))
        if number in list:
            innum("O", number, m1)
            m1 += 1
        else:
            print('\nenter the correct number again:')
