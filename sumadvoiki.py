def list_sum(l1, l2):
    long_list, short_list = (l1, l2) if len(l1) > len(l2) else (l2, l1)
    while len(short_list) < len(long_list):
        short_list.extend(short_list)
    return sum(x*y for x, y in zip(short_list, long_list))

lst1 = [1,2]
lst2 = [1,2,3,4,5]

print(list_sum(lst1, lst2))