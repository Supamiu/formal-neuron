import pickle
from random import uniform


# Classe qui gère un neurone et porte toute sa logique.
class Neuron:
    # Lors de note init on random les valeurs de base.
    def __init__(self):
        self.weight = uniform(-1, 1)
        self.bias = uniform(-1, 1)
        self.r = 0.01

    # En destructeur on register le neurone dans son état actuel.
    def __del__(self):
        with open("neuron.dump", "wb") as f:
            pickle.dump(self, f, protocol=2)
            print("Saved myself in neuron.dump")

    # On charge le neurone sauvegardé.
    def load(self):
        with open("neuron.dump", "wb") as f:
            pickle.dump(self, f, protocol=2)

    # Permet de faire une étape de training
    def use(self, x, result):

        value = x * self.weight + self.bias

        if value == result:
            print('I found it ! Gimme a harder one !')
        else:
            self.weight += (result - value) * self.r * 0.01 * x
            self.bias += (result - value) * self.r * 0.05

        print('\rweight : ' + str(self.weight) + ' | bias : ' + str(self.bias), end='')
        return value + self.bias
