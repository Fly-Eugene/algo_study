flag = [False] * 8
pos = [0] * 8

def set(i):
    for j in range(8):
        if flag[j] == False:
            pos[i] = j
        if i == 7:
            print(pos)
            break
        else:
            flag[j] = True
            set(i+1)
            flag[j] = False
set(0)
