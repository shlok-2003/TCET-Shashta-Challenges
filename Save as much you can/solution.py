t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    total_cost = 0
    for j in range(n):
        total_cost += min(a[j], b[j])
    print(total_cost)
