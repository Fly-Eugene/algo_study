# count 하는 배열을 만든다.
# 0점부터 100점까지 101의 길이를 갖는다.
n = int(input()) # 테스트 회수
for tc in range(0, n):
    # 시험 점수의 범위가 0 ~ 100점까지이다.
    score_cnt = [0] * 101
    tc_index = int(input()) # 테스트 케이스 번호. #1, #2, #3...

    scores = list(map(int, input().split()))
    # 이 때 학생수가 1000명이므로, scores 역시 1000개의 element를 갖는 list이다.
    for score in scores:
        score_cnt[score] += 1 # 값에 해당하는 인덱스에 +1씩 카운트한다.

    # score_cnt : index는 점수를 나타내고, index에 해당하는 값은 count를 나타낸다.
    # 최빈값을 찾는다.
    most_cnt = score_cnt[0]
    most_score = 0 # 이게 결국 점수를 의미한다.

    for score,cnt in enumerate(score_cnt):
        if cnt > most_cnt:
            most_cnt = cnt
            most_score = score
        # 최빈수가 여러 개 일때를 고려해야 한다...
        # 카운트한 값이 동일한 경우에는? 큰 값을 기준으로 넣어야 한다.
        if cnt == most_cnt:
            # 값을 비교해야 한다.
            if most_score > score:
                pass
            else:
                most_cnt = cnt
                most_score = score

    print(f'#{tc_index} {most_score}')

    # list comprehension을 이용하여 다음과 같이 작성할 수도 있다.
    # ans = [i for i in range(len(arr)) if arr[i] == max(arr)]