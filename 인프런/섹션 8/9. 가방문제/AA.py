import sys
#sys.stdin = open("input.txt", "rt")

N, M = map(int, input().split())

jewelry = [tuple(map(int, input().split())) for _ in range(N)]

#print(jewelry)

#dp[i] = i번째 인덱스일때 얻을수 있는 보석의 최대가치? 이렇게 하면 안된다!
#dp = [0 for _ in range(N)] 즉 이건 틀리다.
#dp[i] = ikg일때 얻을 수 있는 보석의 최대가치
dp = [0 for _ in range(M+1)] #0KG~ MKG일때
dp[0] = 0 # 사용갯수는 각 종류마다 무제한 개!(즉 냅색중에서도 무제한)

for jewel_w, jewel_v in jewelry: #종류벌로 n번돈다.
    for weight in range(jewel_w, M+1): #시작은 jewel_w kg 끝은 Mkg
        dp[weight] = max(dp[weight], dp[weight - jewel_w] + jewel_v) #계속해서 갱신해준다.

print(dp[M]) #Mkg일때의 값



