import tkinter as tk
from tkinter import messagebox
import heapq

class DijkstraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Algoritmo de Dijkstra")
        self.graph = {}
        
        # Crear widgets de la interfaz gráfica
        self.label_title = tk.Label(root, text="Algoritmo de Dijkstra", font=("Arial", 16))
        self.label_title.pack(pady=10)
        
        self.label_instructions = tk.Label(root, text="Ingrese el grafo como nodos y distancias (ej: A B 7)")
        self.label_instructions.pack()

        self.entry_graph = tk.Entry(root, width=50)
        self.entry_graph.pack(pady=5)
        
        self.button_add_edge = tk.Button(root, text="Agregar Arista", command=self.add_edge)
        self.button_add_edge.pack(pady=5)

        self.label_start_node = tk.Label(root, text="Ingrese el nodo inicial:")
        self.label_start_node.pack(pady=5)
        
        self.entry_start_node = tk.Entry(root, width=10)
        self.entry_start_node.pack(pady=5)
        
        self.button_calculate = tk.Button(root, text="Calcular Dijkstra", command=self.calculate_dijkstra)
        self.button_calculate.pack(pady=10)
        
        self.text_result = tk.Text(root, height=10, width=50, state='disabled')
        self.text_result.pack(pady=5)
        
        self.graph_display = tk.Text(root, height=10, width=50, state='disabled')
        self.graph_display.pack(pady=5)
   
    def add_edge(self):
        edge_input = self.entry_graph.get()
        try:
            node1, node2, weight = edge_input.split()
            weight = int(weight)
            if node1 not in self.graph:
                self.graph[node1] = []
            if node2 not in self.graph:
                self.graph[node2] = []
            self.graph[node1].append((node2, weight))  # Solo agregamos la arista en una dirección
            
            self.update_graph_display()
            self.entry_graph.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Formato incorrecto. Debe ser: Nodo1 Nodo2 Peso")

    
    def update_graph_display(self):
        self.graph_display.config(state='normal')
        self.graph_display.delete(1.0, tk.END)
        self.graph_display.insert(tk.END, "Grafo actual:\n")
        for node, neighbors in self.graph.items():
            for neighbor, weight in neighbors:
                self.graph_display.insert(tk.END, f"{node} --({weight})--> {neighbor}\n")
        self.graph_display.config(state='disabled')
   
    def calculate_dijkstra(self):
        start_node = self.entry_start_node.get()
        if start_node not in self.graph:
            messagebox.showerror("Error", "El nodo inicial no existe en el grafo.")
            return
        
        distances = self.dijkstra(self.graph, start_node)
        
        self.text_result.config(state='normal')
        self.text_result.delete(1.0, tk.END)
        self.text_result.insert(tk.END, f"Distancias desde el nodo {start_node}:\n")
        for node, distance in distances.items():
            self.text_result.insert(tk.END, f"{node}: {distance}\n")
        self.text_result.config(state='disabled')
    
    def dijkstra(self, graph, start):
        queue = [(0, start)]
        distances = {node: float('infinity') for node in graph}
        distances[start] = 0
        visited = set()
        
        while queue:
            current_distance, current_node = heapq.heappop(queue)
            
            if current_node in visited:
                continue
            visited.add(current_node)
            
            for neighbor, weight in graph[current_node]:
                distance = current_distance + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor))
        
        return distances

# Crear la ventana de Tkinter
root = tk.Tk()
app = DijkstraApp(root)
root.mainloop()

