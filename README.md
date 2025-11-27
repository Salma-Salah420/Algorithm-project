🎯 Project: Algorithms Implementation (Non-Recursive & Recursive)
---------------------------------

This repository contains --two algorithmic tasks --implemented in Python:

Task 4 – Birthday Candles Analysis (Non-Recursive)

Task 7 – K-th Element of Two Sorted Arrays (Recursive)

Both tasks include: input handling, algorithm logic, complexity analysis, and various test cases.
------

📌 Task 4 — Birthday Candles Problem (Non-Recursive)
🔍 Description

The program stores the lengths of birthday candles in an array (size = user’s age). It performs three operations:

Find the largest candle length

Count how many times the largest appears

Check if the array is symmetric

Symmetry is only possible when the array length is odd

The largest value must be exactly in the middle

Left side must mirror the right side
----

🧩 Functions
find_largest(array)

Returns the maximum element in the array.

count_occurrences(array, largest)

Counts how many times the largest value appears.

is_symmetric(array, largest, n)

Checks symmetry using:

Odd length check

Largest element must be in the center

Mirrored comparison of left and right halves
------

🚀 Example Output
Largest candle: 4
Occurrences: 1
Status: symmetric
-----

⏱️ Time Complexity
Function	Complexity
find_largest	O(n)
count_occurrences	O(n)
is_symmetric	O(n)
Total	O(n)
------------------
📌 Task 7 — K-th Element of Two Sorted Arrays (Recursive):
--------
🔍 Description

Given two sorted arrays, the program recursively finds the k-th smallest element in the combined sorted order without merging the arrays.
--------
🧩 Function
k_th_recursive(k_th, arr1, arr2)
-------
Handles:

Empty-array cases

Out-of-range k

Dividing arrays using midpoints

Recursively discarding unnecessary halves (divide-and-conquer)
-------------
🚀 Example Output
Enter k: 5
Enter arr1: [2, 3, 4, 5]
Enter arr2: [1, 6, 7, 8, 9, 10]
Output: 6
-----------
⏱️ Time Complexity

Worst case: O(log n)

Best case: O(1) (base case reached immediately)

🧪 Test Cases Included

Valid symmetric vs non-symmetric arrays

Checking largest element and repetition
------------

Valid inputs, invalid inputs (unsorted arrays)

k within bounds and out-of-range scenarios
