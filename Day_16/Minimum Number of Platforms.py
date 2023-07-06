from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

def calculateMinPatforms(at, dt, n):
    # Write your code here.
    que = [0] * 2400
    for i in range(n):
        que[at[i]] += 1
        que[dt[i]+1] -= 1

    for i in range(1, 2400):
        que[i] += que[i-1]

    return max(que)
# Taking the input.
def takeInput():
    n = int(stdin.readline().strip())
    at = list(map(int, stdin.readline().strip().split(" ")))
    dt = list(map(int, stdin.readline().strip().split(" ")))

    return at, dt, n

# Main.
T = int(input())
while (T > 0):
    T -= 1
    at, dt, n = takeInput()
    minNumOfPlatforms = calculateMinPatforms(at, dt, n)
    print(minNumOfPlatforms)