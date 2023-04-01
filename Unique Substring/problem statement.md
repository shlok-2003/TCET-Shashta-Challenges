# Title- Unique Substring

Naman has a string **S** of size $n$. In one operation, he wants to:

- Select a substring of length $2$ and remove it from the original string.

He is very eager to know the number of possible unique strings generated from this operation. Can you help Naman, in his task **?**

A substring of string **S** is a sequence that can be created from **S** by deleting some characters and without changing the order of the remaining characters.

---
***Input***

The first line of input contains an integer $T$ denoting the number of test cases.

Each test case consists of multiple lines of input:

- The first line of each test case contains $N$ - the length of string.
- The second line contains string $S$ 

---
***Output***

For each testcase, print the number of unique substrings generated after applying operation.

---

***Constraints***

1 <= $t$ <= $10^{4}$

1 <= $N$ <= $2*10^{5}$ 

The second line of the description of each test case contains a string $S$ of length $N$

Consisting of only lowercase letters.

---

***Sample Input***

```
2
6
aaabcc
6
abcdef
```

***Sample Output***

```
4
5
```

***Explanation***

**Test Case: 1:**

You can get the following different strings: `"abcc"` (by deleting the first two or second and third characters), `"aacc"` (by deleting the third and fourth characters), `"aaac"` (by deleting the fourth and the fifth character) and `"aaab"` (by deleting the last two).

**Test Case: 1:**

It can be proved that the number of unique substrings would be not more than 5.

---