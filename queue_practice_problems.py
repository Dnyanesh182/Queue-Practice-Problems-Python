# UC9 – Solve sliding window maximum problem using deque.

from collections import deque


def sliding_window_max(arr: list[int], k: int) -> list[int]:
    """
    Find maximum of each sliding window of size k.

    Time Complexity: O(n)
    Space Complexity: O(k)
    """
    if not arr or k <= 0:
        return []

    dq = deque()  # stores indices
    result = []

    for i in range(len(arr)):
        # Remove indices out of window
        while dq and dq[0] <= i - k:
            dq.popleft()

        # Remove smaller elements from rear
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()

        dq.append(i)

        # Add max to result when window is ready
        if i >= k - 1:
            result.append(arr[dq[0]])

    return result


def main() -> None:
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    result = sliding_window_max(arr, k)

    print(f"Input: {arr}")
    print(f"Window size: {k}")
    print(f"Sliding Window Maximum: {result}")


if __name__ == "__main__":
    main()