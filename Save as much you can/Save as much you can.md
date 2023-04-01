# Title- Still Not Finalized

Shlok loves to travel. As his examination is over, he is planning for a vacation to Ujjain. The entire journey can be completed either by train or by bus. 

- Train ticket cost $X$<sub>$i$</sub> Rupees ($0$ <= $i$ < $N$).
- Bus ticket cost $Y$<sub>$i$</sub> Rupees ($0$ <= $i$ < $N$).

There are $N$ Stops. You are given the cost for train and bus for $N$ stops. Shlok can use train for $a$ stops and then can use bus for $b$ stops. As Shlok is weak in Maths, your task is to find the minimum cost required to complete the journey.

$Note$: You can use both the train and bus.

---
***Input***

The first line of input contains an integer $T$ denoting the number of test cases.

Each test case consists of multiple lines of input:

- The first line of each test case contains an integer $N$
the number of stops.
- The second line of each test case contains $N$ space-separated integers, $X$<sub>$i$</sub>
, denoting the cost of each Train stop.
- The third line of each test case contains $N$ space-separated integers, $Y$<sub>$i$</sub>
, denoting the cost of each Bus stop.

---
***Output***

Output the minimum cost required to complete the journey.

---

***Constraints***

1 <= $t$ <= $10^{4}$

1 <= $n$ <= $2*10^{5}$ 

1 <= $X$<sub>$i$</sub> <= $10^{5}$

1 <= $Y$<sub>$i$</sub> <= $10^{5}$

---

***Sample Input***

2

5

2 5 7 4 11

3 4 5 7 12

9

10 8 4 9 9 6 4 3 2

9 7 9 6 4 7 3 8 2

***Sample Output***

26

44

***Explanation***

**Test Case: 1:**
Shlok can travel by Train for 1, 4, 5 stops (_1_-based indexing), and for stop 2 and 3, he can travel by Bus


---

## DIFFICULTY:

Easy

## PRE-REQUISITES

Array, Greedy

## PROBLEM STATEMENT

Shlok loves to travel. As his examination is over, he is planning for a vacation to Ujjain. The entire journey can be completed either by train or by bus. 

- Train ticket cost $X$<sub>$i$</sub> Rupees ($0$ <= $i$ < $N$).
- Bus ticket cost $Y$<sub>$i$</sub> Rupees ($0$ <= $i$ < $N$).

There are $N$ Stops. You are given the cost for train and bus for $N$ stops. Shlok can use train for $a$ stops and then can use bus for $b$ stops. As Shlok is weak in Maths, your task is to find the minimum cost required to complete the journey.

$Note$: You can use both the train and bus

## Explanation

You need to find a greedy approach. We can iterate the whole array's, and we can add the minimum of the cost of Train and Bus at same index, to the answer variable. Then print the answer variable.

**C++ Solution**
```
#include <bits/stdc++.h>
```
```
using namespace std;
```
```
int main() {
    int t;
    cin >> t;

    while(t--)
    {
        int n;
        cin >> n;

        vector<int> train(n), bus(n);
        for(int i = 0; i < n; i++)
            cin >> train[i];

        for(int i = 0; i < n; i++)
            cin >> bus[i];

        long long cost = 0;
        for(int i = 0; i < n; i++)
            cost += min(train[i], bus[i]);

        cout << cost << endl;
    }
}
```
---

## Time Complexity

$O$($n$) for each test case