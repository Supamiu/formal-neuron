from neuron import Neuron
from random import randrange


# On va commencer par une fonction 5x+2
def main():
    print('hello carbon based life form !')
    result = []
    for i in range(1000):
        x = randrange(0, 1000)
        y = 5 * x + 2
        paths = [x, y]
        result.append(paths)

    neuron = Neuron()
    for row in result:
        neuron.use(row[0], row[1])


if __name__ == '__main__':
    main()
