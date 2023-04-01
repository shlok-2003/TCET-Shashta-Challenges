t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    arr.sort()
    if n == 1:
        print("YES")
    elif arr[0] + arr[-1] <= k:
        print("YES")
    else:
        print("NO")