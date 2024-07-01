import sys
from PIL import Image, ImageDraw

class Node:
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

class StackFrontier:
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("Fronteira Vazia")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node

class QueueFrontier(StackFrontier):
    def remove(self):
        if self.empty():
            raise Exception("Fronteira Vazia")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node

class Maze:
    def __init__(self, filename):
        
        # Lê o arquivo e define a altura e largura do labirinto
        with open(filename) as f:
            contents = f.read()
        # Validação do inicio e objetivo
        if contents.count("A") != 1:
            raise Exception("Labirinto precisa ter um ponto exato de inicio")
        if contents.count("B") != 1:
            raise Exception("Labirinto precisa ter um objetivo exato")
        
        # Determinando altura de largura do labirinto
        contents = contents.splitlines()
        self.height = len(contents)
        self.width = max(len(line) for line in contents)
        
        # Localizando paredes (walls)
        self.walls = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    if contents[i][j] == "A":
                        self.start = (i, j)
                        row.append(False)
                    elif contents[i][j] == "B":
                        self.goal = (i, j)
                        row.append(False)
                    elif contents[i][j] == " ":
                        row.append(False)
                    else:
                        row.append(True)
                except IndexError:
                    row.append(False)
            self.walls.append(row)

        self.solution = None

    def print(self):
        solution = self.solution[1] if self.solution is not None else None
        print()
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    print("#", end="")
                elif (i, j) == self.start:
                    print("A", end="")
                elif (i, j) == self.goal:
                    print("B", end="")
                elif solution is not None and (i, j) in solution:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
        print()

    def neighbors(self, state):
        row, col = state
        # Todas as ações possíveis
        candidates = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1))
        ]

        # Validando se as ações são válidas
        result = []
        for action, (r, c) in candidates:
            if 0 <= r < self.height and 0 <= c < self.width and not self.walls[r][c]:
                result.append((action, (r, c)))
        return result

    def solve(self):
        """Ache uma solução para o labirinto, se existir uma"""

        # Verificando o número de estados já explorados
        self.num_explored = 0

        # Inicializa a fronteira para a posição inicial
        start = Node(state=self.start, parent=None, action=None)
        frontier = StackFrontier()
        frontier.add(start)
        
        # Inicializa de uma posição vazia não explorada
        self.explored = set()
        
        # Loop até a solução ser encontrada
        while True:
            
            # Se nada for encontrado na fronteira, então não existe caminho
            if frontier.empty():
                raise Exception("Sem solução")
            
            # Escolhe um node da fronteira
            node = frontier.remove()
            self.num_explored += 1
            
            # Se o nó for a solução, então temos uma solução
            if node.state == self.goal:
                actions = []
                cells = []
                
                # Verifica os nodes anteriores para encontrar uma solução
                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells)
                return
                
            # Marcar o node como explorado
            self.explored.add(node.state)

            # Adicionar "vizinhos" para a fronteira
            for action, state in self.neighbors(node.state):
                if not frontier.contains_state(state) and state not in self.explored:
                    child = Node(state=state, parent=node, action=action)
                    frontier.add(child)

    def output_image(self, filename, show_solution=True):
        cell_size = 50
        cell_border = 2
        img = Image.new(
            "RGBA",
            (self.width * cell_size, self.height * cell_size),
            "black"
        )
        draw = ImageDraw.Draw(img)
        solution = self.solution[1] if self.solution is not None else None
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    fill = (40, 40, 40)
                elif (i, j) == self.start:
                    fill = (250, 0, 0)
                elif (i, j) == self.goal:
                    fill = (0, 171, 28)
                elif solution is not None and show_solution and (i, j) in solution:
                    fill = (220, 235, 113)
                else:
                    fill = (237, 240, 252)

                draw.rectangle(
                    [
                        (j * cell_size + cell_border, i * cell_size + cell_border),
                        ((j + 1) * cell_size - cell_border, (i + 1) * cell_size - cell_border)
                    ],
                    fill=fill
                )

        img.save(filename)

if len(sys.argv) != 2:
    sys.exit("como iniciar: python maze.py labirinto.txt")

m = Maze(sys.argv[1])
print("Labirinto:")
m.print()
print("Resolvendo...")
m.solve()
print("States explorados:", m.num_explored)
print("Solucão:")
m.print()
m.output_image("labirinto.png", show_solution=True)
