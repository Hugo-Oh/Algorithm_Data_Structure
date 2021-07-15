def solution(lottos, win_nums):

    same_num = 0
    rate = {6 : 1, 5 : 2, 4 : 3, 3 : 4, 2 : 5}

    for i in lottos:
        for j in win_nums:
            if i == j:
                same_num += 1

                max_num = same_num + lottos.count(0)
                min_num = same_num

    maxx = rate[max_num] if max_num in rate else 6
    minn = rate[min_num] if min_num in rate else 6

    answer = [maxx, minn]
    return answer

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))