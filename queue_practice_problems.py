# UC6 – Reverse a queue using stack.

from collections import deque


class Queue:
    """
    Queue implementation using deque for O(1) operations.
    """

    def __init__(self) -> None:
        self.items = deque()

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def enqueue(self, item) -> None:
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.popleft()

    def display(self) -> None:
        print(list(self.items))


def reverse_queue(queue: Queue) -> None:
    """
    Reverse queue using stack.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    stack = []

    # Step 1: Move all elements to stack
    while not queue.is_empty():
        stack.append(queue.dequeue())

    # Step 2: Push back to queue (reversed)
    while stack:
        queue.enqueue(stack.pop())


def main() -> None:
    queue = Queue()

    # Add elements
    for i in [1, 2, 3, 4, 5]:
        queue.enqueue(i)

    print("Original Queue:")
    queue.display()

    reverse_queue(queue)

    print("Reversed Queue:")
    queue.display()


if __name__ == "__main__":
    main()