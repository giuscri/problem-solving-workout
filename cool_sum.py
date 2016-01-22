def cool_sum(lst, c=0):
    if len(lst) == 0: return c
    return cool_sum(lst[1:], c+lst[0])
