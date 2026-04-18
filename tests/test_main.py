import pytest

def rotate_array(arr, k):
    k = k % len(arr)
    return arr[-k:] + arr[:-k]

@pytest.mark.parametrize("arr, k, expected", [
    ([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3]),
    ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),
    ([1, 2, 3, 4, 5], 7, [4, 5, 1, 2, 3]),
    ([1, 2, 3, 4, 5], 0, [1, 2, 3, 4, 5]),
    ([], 2, []),
    ([1], 2, [1]),
])
def test_rotate_array(arr, k, expected):
    assert rotate_array(arr, k) == expected
