import random

class GraphNetwork:
    def __init__(self):
        self.__vertices = [
            f"X_SOURCE_x{i}" for i in range(1, 8)
        ]

        self.__edges = [
            (f"X_SOURCE_x{i}", f"X_x{i}_x{j}") for i in range(1, 8) for j in range(1, 8) if i != j
        ]

        self.__edges += [
            (f"X_x{i}_DISTANT", f"X_x{i}_x{j}") for i in range(1, 8) for j in range(1, 8) if i != j
        ]

        self.__constraints = {
            f"X_x{i}_x{j}": random.randint(1, 10) for i in range(1, 8) for j in range(1, 8) if i != j
        }

        print(self.__vertices)

    def saveLPFile(self, name_file):
        with open(name_file, "w") as lp_file:
            lp_file.write(f"max: {' + '.join(self.__vertices)};\n\n")
            
            for source, dest in self.__edges:
                lp_file.write(f"{source} = {dest};\n")
                
            for constraint, value in self.__constraints.items():
                lp_file.write(f"{constraint} <= {value};\n")


