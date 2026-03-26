# UC1 – Create a Queue class using list to perform basic enqueue and dequeue operations.

class Queue:
    """
    Queue implementation using Python list.

    Follows FIFO (First In First Out) principle.
    """

    def __init__(self) -> None:
        # Internal container for queue elements
        self.items = []

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

        Time Complexity: O(n)
        """
        if not self.items:
            print("Queue Underflow. Cannot dequeue from empty queue.")
            return None

        removed = self.items.pop(0)
        print(f"Dequeued: {removed}")
        return removed


def main() -> None:
    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    queue.dequeue()
    queue.dequeue()
    queue.dequeue()

    # Underflow case
    queue.dequeue()


if __name__ == "__main__":
    main()