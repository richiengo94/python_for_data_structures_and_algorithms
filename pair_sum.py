def sum_pair(int_arr: list, target: int):
    
    if len(int_arr) < 2:
        return

    count_pair = 0
    used_index = []
    pairs = []

    for i in range(len(int_arr)):
        if i in used_index:
            continue
        else:
            if ((target - int_arr[i]) in int_arr[i:]):
                count_pair += 1
                pairs.append((int_arr[i], target - int_arr[i]))
                used_index.append(int_arr.index(target - int_arr[i], i + 1))

    print(pairs)
    return count_pair

print(sum_pair([1, 3, 2, 2], 4))
print(sum_pair([1, 2, 3, 1], 3))
print(sum_pair([1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 13, 14, 11, 13, -1], 10))

def sum_pair2(int_arr: list, target: int):
    
    if len(int_arr) < 2:
        return
    
    used = set()
    pairs = set()

    for i in int_arr:

        diff = target - i

        if diff not in used:
            used.add(i)

        else:
            pairs.add((min(i, diff), max(i, diff)))

    print('\n'.join(map(str, list(pairs))))

    return len(pairs)

print(sum_pair2([1, 3, 2, 2], 4))
print(sum_pair2([1, 2, 3, 1], 3))
print(sum_pair2([1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 13, 14, 11, 13, -1], 10))