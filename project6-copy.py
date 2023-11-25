import random

def playerNum():
    print("Enter player number (1 - 5 players):")
    pnum1 = int(input())
    while(pnum1 < 1 or pnum1 > 5):
        print("Try again:")
        pnum1 = int(input())
    return pnum1

def difficulty():
    print("Select the difficulty (1: Easy, 2: Medium, 3: Hard):")
    diff1 = int(input())
    print("\n")
    while(diff1 < 1 or diff1 > 3):
        print("Try again:")
        diff1 = int(input())
        print("\n")
    if diff1 == 1:
        x = 5
    elif diff1 == 2:
        x = 6
    else:
        x = 10
    return x

def genBoard(dx):
    board1 = []
    temp = []
    snum1, lnum1 = 0, 0
    for i in range(dx):
        for j in range(dx):
            temp.append(["XXX"])
        board1.append(temp)
        temp = []
    if dx == 5:
        snum1 = random.randint(1, 2)
        lnum1 = random.randint(snum1+1, 3)
    elif dx == 6:
        snum1 = random.randint(2, 4)
        lnum1 = snum1
    elif dx == 10:
        lnum1 = random.randint(1,5)
        snum1 = random.randint(lnum1+1, 6)
    return board1, snum1, lnum1

def showBoard(dx, bx):
    for i in range(dx):
        for j in range(dx):
            print(bx[i][j], end=' ')
        print("\n")

def getlistLocation(dx, num):
    x = 0 
    y = 0
    if num%dx != 0:
        x = (dx - 1) - int(num / dx)
    else:
        x = (dx - 1) - (int(num / dx) - 1)
    
    if dx%2 != 0:
        if x%2 == 0 and num%dx != 0:
            y = int((num % dx) - 1)
        elif x%2 == 0 and num%dx == 0:
            y = dx - 1
        elif x%2 != 0 and num%dx == 0:
            y = 0
        else:
            y = (dx - 1) - int((num%dx) - 1)
    else:
        if x%2 != 0 and num%dx != 0:
            y = int((num % dx) - 1)
        elif x%2 != 0 and num%dx == 0:
            y = dx - 1
        elif x%2 == 0 and num%dx == 0:
            y = 0
        else:
            y = (dx - 1) - int((num%dx) - 1)

    return x, y

def getnumLocation(dx, x, y):
    if dx%2 != 0:
        if x % 2 == 0:
            num = (y + 1) + (dx * ((dx - 1) - x))
        else:
            num = (dx - x) * dx - y
    else:
        if x % 2 != 0:
            num = (y + 1) + (dx * ((dx - 1) - x))
        else:
            num = (dx - x) * dx - y   
    return num

def genEntity(px, dx, sx, lx, bx):
    temp = []
    rtemp = []
    sh = []
    sp = []
    lh = []
    lp = []

    for i in range(px):
        temp.append(f"P{i+1}")
    bx[dx-1][0] = temp

    temp = []

    for i in range((sx+lx)*2):
        rtemp.append(random.randint(2,dx*dx-1))

    x = len(rtemp)

    for i in range(x):
        j = 0
        while j < x:
            if j != i and rtemp[j] == rtemp[i]:
                rtemp[i] = random.randint(2,dx*dx-1)
                j = 0
            else:
                j += 1

    for i in range(len(rtemp)):
        if i < sx*2:
            sh.append(rtemp[i])
        else:
            lh.append(rtemp[i])

    x = len(sh)
    i = 0

    while i < x - 1:
        temp.append(sh[i])
        temp.append(sh[i+1])
        sp.append(temp)
        temp = []
        i+=2

    for i in range(len(sp)):
        if sp[i][0] < sp[i][1]:
            sp[i][0], sp[i][1] = sp[i][1], sp[i][0]

    x = len(lh)
    i = 0

    while i < x - 1:
        temp.append(lh[i])
        temp.append(lh[i+1])
        lp.append(temp)
        temp = []
        i+=2

    for i in range(len(lp)):
        if lp[i][0] > lp[i][1]:
            lp[i][0], lp[i][1] = lp[i][1], lp[i][0]

    n = 0
    m = 0
    l = 1
        
    for i in range(2):
        for j in range(len(sp)):
            if i == 0:
                n, m = getlistLocation(dx, sp[j][i])
                bx[n][m] = [f"Snake Head {l}"]
                l += 1
            else:
                n, m = getlistLocation(dx, sp[j][i])
                bx[n][m] = [f"Snake Tail {l}"]
                l += 1
        l = 1
        
    for i in range(2):
        for j in range(len(lp)):
            if i == 0:
                n, m = getlistLocation(dx, lp[j][i])
                bx[n][m] = [f"Ladder Head {l}"]
                l += 1
            else:
                n, m = getlistLocation(dx, lp[j][i])
                bx[n][m] = [f"Ladder Tail {l}"]
                l += 1
        l = 1
        
    return bx, sp, lp
    
def rolldice():
    x = random.randint(1,6)
    return x

def rounds(bx, px, dx, slx, llx):
    win = 0
    round = 1
    while(win == 0):
        for i in range(px):
            k = 0
            x = 0
            y = 0
            z = 0
            print(f"Player {i+1}: Roll the dice: (Press 'Enter' key)")
            input()
            roll = rolldice()
            print(f"Player {i+1} rolled '{roll}'")
            print("\n")
            print("\n")
            for j in range(dx):
                for k in range(dx):
                    if len(bx[j][k]) > 1 and bx[j][k] != ["XXX"]:
                        for l in range(len(bx[j][k])):
                            if bx[j][k][l] == f"P{i+1}":
                                x = j
                                y = k
                                z = l
                                bx[j][k].remove(f"P{i+1}")
                                break
                    else:
                        if bx[j][k][0] == f"P{i+1}":
                            x = j
                            y = k
                            bx[j][k] = ["XXX"]
                            break

            n = getnumLocation(dx, x, y)
            n = n + roll
            
            if n >= dx*dx:
                win = 1
                wp = i + 1
                break

            for d in range(len(slx)):
                if n == slx[d][0]:
                    n = slx[d][1]
                    print(f"Bited by snake to {slx[d][1]}")
                    print("\n")
                    print("\n")
            
            for e in range(len(llx)):
                if n == llx[e][0]:
                    n = llx[e][1]
                    print(f"Climb ladder to {llx[e][1]}")
                    print("\n")
                    print("\n")

            n1, n2 = getlistLocation(dx, n)

            if bx[n1][n2] == ["XXX"]:
                bx[n1][n2] = [f"P{i+1}"]
            else:
                bx[n1][n2].append(f"P{i+1}")

            showBoard(dx, bx)
            print("\n")
            print("\n")
        
        round += 1
    
    return round, wp
                    
pnum = playerNum()
diff = difficulty()
initialboard, snum, lnum = genBoard(diff)
startboard, sloc, lloc = genEntity(pnum, diff, snum, lnum, initialboard)
showBoard(diff, startboard)
print("\n")
print("\n")
roundspend, winplayer = rounds(startboard, pnum, diff, sloc, lloc)
print("\n")
print("\n")
print(f"Player {winplayer} win, {roundspend} rounds spended")
print("\n")
print("\n")
print("Game Ended")
print("\n")
print("\n")