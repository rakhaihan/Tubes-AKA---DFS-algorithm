import timeit
import tkinter as tk
from tkinter import simpledialog, messagebox
import networkx as nx
import matplotlib.pyplot as plt

def generate_tree(n):
    tree = {}
    nodes = [chr(i) for i in range(ord('A'), ord('A') + n)]
    for i in range(n):
        children = []
        if 2 * i + 1 < n:
            children.append(nodes[2 * i + 1])
        if 2 * i + 2 < n:
            children.append(nodes[2 * i + 2])
        tree[nodes[i]] = children
    return tree

# Recursive DFS
def dfs_recursive(G, v, marked):
    marked[ord(v) - ord('A')] = True
    for w in G[v]:
        if not marked[ord(w) - ord('A')]:
            dfs_recursive(G, w, marked)

def visualize_tree(tree):
    G = nx.DiGraph()
    for node, children in tree.items():
        for child in children:
            G.add_edge(node, child)
    
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=15, font_weight="bold", arrows=True)
    plt.show()

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    x = simpledialog.askinteger("Input", "Masukkan banyak node:", minvalue=1)

    results = []
    iterations = 100  # Number of iterations to average

    for n in range(1, x + 1):
        G = generate_tree(n)
        
        total_time_recursive = 0
        for _ in range(iterations):
            marked_recursive = [False] * len(G)
            total_time_recursive += timeit.timeit(lambda: dfs_recursive(G, 'A', marked_recursive), number=1)
        
        average_time_recursive = total_time_recursive / iterations
        results.append((n, average_time_recursive))

    # Display results in a message box
    result_text = "Nodes\tRecursive Time (seconds)\n"
    for n, recursive_time in results:
        result_text += f"{n}\t{recursive_time:.6f}\n"
    
    messagebox.showinfo("Running Times", result_text)

    # Visualize the final tree
    visualize_tree(generate_tree(x))

if __name__ == "__main__":
    main()
