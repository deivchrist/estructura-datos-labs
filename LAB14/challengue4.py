test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class MinHeap:
    def __init__(self):
        self.heap = []
    
    def delete_min(self):
        # "If the heap is empty, there is nothing to delete"
        if not self.heap:
            return None
        
        # "If there is only one element, we remove it and return it"
        if len(self.heap) == 1:
            return self.heap.pop()
        
        # "We store the minimum (the root)"
        min_val = self.heap[0]
    
        # "We replace the root with the last element in the heap"
        self.heap[0] = self.heap.pop()
        
        # "We restore the min-heap property by heapifying down from the root"
        self._heapify_down(0)
        return min_val
    
    def _heapify_down(self, index):
        #  "We continue while the node has at least a left child"
    
        while self._has_left_child(index):
            # "Assume the left child is the smallest by default"
            smaller_child_index = self._left_child_index(index)
            
            # If there is also a right child and it is younger than the left one, we choose it
            if self._has_right_child(index) and self.heap[self._right_child_index(index)] < self.heap[smaller_child_index]:
                smaller_child_index = self._right_child_index(index)
            
            # If the current node is already less than or equal to the smallest of its children, stop
            if self.heap[index] <= self.heap[smaller_child_index]:
                break
            
            # We exchange with the youngest son
            self.heap[index], self.heap[smaller_child_index] = self.heap[smaller_child_index], self.heap[index]
            
            # We update the index to continue going down
            index = smaller_child_index

    def _left_child_index(self, index):
        return 2 * index + 1
    
    def _right_child_index(self, index):
        return 2 * index + 2
    
    def _has_left_child(self, index):
        return self._left_child_index(index) < len(self.heap)
    
    def _has_right_child(self, index):
        return self._right_child_index(index) < len(self.heap)
    
    def size(self):
        return len(self.heap)

def test_1_4():
    heap = MinHeap()
    
    # 1.4.1 Empty heap deletion – remove from empty heap should return None
    result = heap.delete_min()
    record_test("1.4.1 Empty heap deletion", result is None)
    
    # 1.4.2 Single element deletion – removes a single element and the heap becomes empty
    heap.heap = [5]
    result = heap.delete_min()
    record_test("1.4.2 Single element deletion", result == 5 and heap.size() == 0)
    
    # 1.4.3 Multiple deletions – eliminate two minima in ascending order
    heap.heap = [1, 3, 2, 7, 4]
    first = heap.delete_min()
    second = heap.delete_min()
    record_test("1.4.3 Multiple deletions", first == 1 and second == 2)
    
    # 1.4.4 Heap property maintenance – after delete, heap validate
    heap.heap = [1, 3, 2, 7, 4, 5]
    heap.delete_min()
    valid_heap = all(
        heap.heap[i] <= heap.heap[2*i+1] if 2*i+1 < len(heap.heap) else True
        for i in range(len(heap.heap)//2)
    )
    record_test("1.4.4 Heap property maintenance", valid_heap)
    
    # 1.4.5 Size tracking – heap size decreases correctly
    initial_size = heap.size()
    heap.delete_min()
    record_test("1.4.5 Size tracking", heap.size() == initial_size - 1)

test_1_4()
for r in test_results:
    print(r)
