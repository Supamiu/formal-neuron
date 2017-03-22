import getopt
import pickle
from random import uniform

import sys

from neuron import Neuron


# On va commencer par une fonction 5x+2
def main():
    print('Hello carbon based life form !')
    result = []
    # On fait une phase d'apprentissage de 10000 éléments aléatoires, qu'on génère dans un tableau.
    for i in range(10000):
        x = uniform(0, 100)
        y = 5 * x + 2
        paths = [x, y]
        result.append(paths)

    # On parse nos arguments pour savoir si on charge ou si on créé un nouveau neurone.
    optlist, args = getopt.getopt(sys.argv, 'r', ['reload'])
    if '--reload' in args:
        with open("neuron.dump", "rb") as f:
            neuron = pickle.load(f)
    else:
        neuron = Neuron()
    # On lance la phase d'apprentissage, qui print automatiquement son état courant.
    for row in result:
        neuron.use(row[0], row[1])
    print('\n')


if __name__ == '__main__':
    main()
