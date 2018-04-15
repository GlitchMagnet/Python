def merge_the_tools(S, K):
    temp = []
    len_temp = 0
    for item in S:
        len_temp += 1
        if item not in temp:
            temp.append(item)
        if len_temp == K:
            print(''.join(temp))
            temp = []
            len_temp = 0
