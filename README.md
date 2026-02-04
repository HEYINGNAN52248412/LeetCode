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

### 0141 - Linked List Cycle (Easy)
- **Thoughts**: The ultimate speed limit is $O(n)$. While Hash Sets are fast in Python, the **Fast/Slow Pointer** approach is the theoretical "gold standard" for its $O(1)$ space efficiency.
- **Approach**: 
  - Standard: Floyd's Cycle-Finding Algorithm (Fast/Slow pointers).
  - Optimized for Python Time: Hash Set to store visited node identities.
  - "Destructive" Optimization: Re-linking nodes to a sentinel value to detect re-visitation in $O(n)$ time and $O(1)$ space.
- **Complexity**: **Time $O(n)$** | **Space $O(1)$ or $O(n)$**
- **Ref**: [Python Solution](./hot100/Linked_List/141_Linked-List-Cycle.py)

### 0142 - Linked List Cycle II (Medium)
- **Thoughts**: Building on Floyd's Cycle-Finding Algorithm. Detecting the cycle is step one; locating the entry requires understanding the mathematical relationship $a = kL - b$.
- **Approach**: 
  - Phase 1: Use fast and slow pointers to find the collision point.
  - Phase 2: Reset a new pointer to `head` and move it alongside the slow pointer at equal speed. Their meeting point is the cycle's entrance.
  - Ensures $O(1)$ space by utilizing existing list pointers.
- **Complexity**: **Time $O(N)$** | **Space $O(1)$**
- **Ref**: [Python Solution](./hot100/Linked_List/142_Linked-List-Cycle-II.py)

### 0146 - LRU Cache (Medium)
- **Thoughts**: The optimal approach for $O(1)$ time is combining a **Hash Map** (for location) and a **Doubly Linked List** (for order). Attempts to avoid auxiliary space would lead to $O(N)$ lookup times, which is unacceptable for caching systems.
- **Approach**: 
  - Utilize a private `self.key_map` to store node references, ensuring isolation between test cases.
  - Implement **Dummy Nodes** at both ends of the list to simplify node extraction and insertion.
  - Maintain a `current_num` counter and decrement it upon eviction to keep the cache within bounds.
- **Complexity**: **Time $O(1)$** | **Space $O(Capacity)$**
- **Ref**: [Python Solution](./hot100/Linked_List/146_LRU-Cache.py)

### 0148 - Sort List (Medium)
- **Thoughts**: Theoretically, splitting a list into $k$ parts (k-way merge) reduces recursion depth to $\log_k n$. However, the complexity remains $O(n \log n)$ because the cost of merging $k$ elements increases proportionally.
- **Approach**: 
  - Standard Merge Sort uses 2-way splitting (binary) because it is the most efficient balance for in-memory comparisons.
  - For linked lists, the lack of random access makes $k$-way splitting even less attractive compared to the simple fast/slow pointer binary split.
- **Complexity**: **Time $O(n \log n)$** | **Space $O(\log n)$**
- **Ref**: [Python Solution](./hot100/Linked_List/148_Sort-List.py)

### 0160 - Intersection of Two Linked Lists (Easy)
- **Thoughts**: The two-pointer switch strategy naturally handles non-intersecting cases because the traversal lengths $L_A + L_B$ and $L_B + L_A$ are identical. If no intersection exists, both pointers will eventually equal `None` at the same time, satisfying the loop's exit condition.
- **Approach**: 
  - Iteratively move `pA` and `pB`. 
  - Reassign to the opposite head upon reaching `None`. 
  - The loop terminates either at the intersection node or at `None`.
- **Complexity**: **Time $O(M+N)$** | **Space $O(1)$**
- **Ref**: [Python Solution](./hot100/Linked_List/160_Intersection-of-Two-Linked-Lists.py)

