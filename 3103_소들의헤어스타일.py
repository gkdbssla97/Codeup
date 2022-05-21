from collections import deque
N = int(input())

cow = deque()

top = -1
cnt = 0
for i in range(N):
    val = int(input())
    if top == -1:
        cow.append(val)
        top += 1
    else:
        if cow[top] > val:
            cow.append(val)
            cnt += len(cow) - 1
            top += 1
        else:
            #print(f'cow[top]:{cow[top]} val:{val}')
            while cow[top] <= val and top != -1:
                cow.pop()
                top -= 1
                #print(f'top:{top}')
                if top == -1:
                    break
            cow.append(val)
            if top != -1:
                cnt += len(cow) - 1
            top += 1
    #print(cow, top)
    #print(f'cnt:{cnt}')
print(cnt)
