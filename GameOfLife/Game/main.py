import random
from Game import GameOfLife
import matplotlib.pyplot as plt
import matplotlib.animation as animation

if __name__ == "__main__":
    initial_state = [[random.randint(0, 1) for j in range(9)] for i in range(9)]
    game = GameOfLife(initial_state)
    figure = plt.figure()

    im = plt.imshow(initial_state, animated=True)

    def step(i):
        state = game.step()
        im.set_array(state)
        return im,
    ani = animation.FuncAnimation(figure, step, interval=100, blit=True)
    plt.show()