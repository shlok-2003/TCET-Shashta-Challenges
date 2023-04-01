def main():
    n = int(input())
    str = input()

    ans = 0
    for i in range(0, n-2):
        if str[i] == str[i+2]:
            ans += 1
    print(n - 1 - ans)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        main()