for test in range(int(input())):
    N = int(input())
    K = input()
    S = list(map(int, K))
    res = 0
    scoreA, scoreB = 0, 0
    remA, remB = N, N
    for i in range(len(S) - 1):
        # print(scoreA,scoreB,remA,remB)
        if i % 2 == 0: 
            if S[i] == 1:
                scoreA +=1
            remA -= 1
        else:
            if S[i] == 1:
                scoreB += 1
            remB -=1
        if scoreA-scoreB > remB or scoreB-scoreA > remA:
            res = i+1
            break
       
    print(res)

                