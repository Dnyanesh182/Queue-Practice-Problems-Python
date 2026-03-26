# UC7 – Generate binary numbers from 1 to N using queue.

from collections import deque


def generate_binary(n: int) -> list[str]:
    """
    Generate binary numbers from 1 to N using queue.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    result = []
    queue = deque()

    queue.append("1")

    for _ in range(n):
        current = queue.popleft()
        result.append(current)

        queue.append(current + "0")
        queue.append(current + "1")

    return result


def main() -> None:
    n = 5
    binaries = generate_binary(n)

    print(f"Binary numbers from 1 to {n}:")
    print(binaries)


if __name__ == "__main__":
    main()