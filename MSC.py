import random
import networkx as nx

# Создание графа
graph = nx.Graph()

# Добавление вершин
graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_node("D")
graph.add_node("E")

# Добавление рёбер с весами
for source in graph.nodes():
    for target in graph.nodes():
        if source != target:
            graph.add_edge(source, target, weight=random.randint(1, 10))


# Создание LP-файла
with open("graph.lp", "w") as writer:
    writer.write("min: ")
    first_in_line = True
    for source in graph.nodes():
        for target in graph.nodes():
            if source != target:
                if not first_in_line:
                    writer.write(" + ")
                weight = graph[source][target]["weight"]
                writer.write(f"{weight} x_{source}{target}")
                first_in_line = False
    
    writer.write(";\n")
    
    # ограничения
    for source in graph.nodes():
        writer.write(f"c_{source}: ")
        first_in_line = True
        for target in graph.nodes():
            if source != target:
                if not first_in_line:
                    writer.write(" + ")
                writer.write(f"x_{source}{target}")
                first_in_line = False
        writer.write(" >= 1;\n")
    
    writer.write("bin ")
    first_in_line = True
    for source in graph.nodes():
        for target in graph.nodes():
            if source != target:
                if not first_in_line:
                    writer.write(" ")
                writer.write(f"x_{source}{target}")
                first_in_line = False
    writer.write(";\n")


