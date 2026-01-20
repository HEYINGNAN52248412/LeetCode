# LeetCode Practice 🚀

Algorithm insights from a UCL CS student. Focusing on efficiency and Pythonic logic.

## 📂 Structure
- `1-50/` | `51-100/` : Categorized by Problem ID.
- `notes/` : Reusable algorithm templates.

---

## 📝 Solved Problems

### 0001 - Two Sum
- **Thoughts**: Brute force is $O(n^2)$. Optimal way is to "look back" using a Hash Map to find the complement (`target - n`).
- **Approach**: One-pass Dictionary to store `{value: index}`.
- **Stats**: **Time $O(n)$** | **Space $O(n)$**
- **Ref**: [Python Solution](./1-50/1_Two-Sum.py)

### 0002 - Add Two Numbers
- **Thoughts**: Standard math addition logic. Use a **Dummy Node** to avoid handling the head node as a special case.
- **Approach**: Traverse both lists while maintaining a `carry` variable. Create a new `ListNode` for each digit sum and link them.
- **Stats**: **Time $O(\max(m, n))$** | **Space $O(\max(m, n))$**
- **Ref**: [Python Solution](./1-50/2_Add-Two-Numbers.py)

### 0003 - Longest Substring Without Repeating Characters
- **Thoughts**: Use a **Sliding Window** with a Hash Map to track the last seen index of each character. This avoids unnecessary re-scanning.
- **Approach**: Maintain two integer "pointers" (`left` and `right`). When a duplicate is found within the window, jump the `left` pointer to the position after the previous occurrence.
- **Stats**: **Time $O(n)$** | **Space $O(\min(m, n))$**
- **Ref**: [Python Solution](./1-50/3_Longest-Substring.py)

### 0004 - Median of Two Sorted Arrays (Hard)
- **Thoughts**: Binary search on the partition position of the smaller array. By ensuring $L_1 \le R_2$ and $L_2 \le R_1$, we find the median without merging.
- **Approach**: 
  - Swap arrays to ensure $O(\log(\min(m, n)))$.
  - Use virtual boundaries ($-\infty$, $+\infty$) for seamless edge-case handling.
  - Implement precise $O(\log n)$ index jumping for the binary search bounds.
- **Stats**: **Time $O(\log(\min(m, n)))$** | **Space $O(1)$**
- **Ref**: [Python Solution](./1-50/4_Median-Two-Arrays.py)

### 0005 - Longest Palindromic Substring (Medium)
- **Thoughts**: A palindromic string is symmetric around its center. By iterating through every possible center—including each character (odd length) and each gap between characters (even length)—we can expand outwards to find the maximum boundaries.
- **Approach**: **Expand Around Center**. 
  - For each index $i$, we consider two cases: a single-character center `expand(s, i, i)` and a two-character center `expand(s, i, i+1)`.
  - The `while` loop continues as long as characters on both sides match and the pointers remain within bounds.
  - This avoids the $O(n^2)$ space requirement of Dynamic Programming while maintaining the same time efficiency.
- **Stats**: **Time $O(n^2)$** | **Space $O(1)$**
- **Ref**: [Python Solution](./1-50/5_Longest-Palindrome.py)

### 0006 - Zigzag Conversion (Medium)
- **Thoughts**: Simulate the row-by-row "falling" process using an oscillating row pointer.
- **Approach**: Iterate through the string and append characters to a row list. Flip the traversal direction ($\pm 1$) whenever the top or bottom row is reached.
- **Stats**: **Time $O(n)$** | **Space $O(n)$**
- **Ref**: [Python Solution](./1-50/6_Zigzag-Conversion.py)

---
*Algorithm + Data Structures = Programs*