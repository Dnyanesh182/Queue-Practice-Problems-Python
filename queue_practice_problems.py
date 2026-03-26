# UC3 – Check if the queue is empty and handle underflow conditions.

class Queue:
    """
    Queue implementation using Python list.

    Supports enqueue, dequeue, peek, and is_empty operations.
    """

    def __init__(self) -> None:
        self.items = []

    def is_empty(self) -> bool:
        """
        Check if queue is empty.

        Time Complexity: O(1)
        """
        return len(self.items) == 0

    def enqueue(self, item) -> None:
        self.items.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow. Cannot dequeue from empty queue.")
            return None

        removed = self.items.pop(0)
        print(f"Dequeued: {removed}")
        return removed

    def peek(self):
        if self.is_empty():
            print("Queue is empty. No front element.")
            return None

        return self.items[0]


def main() -> None:
    queue = Queue()

    print(f"Is queue empty? {queue.is_empty()}")

    queue.enqueue(10)
    queue.enqueue(20)

    print(f"Front element: {queue.peek()}")

    queue.dequeue()
    queue.dequeue()

    # Underflow cases
    queue.dequeue()
    queue.peek()

    print(f"Is queue empty? {queue.is_empty()}")


if __name__ == "__main__":
    main()