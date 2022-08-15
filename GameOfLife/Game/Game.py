import numpy as np


class GameOfLife:
    """
    Simulate game of life given rules:
        1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
        2. Any live cell with two or three live neighbours lives on to the next generation.
        3. Any live cell with more than three live neighbours dies, as if by overpopulation.
        4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    """

    def __init__(self, initial_state):
        self.state = initial_state
        self.initial_state = initial_state

    def step(self):
        new_state = np.array([np.array([self.get_state(i, j) for j in range(len(self.state[0]))]) for i in range(len(self.state))])
        self.state = new_state
        return new_state

    def get_state(self, x, y):
        live_neighbours = 0
        for i in range(-1, 1):
            for j in range(-1, 1):
                if j != 0 or i != 0 or x + i >= 0 or x + i < len(self.state) or y + j >= 0 or y + j < len(self.state[0]):
                    if self.state[x+i][y+j] == 1:
                        live_neighbours += 1
        if (self.state[x][y] == 1 and 1 < live_neighbours < 4) or (self.state[x][y] == 0 and live_neighbours == 3):
            return 1
        return 0
