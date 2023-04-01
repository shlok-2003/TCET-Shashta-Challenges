## DIFFICULTY:

Easy

## PRE-REQUISITES

Array, Greedy

## PROBLEM STATEMENT

Shlok loves to travel. As his examination is over, he is planning for a vacation to Ujjain. The entire journey can be completed either by train or by bus. 

- Train ticket cost $X$<sub>$i$</sub> Rupees ($0$ <= $i$ < $N$).
- Bus ticket cost $Y$<sub>$i$</sub> Rupees ($0$ <= $i$ < $N$).

There are $N$ Stops. You are given the cost for train and bus for $N$ stops. Shlok can use train for $a$ stops and then can use bus for $b$ stops. As Shlok is weak in Maths, your task is to find the minimum cost required to complete the journey.

$Note$: You can use both the train and bus.

## Explanation

You need to find a greedy approach. We can iterate the whole array's, and we can add the minimum of the cost of Train and Bus at same index, to the answer variable. Then print the answer variable.

**Python Solution**

    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        total_cost = 0
        for j in range(n):
            total_cost += min(a[j], b[j])
        print(total_cost)

## Time Complexity

$O$($n$) for each test case