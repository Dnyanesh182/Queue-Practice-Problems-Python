# UC4 – Implement size method to return the number of elements in the queue.

class Queue:
    """
    Queue implementation using Python list.

    Supports enqueue, dequeue, peek, is_empty, and size operations.
    """

    def __init__(self) -> None:
        self.items = []

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def size(self) -> int:
        """
        Return number of elements in queue.

        Time Complexity: O(1)
        """
        return len(self.items)

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

    print(f"Initial size: {queue.size()}")

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    print(f"Size after enqueue: {queue.size()}")

    queue.dequeue()
    print(f"Size after one dequeue: {queue.size()}")

    queue.dequeue()
    queue.dequeue()

    print(f"Final size: {queue.size()}")


if __name__ == "__main__":
    main()