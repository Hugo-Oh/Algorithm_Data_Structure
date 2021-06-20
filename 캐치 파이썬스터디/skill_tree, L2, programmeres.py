skill = "CBD"
skill_tree = ["BACDE", "CBADF", "AECB", "BDA"]

skill_tree = list(map(lambda x : "".join([s for s in x if s in skill]), skill_tree))

cnt = len(skill_tree)
"""for i in skill_tree:
    for j in range(len(i)):
        if i[j] != skill[j]:
            cnt -= 1
            break
"""
cnt = 0
for i in skill_tree:
    if i == skill[:len(i)]:
        cnt += 1

print(cnt)