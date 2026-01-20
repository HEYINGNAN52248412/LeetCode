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

---
*Algorithm + Data Structures = Programs*