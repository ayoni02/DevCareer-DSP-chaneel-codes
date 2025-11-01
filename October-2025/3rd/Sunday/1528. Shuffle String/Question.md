Leetcode:https://leetcode.com/problems/shuffle-string/description <br>
Topic: 1528. Shuffle String
<br>
You are given a string s and an integer array indices of the same length. The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
<br>
Return the shuffled string.
<br><br>
Example 1:<br>
<img width="321" height="243" alt="image" src="https://github.com/user-attachments/assets/9718a17e-887d-47a8-924f-0b21f365ef4f" /><br>
Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]<br>
Output: "leetcode"<br>
Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.<br>
<br>
Example 2:<br>
Input: s = "abc", indices = [0,1,2]<br>
Output: "abc"<br>
Explanation: After shuffling, each character remains in its position.<br>
<br>
Constraints:<br>
* s.length == indices.length == n<br>
* 1 <= n <= 100<br>
* s consists of only lowercase English letters.<br>
* 0 <= indices[i] < n<br>
* All values of indices are unique.<br>
<br>
Tags: Array String
