N = int(input())
queue = [i for i in range(1, N + 1)]
front = -1
rear = len(queue) - 1

while front != rear - 1:
    # 1. 카드를 한 장 버린다.
    front += 1

    # 2. 맨 위의 카드를 맨 아래로 옮긴다.
    front += 1
    t = queue[front]
    queue.append(t)
    rear += 1
print(queue[-1])