### 0206 - Reverse Linked List (Easy)
- **Thoughts**: The foundational operation for many complex list problems (e.g., #25, #92). It demonstrates the power of iterative pointer manipulation to change list directionality without auxiliary space.
- **Approach**: 
  - Use a three-pointer iterative pattern (`prev`, `curr`, `temp`).
  - Update `curr.next` to point to `prev` at each step.
  - Carefully manage the movement of pointers to avoid losing list references.
- **Complexity**: **Time $O(N)$** | **Space $O(1)$**
- **Ref**: [Python Solution](./hot100/Linked_List/206_Reverse-Linked-List.py)

### 0234 - Palindrome Linked List (Easy)
- **Thoughts**: A perfect integration of basic linked list operations. To achieve $O(1)$ space, we must modify the list in-place rather than using an auxiliary array.
- **Approach**: 
  - **Find Mid**: Use fast/slow pointers to locate the center of the list.
  - **Reverse Second Half**: Reverse the nodes from the midpoint to the end using the three-pointer pattern.
  - **Compare**: Iterate through both halves simultaneously, checking for value parity.
  - **Edge Cases**: Handles single-node or empty lists via initial guard clauses.
- **Complexity**: **Time $O(N)$** | **Space $O(1)$**
- **Ref**: [Python Solution](./hot100/Linked_List/234_Palindrome-Linked-List.py)

### 👐 Two_Pointers

### 0011 - Container With Most Water (Medium)
- **Thoughts**: A classic application of the two-pointer technique combined with a greedy strategy. The key insight is that moving the pointer at the shorter height is the only way to potentially increase the area as the width decreases.
- **Approach**: 
  - Initialize pointers at the start (`left`) and end (`right`) of the array.
  - Calculate area using $\min(height[left], height[right]) \times (right - left)$.
  - Move the pointer pointing to the shorter line inward.
  - Maintain a global `max_water` variable to track the best result found.
- **Complexity**: **Time $O(n)$** | **Space $O(1)$**
- **Ref**: [Python Solution](./hot100/Two_Pointers/11_Container-With-Most-Water.py)

### 0015 - 3Sum (Medium)
- **Thoughts**: The prerequisite for an $O(n^2)$ two-pointer solution is a **sorted array**. The main challenge is avoiding duplicate triplets without using expensive hash sets.
- **Approach**: 
  - **Sorting**: Enables the two-pointer "clamping" logic.
  - **Fixed Pointer (i)**: Iterates through the list; skip if `nums[i] == nums[i-1]`.
  - **Moving Pointers (j, k)**: Shrink towards the middle based on the sum.
  - **Internal De-duplication**: After finding a valid triplet, increment `j` and decrement `k` past any identical values.
- **Complexity**: **Time $O(n^2)$** | **Space $O(1)$**
- **Ref**: [Python Solution](./hot100/Two_Pointers/15_3-Sum.py)

### 0042 - Trapping Rain Water (Hard)
- **Thoughts**: The water trapped at any position is limited by the minimum of the maximum heights to its left and right. By always moving the pointer with the smaller current height, we ensure that the historical maximum on that specific side is the true bottleneck, while the taller opposite pointer serves as a guaranteed "dam".
- **Approach**: 
  - Initialize `left` and `right` pointers at array ends and track `left_max` and `right_max`.
  - Compare `height[left]` and `height[right]`; process the shorter side to maintain the bottleneck invariant.
  - Update the side's historical max and add (`max - current_height`) to the total if the current height is lower than the max.
- **Complexity**: **Time $O(N)$** | **Space $O(1)$**
- **Ref**: [Python Solution](./hot100/Two_Pointers/42_Trapping-Rain-Water.py)

### 0283 - Move Zeroes (Easy)
- **Thoughts**: A classic application of the "Fast-Slow Pointer" technique to modify an array in-place without using extra space. By swapping instead of inserting, we maintain $O(n)$ time complexity.
- **Approach**: 
  - Initialize `slow = 0` to track the position where the next non-zero element should go.
  - Use `fast` to scan the array.
  - When `nums[fast] != 0`, swap `nums[fast]` with `nums[slow]` and increment `slow`.
  - This effectively pushes all zeros to the end while preserving the relative order of non-zero elements.
- **Complexity**: **Time $O(n)$** | **Space $O(1)$**
- **Ref**: [Python Solution](./hot100/Two_Pointers/283_Move-Zeroes.py)

### 🪟Sliding_Window

### 0003 - Longest Substring Without Repeating Characters (Medium)
- **Thoughts**: A classic sliding window problem optimized with a Hash Map to store the last seen index of each character. This allows the left pointer to "jump" rather than crawl, achieving true linear time.
- **Approach**: 
  - Use `right` pointer to expand the window and add characters to `char_map`.
  - When a duplicate is found, update `left` to `max(left, char_map[char] + 1)`.
  - The `max` function is crucial to prevent the `left` pointer from moving backwards.
  - Update `max_length` at each step: $right - left + 1$.
- **Complexity**: **Time $O(n)$** | **Space $O(min(m, n))$** (where $m$ is the character set size).
- **Ref**: [Python Solution](./hot100/Sliding_Window/3_Longest-Substring-Without-Repeating-Characters.py)

### 0076 - Minimum Window Substring (Hard)
- **Thoughts**: The ultimate challenge of the sliding window technique. The core optimization is replacing expensive hash map comparisons ($O(K)$) with an integer counter (`full_fill_char_nums`) to track how many unique characters in $t$ have met their required frequency.
- **Approach**: 
  - **Preprocessing**: Build a target frequency map for $t$ and track the number of unique characters needed.
  - **Expansion**: Move the `right` pointer to include characters in the window, updating the `window_map` and the `full_fill_char_nums` counter whenever a requirement is precisely met.
  - **Contraction**: While the window is "valid" (all characters satisfied), record the minimum window indices and shrink the `left` pointer to find the local optimal.
  - **State Management**: If a character removed from the left causes it to fall below the required frequency, decrement the `full_fill_char_nums` counter.
- **Complexity**: **Time $O(S + T)$** | **Space $O(K)$** where $K$ is the size of the character set (e.g., 52 for letters).
- **Ref**: [Python Solution](./hot100/Sliding_Window/76_Minimum-Window-Substring.py)

### 0239 - Sliding Window Maximum (Hard)
- **Thoughts**: The Monotonic Deque is the key to solving this in linear time. By maintaining indices in a deque such that their values are strictly decreasing, we can find the maximum of any window in $O(1)$.
- **Approach**: 
  - Use `collections.deque` to store **indices**.
  - **Maintain Monotonicity**: Before appending index `i`, `pop()` from the back while `nums[i] >= nums[deque[-1]]`.
  - **Boundary Check**: If the front index is `i - k`, it's out of the window; `popleft()`.
  - **Result Extraction**: Once the first window forms (`i >= k-1`), the current max is `nums[deque[0]]`.
- **Complexity**: **Time $O(N)$** | **Space $O(K)$**
- **Ref**: [Python Solution](./hot100/Sliding_Window/239_Sliding-Window-Maximum.py)

### 0438 - Find All Anagrams in a String (Medium)
- **Thoughts**: This is a classic "Fixed-size Sliding Window" problem. The core idea is to maintain a frequency map of the current window and compare it with the target frequency map of string $p$.
- **Approach**: 
  - Initialize `p_map` with character frequencies of $p$.
  - Slide a window of length `len(p)` over string $s$.
  - On each step: increment the count of the new character and decrement the count of the character that just left the window.
  - **Crucial**: If a character's count drops to zero, `del` it from the map to ensure the `==` operator works correctly between dictionaries.
- **Complexity**: **Time $O(N)$** (where $N$ is `len(s)`, since dictionary comparison is $O(26)$) | **Space $O(1)$** (since the map size is capped by the alphabet).
- **Ref**: [Python Solution](./hot100/Sliding_Window/438_Find-All-Anagrams-in-a-String.py)


### 🤑 Greedy

### 0045 - Jump Game II (Medium)
- **Thoughts**: The core greedy logic relies on "Range Expansion." We don't care about the specific intermediate landing spots, only the maximum reach each jump provides.
- **Approach**: 
  - `i` acts as a scout within the `current_jump_end`.
  - `farthest` captures the best possible next step.
  - `step` is incremented only when the current range is exhausted, signaling a mandatory jump to the next optimal range.
- **Complexity**: **Time $O(N)$** | **Space $O(1)$**
- **Ref**: [Python Solution](./hot100/Greedy/45_Jump-Game-II.py)

### 0055 - Jump Game (Medium)
- **Thoughts**: This problem reduces the goal to "Range Coverage" without the need to count "Range Transitions." We only care if the "scout" stays within the bounds of our maximum possible reach.
- **Approach**: 
  - `i` acts as a scout exploring the array tile by tile.
  - `farthest` captures the absolute best reach discovered by the scout so far.
  - If the scout `i` ever exceeds the `farthest` point, it means he has hit a gap he cannot jump over; return `False`.
  - If `farthest` covers or exceeds the final index at any point, the path is confirmed; return `True`.
- **Complexity**: **Time O(N)** | **Space O(1)**
- **Ref**: [Python Solution](./hot100/Greedy/55_Jump-Game.py)

### 0121 - Best Time to Buy and Sell Stock (Easy)
- **Thoughts**: The goal is to find the maximum difference between a historical minimum price and a subsequent higher price. Instead of checking all pairs ($O(N^2)$), we maintain the "global minimum" seen so far to calculate potential profit in a single pass.
- **Approach**: 
  - Initialize `min_price` to infinity and `max_profit` to 0.
  - Iterate through the `prices` array once.
  - Update `min_price` if the current day's price is lower than the recorded minimum.
  - Otherwise, calculate the potential profit by subtracting `min_price` from the current price and update `max_profit` if this value is higher than the current maximum.
- **Complexity**: **Time $O(N)$** | **Space $O(1)$**
- **Ref**: [Python Solution](./hot100/DP/121_Best-Time-to-Buy-and-Sell-Stock.py)

### 0763 - Partition Labels (Medium)
- **Thoughts**: This problem utilizes a greedy "boundary extension" strategy similar to Jump Game II. To ensure each character appears in at most one part, a partition must extend at least to the last occurrence of every character it contains.
- **Approach**: 
  - **First Pass**: Traverse the string to build a hash map storing the last-seen index of every character.
  - **Second Pass**: Iterate through the string and maintain a `cut_point` (boundary) representing the maximum last-seen index of all characters encountered in the current segment.
  - **Cutting**: When the current index `i` matches the `cut_point`, it signifies that all characters within the current range have no further appearances later in the string; record the partition size and reset the start marker.
- **Complexity**: **Time $O(N)$** | **Space $O(1)$** (The hash map stores a maximum of 26 lowercase English letters).
- **Ref**: [Python Solution](./hot100/Greedy/763_Partition-Labels.py)

## 🌲 Binary Tree

### 0094 - Binary Tree Inorder Traversal (Easy)
- **Thoughts**: The stack simulates recursion by remembering parent nodes. A `pop()` occurs only when the inner loop hits the leftmost end (`curr is None`), signaling that the current node's left subtree is finished. Since the left side is "done," we only need to visit the node and pivot to the right.
- **Approach**: 
  - **Dive Left**: Use an inner `while curr:` loop to push nodes onto the stack until `curr` reaches the bottom-left `None`.
  - **Backtrack**: The program "returns" to the parent by popping from the stack, appending its value, and moving to `curr.right`.
  - **Repeat**: If a right child exists, the "Dive Left" process starts over for that subtree; otherwise, it pops the next parent.
- **Complexity**: **Time $O(N)$** | **Space $O(H)$**.
- **Ref**: [Python Solution](./hot100/Binary_Tree/94_Binary-Tree-Inorder-Traversal.py)

### 0098 - Validate Binary Search Tree (Medium)
- **Thoughts**: A tree is a valid BST if and only if its in-order traversal yields a strictly increasing sequence. We utilize the stack-based iterative traversal to verify this property in a single pass.
- **Approach**: 
  - **Dive Left**: Use the standard `while curr:` loop to hit the bottom-left `None`. This triggers the "Backtrack" phase by popping the stack.
  - **The "Left is Done" Insight**: Every time we pop a node, we are returning from its left child. This ensures the entire left subtree is already verified, so we only need to compare the current value with the `prev` value and then pivot to the right.
  - **Validation**: Initialize `prev` as `-float('inf')` to ensure the first (smallest) node doesn't trigger a false negative.
  - **Shift**: Move to `curr.right` to continue the verification for the rest of the tree.
- **Complexity**: **Time $O(N)$** | **Space $O(H)$**.
- **Ref**: [Python Solution](./hot100/Binary_Tree/98_Validate-BST.py)

### 0101 - Symmetric Tree (Easy)
- **Thoughts**: A tree is symmetric if its left and right subtrees are mirrors of each other. Instead of creating lists, we compare nodes in pairs: the outer children must match, and the inner children must match.
- **Approach**: 
  - **Recursive (DFS)**: Use a helper function `isMirror(L, R)`. If both are null, return true; if one is null or values differ, return false. Recursively check `(L.left, R.right)` and `(L.right, R.left)`.
  - **Iterative (BFS)**: Use a `queue` to store pairs of nodes that should be identical. Pop two nodes at a time, compare them, and push their respective children in mirrored order (outer pairs then inner pairs).
- **Complexity**: **Time $O(N)$** | **Space $O(H)$** for DFS or **$O(W)$** for BFS.
- **Ref**: [Python Solution](./hot100/Binary_Tree/101_Symmetric-Tree.py)

### 0102 - Binary Tree Level Order Traversal (Medium)
- **Thoughts**: Level order traversal is a Breadth-First Search (BFS) application. Unlike DFS which dives deep, BFS uses a FIFO queue to sweep the tree layer by layer. The "Level Isolation" trick—capturing the queue's size before the loop starts—is essential to separate nodes of different depths within a single queue.
- **Approach**: 
  - **Level Isolation**: In each `while` iteration, measure `len(queue)` to define the boundary of the current level.
  - **FIFO Processing**: Use a `for` loop to `popleft()` exactly that many nodes. This ensures we "clear the floor" before moving to nodes added during the current sweep.
  - **Child Expansion**: For each node processed, append its existing (non-null) `left` and `right` children to the back of the queue.
  - **Collection**: Append the results of each `for` loop into the final `ans` list to maintain the nested structure.
- **Complexity**: **Time $O(N)$** | **Space $O(W)$** ($W$ is the maximum width of the tree).
- **Ref**: [Python Solution](./hot100/Binary_Tree/102_Level-Order-Traversal.py)

### 0104 - Maximum Depth of Binary Tree (Easy)
- **Thoughts**: While DFS (recursion) is the most concise way to find depth, BFS (Level Order) provides a literal count of the tree's layers. Iterative DFS with a stack is tricky for depth because the stack height fluctuates during backtracking and doesn't always reflect the leaf's actual depth.
- **Approach**: 
  - **Level-by-Level**: Use a `queue` to perform a standard BFS.
  - **Depth Counter**: Increment a `depth` variable each time the `while queue:` loop starts a new level.
  - **Exhaustion**: Use the `len(queue)` trick to process all nodes at the current level before moving to the next, ensuring the counter accurately reflects the number of layers traversed.
- **Complexity**: **Time $O(N)$** | **Space $O(W)$** ($W$ is the maximum width of the tree).
- **Ref**: [Python Solution](./hot100/Binary_Tree/104_Maximum-Depth.py)

### 0105 - Construct Binary Tree from Preorder and Inorder Traversal (Medium)
- **Thoughts**: The core logic relies on Pre-order identifying the root and In-order partitioning the tree. A common pitfall is confusing the `TreeNode` object with its `int` value during search. For efficiency, especially in UCL COMP0005 context, we recognize that In-order length dictates the split in the Pre-order array.
- **Approach**: 
  - **Base Case**: Return `None` if input arrays are empty.
  - **Root Identification**: The first element of `preorder` is the root. Locate its index in `inorder` to determine subtree sizes.
  - **Left**: Use the first `root_index` elements following the root in `preorder`.
  - **Right**: Use the remaining elements in `preorder`.
  - **Recursive Build**: Reconstruct the `root.left` and `root.right` by passing these partitioned slices back into the function.
- **Complexity**: **Time $O(N^2)$** (due to `.index()` and slicing in each call) | **Space $O(N)$**. To optimize to $O(N)$ time, use a Hash Map for index lookups.
- **Ref**: [Python Solution](./hot100/Binary_Tree/105_Construct-Tree.py)

### 0108 - Convert Sorted Array to Binary Search Tree (Easy)
- **Thoughts**: To ensure the BST is height-balanced, we must pick the median of the sorted array as the root. This ensures the number of nodes in the left and right subtrees is as equal as possible, maintaining a height of $O(\log N)$.
- **Approach**: 
  - **Find Mid**: Calculate the middle index `mid = len(nums) // 2`.
  - **Root Creation**: Create a `TreeNode` using `nums[mid]`.
  - **Divide and Conquer**: 
    - Recursively build the `left` subtree using the slice `nums[:mid]`.
    - Recursively build the `right` subtree using the slice `nums[mid+1:]`.
  - **Base Case**: If the array is empty, return `None`.
- **Complexity**: **Time $O(N)$** | **Space $O(\log N)$** (for the recursion stack, excluding the space for the tree itself).
- **Ref**: [Python Solution](./hot100/Binary_Tree/108_Sorted-Array-To-BST.py)



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