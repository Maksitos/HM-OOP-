from abc import abstractmethod, ABCMeta


class Material:
    __metaclass__ =ABCMeta

    @abstractmethod
    def agg_state(self):
        pass


class Element(Material):

    def __init__(self, melting_temp, boiling_temp):

        self.melting_temp = melting_temp
        self.boiling_temp = boiling_temp

    def agg_state(self, t, scale):
        if scale == 'K':
            self.melting_temp = self.melting_temp + 273.15
            self.boiling_temp = self.boiling_temp + 273.15
        elif scale == 'F':
            self.melting_temp = self.melting_temp + 32
            self.boiling_temp = self.boiling_temp + 32
        else:
            pass

        if t <= self.melting_temp:
            return 'solid'
        elif self.melting_temp <= t < self.boiling_temp:
            return 'liquid'
        elif t >= self.boiling_temp:
            return 'gas'


Oxygen = Element(-218.35, -182.96)

print(Oxygen.agg_state(-150, 'C'))
