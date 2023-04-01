## DIFFICULTY:

Easy

## PRE-REQUISITES

String, Greedy

## PROBLEM STATEMENT

Naman has a string **S** of size $n$. In one operation, he wants to:

- Select a substring of length $2$ and remove it from the original string.

He is very eager to know the number of possible unique strings generated from this operation. Can you help Naman, in his task **?**

A substring of string **S** is a sequence that can be created from **S** by deleting some characters and without changing the order of the remaining characters.

## Explanation

Initialize an `ans` variable with value of 0. Now run the loop from 0 to `n-2`. If we find that an character at index `i` is equal to character at index `i+2`, then we increment the value of ans. 

At the end, we return the value `n-1-ans`.

**Python Solution**

```python
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
```

## Time Complexity

$O$($n$) for each test case.