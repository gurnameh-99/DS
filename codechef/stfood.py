for test in range (int(input())):
    N = int(input())
    profit = 0
    while(N):
        N -= 1
        S, P, V = map(int, input().split())
        cost = int(P/(S+1)) * V
        if cost > profit:
            profit = cost
    
    print(profit)
    #This is a code to highlight the profit of a shopkeeper in order to decide which food he must make daily for gaininig maximum profit