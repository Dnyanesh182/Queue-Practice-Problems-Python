# UC2 – Implement peek (front) operation to view the first element of the queue.

class Queue:
    """
    Queue implementation using Python list.

    Supports enqueue, dequeue, and peek operations.
    """

    def __init__(self) -> None:
        self.items = []

    def enqueue(self, item) -> None:
        self.items.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        if not self.items:
            print("Queue Underflow. Cannot dequeue from empty queue.")
            return None

        removed = self.items.pop(0)
        print(f"Dequeued: {removed}")
        return removed

    def peek(self):
        """
        Return the front element without removing it.

        Time Complexity: O(1)
        """
        if not self.items:
            print("Queue is empty. No front element.")
            return None

        return self.items[0]


def main() -> None:
    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    print(f"Front element (peek): {queue.peek()}")  # 10

    queue.dequeue()
    print(f"Front after dequeue: {queue.peek()}")  # 20

    # Empty case
    queue.dequeue()
    queue.dequeue()
    print(f"Peek on empty queue: {queue.peek()}")


if __name__ == "__main__":
    main()