#from _collections import queue

n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
words_checker = {x : [] for x in words}

i = 1

while True:
    word = words.pop(0)
    if i % n in words_checker[word]: # (i % n) 번째
        print([i % n, i // n])
        break

    else:
        words_checker[word].append(i % n)
        words.append(word) #다시 queue에 append
        i += 1