# UC5 – Implement queue using collections.deque for optimized performance.

from collections import deque


class Queue:
    """
    Optimized Queue implementation using collections.deque.

    Provides O(1) enqueue and dequeue operations.
    """

    def __init__(self) -> None:
        # Using deque for efficient operations
        self.items = deque()

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def size(self) -> int:
        return len(self.items)

    def enqueue(self, item) -> None:
        """
        Add element to rear of queue.

        Time Complexity: O(1)
        """
        self.items.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        """
        Remove element from front of queue.

        Time Complexity: O(1)
        """
        if self.is_empty():
            print("Queue Underflow. Cannot dequeue from empty queue.")
            return None

        removed = self.items.popleft()
        print(f"Dequeued: {removed}")
        return removed

    def peek(self):
        """
        Return front element without removing it.

        Time Complexity: O(1)
        """
        if self.is_empty():
            print("Queue is empty. No front element.")
            return None

        return self.items[0]


def main() -> None:
    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    print(f"Front element: {queue.peek()}")
    print(f"Queue size: {queue.size()}")

    queue.dequeue()
    queue.dequeue()

    print(f"Front after dequeue: {queue.peek()}")
    print(f"Queue size: {queue.size()}")


if __name__ == "__main__":
    main()