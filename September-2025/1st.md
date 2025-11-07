# September 1st Programming Problems

## Problem 1: Cookie Mystery

**Description:**

Create a program that determines who ate the last cookie based on the input type:
- If the input is a **string** → "Zach" ate the cookie
- If the input is a **float** or **int** → "Monica" ate the cookie
- If the input is anything else → "the dog" ate the cookie

**Output Format:**
```
Who ate the last cookie? It was (name)!
```

**Example:**
```
Input: "hi"
Output: "Who ate the last cookie? It was Zach!"
```
*(Zach is returned because the input is a string)*

**Note:** Ensure correct spacing and punctuation in your output.

---

## Problem 2: Race to Person 3

**Description:**

You are given three integers `x`, `y`, and `z` representing positions of three people on a number line:
- `x` is the position of Person 1
- `y` is the position of Person 2
- `z` is the position of Person 3 (stationary)

Both Person 1 and Person 2 move toward Person 3 at the same speed. Determine who reaches Person 3 first.

**Return Values:**
- `1` if Person 1 arrives first
- `2` if Person 2 arrives first
- `0` if both arrive at the same time

**Examples:**

**Example 1:**
```
Input: x = 2, y = 7, z = 4
Output: 1
Explanation: Person 1 is 2 steps away (|2-4| = 2), Person 2 is 3 steps away (|7-4| = 3)
```

**Example 2:**
```
Input: x = 2, y = 5, z = 6
Output: 2
Explanation: Person 1 is 4 steps away (|2-6| = 4), Person 2 is 1 step away (|5-6| = 1)
```

**Example 3:**
```
Input: x = 1, y = 5, z = 3
Output: 0
Explanation: Both are 2 steps away (|1-3| = 2, |5-3| = 2)
```

---

## Problem 3: Square Root (Integer)

**Description:**

Given a non-negative integer `x`, return the square root of `x` rounded down to the nearest integer. The returned integer must be non-negative.

**Constraints:**
- You **must not** use any built-in exponent function or operator
- Do not use `pow(x, 0.5)` in C++ or `x ** 0.5` in Python
- `0 <= x <= 2³¹ - 1`

**Examples:**

**Example 1:**
```
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2
```

**Example 2:**
```
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., rounded down gives 2
```

---

## Problem 4: Fix String Case

**Description:**

You will be given a string that may have mixed uppercase and lowercase letters. Your task is to convert that string to either lowercase only or uppercase only based on making as few changes as possible.

**Rules:**
- Convert to the case that requires the fewest changes
- If the string contains an **equal number** of uppercase and lowercase letters, convert the string to **lowercase**

**Examples:**

```
solve("coDe") = "code"
Explanation: Lowercase characters (3) > uppercase characters (1). Change only "D" to lowercase.
```

```
solve("CODe") = "CODE"
Explanation: Uppercase characters (3) > lowercase characters (1). Change only "e" to uppercase.
```

```
solve("coDE") = "code"
Explanation: Uppercase (2) == lowercase (2). Change all to lowercase.
```