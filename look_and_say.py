def look_and_say(max_iterations=42):
    iteration_ix = 0
    current = '1'
    while iteration_ix < max_iterations:
        yield current
        next = ''
        i = 0
        j = 0
        while i < len(current):
            j = i
            while j < len(current) and current[i]==current[j]:
                j += 1
            next += str(j-i) + current[i]
            i = j
        current = next
        iteration_ix += 1

if __name__ == '__main__':
    for i, x in enumerate(look_and_say()):
        if i == 7:
            print(x)
            break
