# аргумент числов списък
# резултат друг списък, в който са включени само нечетните числа от списъка аргумент

def odd(l):
    return [element for element in l if element % 2]

a = [1,2,3,3,4,5,6,6,6,7,8,9,9,9,]
print(odd(a))