### Selection Sort

**Definition:**
Selection sort is a simple comparison-based sorting algorithm.

It works by repeatedly selecting the smallest element from the unsorted sublist and moving it to the sorted sublist.

**Steps:**
1. Find the smallest element in the array.
2. Swap it with the first element.
3. Find the second smallest element in the array.
4. Swap it with the second element.
5. Repeat the process until the entire array is sorted.

**Python Implementation:**
```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
```

**Example:**
```python
arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)
```

### Insertion Sort

**Definition:**
Insertion sort is a simple comparison-based sorting algorithm.

It builds the final sorted array one item at a time.

**Steps:**
1. Start with the second element (assuming the first element is trivially sorted).
2. Compare the current element with the sorted elements before it.
3. Insert the current element into the correct position within the sorted elements.
4. Repeat until the whole array is sorted.

**Python Implementation:**
```python
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
```

**Example:**
```python
arr = [12, 11, 13, 5, 6]
sorted_arr = insertion_sort(arr)
print("Sorted array:", sorted_arr)
```

---

