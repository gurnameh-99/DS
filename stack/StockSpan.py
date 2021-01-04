
from sys import stdin

def stockSpan(price, n) :
    output = [-1] * n
    print(output)
    span = []
    for i in range(0, len(price)):
        spanCount = 1
        j = i-1
        while price[j] < price[i] and j >= 0:
            spanCount += 1
            j -= 1
        span.append(spanCount)
    return span

'''-------------- Utility Functions --------------'''




def printList(arr) :
	for i in range(len(arr)) :
		print(arr[i], end = " ")

	print()


def takeInput():
	size = int(stdin.readline().strip())

	if size == 0 :
		return list(), 0

	price = list(map(int, stdin.readline().strip().split(" ")))

	return price, size


#main
price, n = takeInput()

output = stockSpan(price, n)
printList(output)
