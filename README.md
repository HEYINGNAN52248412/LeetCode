# LeetCode Practice 🚀

Algorithm insights from a UCL CS student. Focusing on efficiency and Pythonic logic.

## 📂 Structure
- `hot100/` : Curated solutions for the LeetCode Hot 100 Liked list.
- `1-50/` | `51-100/` : Categorized by Problem ID.

---

## 🔥 LeetCode Hot 100

### 🧩 Hashing

### 0049 - Group Anagrams (Medium)
- **Thoughts**: Anagrams share the same characters with the same frequencies. Using a `set` or `frozenset` as a key is insufficient as it loses frequency data (e.g., "eat" vs "eatt"). 
- **Approach**: 
  - Use a sorted version of the string (`"".join(sorted(s))`) as a canonical key for the hash map to group anagrams.
  - Corrected the previous syntax error where `append` was used with square brackets `[]` instead of parentheses `()`.
  - Implemented a "check-then-initialize" logic to prevent the dictionary from overwriting previous values.
- **Complexity**: **Time $O(N \cdot K \log K)$** | **Space $O(N \cdot K)$**
- **Ref**: [Python Solution](./hot100/Hashing/49_Group-Anagrams.py)

### 0128 - Longest Consecutive Sequence (Medium)
- **Thoughts**: The $O(n)$ constraint rules out sorting ($O(n \log n)$). We must use a Hash Set for $O(1)$ lookups. The key is to avoid redundant checks by only starting a sequence count from its "head" (the smallest element in that sequence).
- **Approach**: 
  - Convert `nums` to a `set` to remove duplicates and enable fast searching.
  - Iterate through the set. If `num - 1` is not present, it marks the start of a new consecutive sequence ("龙头" logic).
  - Use a `while` loop to count the sequence length starting from this head. This ensures each element is visited at most twice, maintaining linear time.
- **Complexity**: **Time $O(n)$** | **Space $O(n)$**
- **Ref**: [Python Solution](./hot100/Hashing/128_Longest-Consecutive-Sequence.py)

### 0560 - Subarray Sum Equals K (Medium)
- **Thoughts**: Moving from $O(n^2)$ to $O(n)$ requires a Hash Map to store previously calculated prefix sums. This is a core technique for range sum queries in unsorted arrays.
- **Approach**: Prefix Sum + Hash Map optimization. We calculate the cumulative sum and look for the specific previous sum that would result in the target $k$ when subtracted.
- **Complexity**: **Time $O(n)$** | **Space $O(n)$**
- **Ref**: [Python Solution](./551-600/560_Subarray-Sum-Equals-K.py)

### 🔗 Linked_List

### 0019 - Remove Nth Node From End of List (Medium)
- **Thoughts**: The `AttributeError` occurs because `fast` can become `None` *before* reaching the `while` loop if $n$ equals the list length.
- **Approach**: 
  - Use a **Dummy Node** to guarantee that `fast` always points to a valid `ListNode` object when the `while` condition is first evaluated.
  - This effectively transforms the "remove head" edge case into a standard "remove middle" operation.
- **Complexity**: **Time $O(L)$** | **Space $O(1)$**
- **Ref**: [Python Solution](./hot100/Linked_List/19_Remove-Nth-Node.py)

### 0021 - Merge Two Sorted Lists (Easy)
- **Thoughts**: Using an iterative approach with a **Dummy Node** is the most memory-efficient way ($O(1)$ space). It avoids the complex "in-place" pointer surgery that can lead to circular references.
- **Approach**: 
  - Create a `dummy` node and a `curr` tracker to build the new list.
  - In each iteration, pick the smaller node, link it to `curr.next`, and move 'curr' forward.
  - Once one list is exhausted, link the remainder of the other list in $O(1)$ time.
- **Complexity**: **Time $O(N + M)$** | **Space $O(1)$**
- **Ref**: [Python Solution](./hot100/Linked_List/21_Merge-Two-Sorted-Lists.py)

### 0023 - Merge k Sorted Lists (Hard)
- **Thoughts**: Merging $k$ lists one by one is inefficient ($O(k^2n)$). Using a **Divide and Conquer** approach allows us to merge pairs of lists, reducing the number of merging operations to a logarithmic scale relative to $k$.
- **Approach**: 
  - Reuse the recursive `merge_two_lists` logic developed in Problem 21.
  - Use an `interval` to pair up lists (e.g., merge list[0] with list[1], list[2] with list[3]). 
  - In each pass, double the `interval` until only one merged list remains at `lists[0]`. 
  - This effectively builds a "merging tree" structure.
- **Complexity**: **Time $O(nk \log k)$** | **Space $O(\log k)$** (due to recursion stack of merge_two_lists and the iterative interval logic)
- **Ref**: [Python Solution](./hot100/Linked_List/23_Merge-k-Sorted-Lists.py)

