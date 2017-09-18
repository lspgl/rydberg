import math
import random as rand


class Rydberg:

    def __init__(self, pos, moment, idx):
        # ID of the Dipole
        self.idx = idx

        # Position
        self.pos = pos

        # Dipole Moment Vector
        self.moment = moment

        # Set Dipole with initial params
        # self.setDipole(pos=self.pos, moment=self.moment)

    def setDipole(self, pos=None, moment=None):
        # Change moment only if specified
        if moment is not None:
            self.moment = moment

        # Change pos only if specified
        if pos is not None:
            self.pos = pos

    def __repr__(self):
        retstr = ('RY @ X:' + str(round(self.pos[0], 1)) +
                  ' Y:' + str(round(self.pos[1], 1)) +
                  ' Z:' + str(round(self.pos[2], 1)))
        return retstr
