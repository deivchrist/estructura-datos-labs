test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class MaxHeap:
    def __init__(self):
        # "We create an empty list to represent the heap"
        self.heap = []
    
    def insert(self, value):
        # "We add the new value to the end of the heap"
        self.heap.append(value)
        # "We apply heapify up from that index"
        self._heapify_up(len(self.heap) - 1)
    
    def delete_max(self):
        #  "If the heap is empty, there is nothing to delete"
        if not self.heap:
            return None
        # "If there is only one element, we remove it and return it"
        if len(self.heap) == 1:
            return self.heap.pop()
        max_val = self.heap[0]
        #the root with the last value
        self.heap[0] = self.heap.pop()
        # "We restore the max-heap property by heapifying down from the root"
        self._heapify_down(0)
        return max_val
    
    def build_heap(self, array):
        # Reemplazamos el contenido del heap por el nuevo arreglo
        self.heap = array[:]
        # Comenzamos desde el último nodo con hijos hacia la raíz
        for i in reversed(range(len(self.heap)//2)):
            self._heapify_down(i)
    
    def _heapify_up(self, index):
        # We move the node up as long as it is greater than its parent
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2
    
    def _heapify_down(self, index):
        # We maintain ownership of the MaxHeap by bringing down the node if necessary 

        while 2 * index + 1 < len(self.heap):
            largest = index
            left = 2 * index + 1
            right = 2 * index + 2
            if left < len(self.heap) and self.heap[left] > self.heap[largest]:
                largest = left
            if right < len(self.heap) and self.heap[right] > self.heap[largest]:
                largest = right
            if largest == index:
                break
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            index = largest

def test_1_5():
    heap = MaxHeap()
    
    # 1.5.1 MaxHeap insertion: raíz debe ser el mayor valor insertado
    heap.insert(3)
    heap.insert(1)
    heap.insert(5)
    record_test("1.5.1 MaxHeap insertion", heap.heap[0] == 5)
    
    # 1.5.2 MaxHeap deletion: debe devolver el valor máximo
    max_val = heap.delete_max()
    record_test("1.5.2 MaxHeap deletion", max_val == 5)
    
    # 1.5.3 Build heap from array: convierte arreglo desordenado en MaxHeap
    heap.build_heap([3, 1, 4, 1, 5, 9, 2])
    record_test("1.5.3 Build heap from array", heap.heap[0] == max(heap.heap))
    
    # 1.5.4 Heap property verification: padre ≥ hijos en todos los nodos
    valid_max_heap = all(
        heap.heap[i] >= heap.heap[2*i+1] if 2*i+1 < len(heap.heap) else True
        for i in range(len(heap.heap)//2)
    )
    record_test("1.5.4 Heap property verification", valid_max_heap)
    
    # 1.5.5 Empty array handling: build_heap([]) debe funcionar y dejar el heap vacío
    heap.build_heap([])
    record_test("1.5.5 Empty array handling", len(heap.heap) == 0)


test_1_5()
for r in test_results:
    print(r)
