import bisect

bisect.bisect_left()
bisect.bisect_right()
"""info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]

query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

#전체 경우의 수 = 4 * 3 * 3 * 3 = 무조건 이중에 하나...
#결국 어떤게 들어오든 이 선택지중에 하나를 고르는 것이므로
#score를 제외하고는 이 앞의 조건들을 indexing화 시키는건 어떨지
#java = 0, 1, 2
#back/front = 0, 1
#appl = 0, 1
#food = 0, 1
#backend = 1
#로 변환해서 넣기
df_info = []
df_con  = []
for i in info:
    temp = i.split()
    df_info.append([x[0] for x in temp[:-1]] + [int(temp[-1])])


#- = pass
for i in query:
    temp_con = i.replace("and", " ").replace("   |  "," ").split()
    df_con.append([x[0] for x in temp_con[:-1]] + [int(temp_con[-1])])

print(df_info)

"""

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]

query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
a = [1, 2, 2]
print(a.count(2))