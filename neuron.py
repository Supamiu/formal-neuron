import pickle
from random import randrange


class Neuron:
    def __init__(self):

        self.weight = randrange(-1, 1)
        self.bias = randrange(-1, 1)
        self.r = 0.05

    def __del__(self):
        with open("neuron.dump", "wb") as f:
            pick = pickle.Pickler(f)
            pick.dump(self)

    def save(self):
        with open("neuron.dump", "wb") as f:
            pick = pickle.Pickler(f)
            pick.dump(self)

    def use(self, x, result):

        value = x * self.weight

        if value == result:
            print('I found it ! gimme a harder one !')
        else:
            #On compare le résultat de base avec le résultat attendu pour gérer le biais
            if value > result:
                self.weight -= self.r
            else:
                self.weight += self.r

            if self.bias + value > result:
                self.bias -= self.r
            else:
                self.bias += self.r

        print('current weight : ' + str(self.weight))
        print('current bias : ' + str(self.bias))
        return value + self.bias
