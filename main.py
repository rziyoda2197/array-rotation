def rotate_array(arr, k):
    k = k % len(arr)
    return arr[-k:] + arr[:-k]
```

```python
# Test qilish
arr = [1, 2, 3, 4, 5]
k = 2
print(rotate_array(arr, k))  # Chiqaradi: [4, 5, 1, 2, 3]
```

```python
# Test qilish
arr = [1, 2, 3, 4, 5]
k = 7
print(rotate_array(arr, k))  # Chiqaradi: [4, 5, 1, 2, 3]
```

```python
# Test qilish
arr = [1, 2, 3, 4, 5]
k = 0
print(rotate_array(arr, k))  # Chiqaradi: [1, 2, 3, 4, 5]
