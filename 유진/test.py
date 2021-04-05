def dfs(cnt):
    global ans
    if cnt == 9:
        start, score = 0, 0

        for inning in a: # 선수별 이닝 반복문
            out, b1, b2, b3 = 0, 0, 0, 0 # 베이스

            while out < 3: # 쓰리아웃
                p = select[start]
                if inning[p] == 0: # 아웃
                    out += 1
                elif inning[p] == 1: # 1루타
                    score += b3
                    b1, b2, b3 = 1, b1, b2
                elif inning[p] == 2: # 2루타
                    score += b2 + b3
                    b1, b2, b3 = 0, 1, b1
                elif inning[p] == 3: # 3루타
                    score += b1 + b2 + b3
                    b1, b2, b3 = 0, 0, 1
                else: # 홈런
                    score += b1 + b2 + b3 + 1
                    b1, b2, b3 = 0, 0, 0

                start += 1 # 선수 인덱스에 하나 더 해주고
                start %= 9 # 이어서 칠수 있도록

        ans = max(ans, score)
        return

    for i in range(9):
        if visit[i]:
            continue
        visit[i] = 1
        select[i] = cnt
        dfs(cnt + 1)
        visit[i] = 0
        select[i] = 0


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
select, visit = [0 for _ in range(9)], [0 for _ in range(9)]
visit[3] = 1 # 4번타자
ans = 0
dfs(1)
print(ans)