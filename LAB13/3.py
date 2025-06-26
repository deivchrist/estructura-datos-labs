class MinHeap:
    def __init__(self):
        self.heap = []

    def delete_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        min_elem = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return min_elem

    def _heapify_down(self, index):
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break


def test_min_heap_delete_min():
    h = MinHeap()
    print("🧹 Test 1:", h.delete_min() is None)
    h.heap = [1]; print("🧹 Test 2:", h.delete_min() == 1 and h.heap == [])
    h.heap = [1, 3, 2]; print("🧹 Test 3:", h.delete_min() == 1 and h.heap == [2, 3])
    h.heap = [1, 3, 4, 5]; print("🧹 Test 4:", h.delete_min() == 1 and h.heap == [3, 5, 4])
    h.heap = [1, 2, 3, 4, 5]; print("🧹 Test 5:", h.delete_min() == 1)

test_min_heap_delete_min()

def extra_tests():
    h = MinHeap()
    h.heap = [2, 4, 3, 8, 5]; print("🧪 Extra Test 1:", h.delete_min() == 2 and h.heap == [3, 4, 5, 8])

    h = MinHeap()
    h.heap = [10, 15, 20, 17, 25]; print("🧪 Extra Test 2:", h.delete_min() == 10 and h.heap == [15, 17, 20, 25])

    h = MinHeap()
    h.heap = [5, 6, 7, 8, 9, 10]; print("🧪 Extra Test 3:", h.delete_min() == 5 and h.heap == [6, 8, 7, 10, 9])

extra_tests()


