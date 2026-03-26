# UC10 – Implement queue using two stacks (advanced problem).

class QueueUsingStacks:
    """
    Queue implementation using two stacks.

    Maintains FIFO behavior using LIFO stacks.
    """

    def __init__(self) -> None:
        self.stack_in = []
        self.stack_out = []

    def is_empty(self) -> bool:
        return not self.stack_in and not self.stack_out

    def enqueue(self, item) -> None:
        """
        Add element to queue.

        Time Complexity: O(1)
        """
        self.stack_in.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        """
        Remove element from queue.

        Amortized Time Complexity: O(1)
        """
        if self.is_empty():
            print("Queue Underflow. Cannot dequeue.")
            return None

        # Transfer elements if needed
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

        removed = self.stack_out.pop()
        print(f"Dequeued: {removed}")
        return removed

    def peek(self):
        """
        Get front element without removing.

        Amortized Time Complexity: O(1)
        """
        if self.is_empty():
            return None

        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

        return self.stack_out[-1]


def main() -> None:
    queue = QueueUsingStacks()

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    print(f"Front element: {queue.peek()}")

    queue.dequeue()
    queue.dequeue()

    print(f"Front after dequeue: {queue.peek()}")

    queue.dequeue()

    # Underflow case
    queue.dequeue()


if __name__ == "__main__":
    main()