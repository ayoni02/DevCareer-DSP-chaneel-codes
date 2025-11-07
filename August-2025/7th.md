# August 7th Problems

## Problem 1: Filter the Number

**Description:**

Oh, no! The number has been mixed up with the text. Your goal is to retrieve the number from the text, can you return the number back to its original state?

**Task:**

Your task is to return a number from a string.

**Details:**

You will be given a string of numbers and letters mixed up, you have to return all the numbers in that string in the order they occur.

**Examples:**

```
"a1b2c3" → 123
"abc123def456" → 123456
"hello5world3" → 53
```

---

## Problem 2: Remove First and Last Character Part Two

**Description:**

This is a spin off of the first kata. You are given a string containing a sequence of character sequences separated by commas.

Write a function which returns a new string containing the same character sequences except the first and last ones but this time separated by spaces.

**Rules:**

- If the input string is empty or the removal of the first and last items would cause the resulting string to be empty, return an empty value (represented as `NULL`)

**Examples:**

```
"1,2,3" → "2"
```

```
"1,2,3,4" → "2 3"
```

```
"1,2,3,4,5" → "2 3 4"
```

```
"" → NULL
```

```
"1" → NULL
```

```
"1,2" → NULL
```

---

## Problem 3: Odd-Even String Sort

**Description:**

Given a string `s`, your task is to return another string such that even-indexed and odd-indexed characters of `s` are grouped and the groups are space-separated. Even-indexed group comes as first, followed by a space, and then by the odd-indexed part.

**Example:**

```
Input: "CodeWars"
Output: "CdWr oeas"

Breakdown:
         C o d e W a r s
indices: 0 1 2 3 4 5 6 7

Even indices (0, 2, 4, 6): "CdWr"
Odd indices (1, 3, 5, 7): "oeas"

Final output: "CdWr oeas"
```

**Notes:**
- Tested strings are at least 8 characters long

---

## Problem 4: Simple Calculator

**Description:**

You are required to create a simple calculator that returns the result of addition, subtraction, multiplication or division of two numbers.

**Function Arguments:**

Your function will accept three arguments:
1. The first argument should be a number
2. The second argument should be a number
3. The third argument should represent a sign indicating the operation to perform on these two numbers

**Return Value:**

You should return the result of applying the given operation to these numbers.

**Special Cases:**

- **In dynamically typed languages (JS, PHP, Python):** The first and second arguments can be not numbers. In that case, return `"unknown value"`
- If the given operation to perform on the two numbers is not one of the four mentioned above (`+`, `-`, `*`, `/`), return `"unknown value"`

**Examples:**

```
calculator(1, 2, "+") → 3
```

```
calculator(1, 2, "&") → "unknown value"
Explanation: "&" is not a valid operation
```

```
calculator(1, "k", "*") → "unknown value"
Explanation: Second argument is not a number (for dynamically-typed languages)
```

**Good luck!**