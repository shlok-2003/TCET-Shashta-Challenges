## DIFFICULTY:

Easy

## PRE-REQUISITES

Array, Sorting

## PROBLEM STATEMENT

Kapil has **n** numbers as A<sub>i</sub>, where ($0$ <= $i$ < $N$). He is given a task along with a number **k**. In one step, he can:

- Select two numbers with index *i* and *j*, (i $\neq$) j such that **A<sub>i</sub> + A<sub>j</sub>** **<=** **k**.
- Now, he can either remove **A<sub>i</sub>** or **A<sub>j</sub>**

He can perform these steps several (possibly, zero) times till he is left with only one number. As Kapil has his exam's going on, he cannot single-handedly complete the task. So, you need to help Kapil. Print YES if it's possible to make the array size 1, otherwise NO.

## Explanation

This problem requires removing of element. We can select two numbers at a time, so lets select two smallest number and remove the number which is bigger between them. For example, we can select 1 and 5, and remove the number 5. Note, that these numbers must be present in the array.

As we are the performing these steps, we will eventually come to a point where we would be selecting the smallest number and largest number. Now, If we are able to remove the smallest number between them, then we will print YES, otherwise No. This means that if **smallest-number** + **second-largest-number** <= **k** then YES, otherwise NO.

**Python Solution**

```python
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
```

## Time Complexity

$O$($nlogn$) for each test case.