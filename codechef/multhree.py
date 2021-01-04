
for test in range(int(input())):
    length, d1, d2 = map(int, input().split(" "))
    _sum = d1 + d2
    if length == 2:
        if(_sum % 3 == 0 and _sum != 0):
            print("YES")
        else:
            print("NO")
        continue
    temp = (d1 + d2) % 10
    _sum += temp

    groups = int((length - 3) / 4)
    remaining = length - (groups*4) - 3
    _sum += (groups * 20)
    for i in range(remaining):
        temp = (2 * temp)%10
        _sum += temp

    if _sum % 3 == 0:
        print("YES")
    else:
        print("NO")
