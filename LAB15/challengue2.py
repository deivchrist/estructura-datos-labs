test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def get_vertices(self):
        return list(self.adjacency_list.keys())

    def get_vertex_count(self):
        return len(self.adjacency_list)

    def has_vertex(self, vertex):
        return vertex in self.adjacency_list

def test_1_2():
    graph = Graph()
    
    # 1.2.1 Single vertex addition
    graph.add_vertex("Lima")
    record_test("1.2.1 Single vertex addition", graph.has_vertex("Lima"))
    
    # 1.2.2 Multiple vertex addition
    graph.add_vertex("Cusco")
    graph.add_vertex("Arequipa")
    record_test("1.2.2 Multiple vertex addition", graph.get_vertex_count() == 3)
    
    # 1.2.3 Duplicate prevention
    initial_count = graph.get_vertex_count()
    graph.add_vertex("Lima")  # Adding duplicate
    record_test("1.2.3 Duplicate prevention", graph.get_vertex_count() == initial_count)
    
    # 1.2.4 Vertex isolation
    lima_neighbors = graph.adjacency_list.get("Lima", [])
    record_test("1.2.4 Vertex isolation", len(lima_neighbors) == 0)
    
    # 1.2.5 Graph size tracking
    graph.add_vertex("Trujillo")
    record_test("1.2.5 Graph size tracking", "Trujillo" in graph.get_vertices())

# 🚀 Run tests
test_1_2()

# 📋 Summary
for r in test_results:
    print(r)
