# UC8 – Implement circular queue with fixed size.

class CircularQueue:
    """
    Circular Queue implementation using fixed-size array.
    """

    def __init__(self, size: int) -> None:
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def is_empty(self) -> bool:
        return self.front == -1

    def is_full(self) -> bool:
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, item) -> None:
        if self.is_full():
            print("Queue Overflow. Cannot enqueue.")
            return

        if self.is_empty():
            self.front = 0

        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = item
        print(f"Enqueued: {item}")

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow. Cannot dequeue.")
            return None

        item = self.queue[self.front]

        if self.front == self.rear:
            # Queue becomes empty
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        print(f"Dequeued: {item}")
        return item

    def display(self) -> None:
        if self.is_empty():
            print("Queue is empty.")
            return

        i = self.front
        elements = []

        while True:
            elements.append(self.queue[i])
            if i == self.rear:
                break
            i = (i + 1) % self.size

        print(elements)


def main() -> None:
    cq = CircularQueue(5)

    cq.enqueue(10)
    cq.enqueue(20)
    cq.enqueue(30)
    cq.enqueue(40)
    cq.enqueue(50)  # Full

    cq.display()

    cq.dequeue()
    cq.dequeue()

    cq.enqueue(60)
    cq.enqueue(70)

    cq.display()


if __name__ == "__main__":
    main()