### 0024 - Swap Nodes in Pairs (Medium)
- **Thoughts**: The `AttributeError: 'NoneType'` often stems from incorrect short-circuit logic in the `while` loop (checking `curr.next.next` before `curr.next`).
- **Approach**: 
  - Use a **Dummy Node** to simplify the head swap, and maintain a strict check: `while curr.next and curr.next.next` to handle both even and odd length lists safely.
  - Implement the three-way pointer re-assignment: `node2.next` to `node1`, `curr.next` points to `node2`, and `node1.next` to the remainder of the list (`node3`).
- **Complexity**: **Time $O(N)$** | **Space $O(1)$**
- **Ref**: [Python Solution](./hot100/Linked_List/24_Swap-Nodes-in-Pairs.py)

### 0025 - Reverse Nodes in k-Group (Hard)
- **Thoughts**: The challenge lies in maintaining list integrity during segmented reversals. The core logic involves isolated group reversal and precise re-stitching of group boundaries.
- **Approach**: 
  - **Reversal Helper**: Uses a three-pointer iterative pattern to flip directionality within a $k$-length window.
  - **Segment Control**: A scouting pointer (`curr_final`) ensures $k$ nodes exist before triggering a flip.
  - **Re-linking**: Explicitly links the `prev_group_tail` to the `new_head` and the `new_tail` to the `remaining_list`.
  - **Pointer Advancement**: Updates the group anchor to the `new_final` after each swap to reset the window.
- **Complexity**: **Time $O(N)$** | **Space $O(1)$**
- **Ref**: [Python Solution](./hot100/Linked_List/25_Reverse-k-Group.py)

### 0138 - Copy List with Random Pointer (Medium)
- **Thoughts**: Deep copying a non-linear linked list requires a way to track the relationship between original and cloned nodes to correctly assign `random` pointers.
- **Approach**: 
  - **Hash Map**: Creates an $O(N)$ mapping from old to new nodes. Simple and reliable.
  - **Interleaving (O(1) Space)**: Temporarily weaves the new nodes into the original list. This allows direct access to cloned nodes via `curr.random.next`, eliminating the need for an auxiliary map.
  - **Index-based**: Maps nodes to indices and searches linearly. Least efficient at $O(N^2)$ time.
- **Complexity**: **Time $O(N)$** | **Space $O(1)$** (Auxiliary)
- **Ref**: [Python Solution](./hot100/Linked_List/138_Copy-List-with-Random-Pointer.py)


## 📝 Solved Problems(Sequential)

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

### 0007 - Reverse Integer (Medium)
- **Thoughts**: Reverse the integer by converting it to a string and using Python's slicing technique. The logic is straightforward, but the real challenge is handling environmental constraints.
- **Approach**: 
  - Convert the absolute value of $x$ to a string and reverse it with `[::-1]`.
  - Explicitly check if the result falls outside the signed 32-bit range $[-2^{31}, 2^{31}-1]$.
- **Stats**: **Time $O(\log_{10} n)$** | **Space $O(\log_{10} n)$** (due to string conversion)
- **Ref**: [Python Solution](./1-50/7_Reverse-Integer.py)

### 0008 - String to Integer (atoi) (Medium)
- **Thoughts**: Decouple the parsing steps (whitespace -> sign -> digits) instead of using complex flag management.
- **Approach**: 
  - Use `lstrip()` for whitespace.Handle sign with simple indexing.
  - Calculate the integer mathematically ($res = res \times 10 + d$) to achieve $O(1)$ extra space.
- **Stats**: **Time $O(n)$** | **Space $O(1)$**
- **Ref**: [Python Solution](./1-50/8_atoi.py)

### 0009 - Palindrome Number (Easy)
- **Thoughts**: Avoid string conversion by reversing only the **latter half** of the integer. 
- **Approach**: 
  - Handle edge cases: negative numbers and numbers ending in 0 (excluding 0 itself).
  - Use the math property $res = res \times 10 + x \% 10$ to build the reversed half.
  - Stop when $x \le reversed\_half$. Compare $x$ with $reversed\_half$ (and handle odd-length digits by `// 10`).
- **Stats**: **Time $O(\log_{10} n)$** | **Space $O(1)$**
- **Ref**: [Python Solution](./1-50/9_Palindrome-Number.py)

### 0011 - Container With Most Water (Medium)
- **Thoughts**: A brute-force $O(n^2)$ approach will timeout. The area is constrained by the shorter bar. To find a larger area, we must move the pointer pointing to the shorter bar to potentially find a taller one.
- **Approach**: **Two Pointers**.
  - Initialize `left` at 0 and `right` at the end of the array.
  - Calculate area and update `max_water` in each step.
  - Move the pointer with the smaller height inward.
- **Stats**: **Time $O(n)$** | **Space $O(1)$**
- **Ref**: [Python Solution](./1-50/11_Container-With-Most-Water.py)

---
*Algorithm + Data Structures = Programs*