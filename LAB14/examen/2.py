test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedQueue:
    def __init__(self):
        self._front = None # _ lo usan los seniors para indicar que es no deberia salir de la clase
        self._rear  = None
        self._count = 0

    def is_empty(self):
        """Return True if queue is empty."""
        # Your solution here 🛠️
        return self._count == 0 

    def enqueue(self, item):
        """Add item to rear."""
        # Si yo tengo una cola debo tener personas en la fila
        new_node = Node(item)
        if self._rear is None:
            # Si la cola esta vacia, el nuevo nodo es el frente y el final
            self._front = new_node
            self._rear = new_node
        else:
            # Si la cola no esta vacia, agrego el nuevo nodo al final
            self._rear.next = new_node
            self._rear = new_node
        self._count += 1

    def dequeue(self):
        """Remove and return front item or None."""
        # Your solution here 🛠️
        if self.front is None:
            return None
        removed_item = self._front.data
        self._front = self._front.next
        self._count -= 1
        if self._front is None:
            self._rear = None
        return removed_item
    
        # Si la cola esta vacia, no hay nada que sacar
        pass

    def size(self):
        """Return number of elements."""
        # Your solution here 🛠️
        return self._count 
        pass

def test_o5_2():
    queue_linked = LinkedQueue()
    record_test("o5.2.1 empty",
        queue_linked.is_empty() is True and queue_linked.size() == 0)

    queue_linked.enqueue("a")
    queue_linked.enqueue("b")
    record_test("o5.2.2 enqueue/dequeue",
        queue_linked.is_empty() is False and
        queue_linked.size() == 2 and
        queue_linked.dequeue() == "a")

    queue_linked.dequeue()
    record_test("o5.2.3 drained",
        queue_linked.is_empty() is True and queue_linked.size() == 0)

    previous_size = queue_linked.size()
    record_test("o5.2.4 invalid dequeue",
        queue_linked.dequeue() is None and queue_linked.size() == previous_size)

    record_test("o5.2.5 return types",
        isinstance(queue_linked.is_empty(), bool) and
        isinstance(queue_linked.size(), int) and
        isinstance(queue_linked.dequeue(), (int, str, type(None))))

# 🚀 Run tests
test_o5_2()

# 📋 Summary
for result in test_results:
    print(result)