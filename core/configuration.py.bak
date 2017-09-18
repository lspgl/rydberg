import random as rand
from rydberg import Rydberg
import copy
import csv
import math
from toolkit import vectools3d
from toolkit.aux import colors
from ast import literal_eval as make_tuple


class Configuration:

    def __init__(self):
        self.population = []
        print colors.RED + 'Empty cell initialized' + colors.ENDC

    def read(self, fn):
        print colors.YEL + 'Reading CSV: ' + colors.WARNING + fn + colors.ENDC
        self.population = []
        with open(fn, 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for i, row in enumerate(reader):
                position = make_tuple(row[0])
                moment = make_tuple(row[1])
                atom = Rydberg(position, moment, i)
                self.population.append(copy.copy(atom))

    def readpos(self, fn, m=None):
        print colors.YEL + 'Reading TXT: ' + colors.WARNING + fn + colors.ENDC
        with open(fn) as f:
            content = f.readlines()
        # you may also want to remove whitespace characters like `\n` at the end of each line
        content = [x.strip().split(' ') for x in content]
        for i, line in enumerate(content):
            position = tuple(float(cord) for cord in line)
            if m is None:
                moment = vectools3d.normvector((rand.uniform(-1.0, 1.0),
                                                rand.uniform(-1.0, 1.0),
                                                rand.uniform(-1.0, 1.0)))
            else:
                moment = vectools3d.normvector(m)
            atom = Rydberg(position, moment, i)
            self.population.append(copy.copy(atom))

    def write(self, fn):
        print colors.YEL + 'Writing CSV: ' + colors.WARNING + fn + colors.ENDC
        with open(fn, 'wb') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            for atom in self.population:
                payload = [atom.pos, atom.moment]
                writer.writerow(payload)

    def makeRandom(self, n, cellsize, seed=None):
        print colors.RED + 'Populating randomly with ' + str(n) + ' Atoms' + colors.ENDC
        rand.seed(seed)
        self.cellsize = cellsize
        for i in range(n):
            position = (rand.uniform(0, self.cellsize),
                        rand.uniform(0, self.cellsize),
                        rand.uniform(0, self.cellsize))

            moment = vectools3d.normvector((rand.uniform(-1.0, 1.0),
                                            rand.uniform(-1.0, 1.0),
                                            rand.uniform(-1.0, 1.0)))
            atom = Rydberg(position, moment, i)
            self.population.append(copy.copy(atom))

    def makeAligned(self, n, cellsize, moment, seed=None):
        print colors.RED + 'Populating Aligned with ' + str(n) + ' Atoms' + colors.ENDC
        rand.seed(seed)
        self.cellsize = cellsize
        for i in range(n):
            position = (rand.uniform(0, self.cellsize),
                        rand.uniform(0, self.cellsize),
                        rand.uniform(0, self.cellsize))

            normmoment = vectools3d.normvector(moment)

            atom = Rydberg(position, normmoment, i)
            self.population.append(copy.copy(atom))

    def plotdipoles(self, fn='dipoles'):
        print colors.RED + 'Plotting Dipoles' + colors.ENDC
        from mpl_toolkits.mplot3d import Axes3D
        import matplotlib.pyplot as plt
        fig = plt.figure(figsize=(12, 8))
        ax = fig.add_subplot(111, projection='3d')
        ax.set_aspect('equal')
        ax.set_title('Rydberg Dipole Alignment')
        ax.set_xlabel('X Position')
        ax.set_ylabel('Y Position')
        for atom in self.population:
            # ax.scatter(*zip(atom.pos), edgecolor='#d03600', facecolor='#d03600', zorder=1)
            origin = list(atom.pos)
            scale = 0.25
            # scale = 100.0
            endpoint = [x + scale * atom.moment[i] for i, x in enumerate(atom.pos)]
            tracepoint = origin[:2]
            tracepoint.append(0)
            momentLine = (origin, endpoint)
            traceLine = (origin, tracepoint)
            ax.plot(*zip(*momentLine), color='#d03600')
            ax.plot(*zip(*traceLine), marker='x', ms=1, color='black', alpha=0.2, lw=0.2)

        fig.savefig(('img/' + fn + '.png'), dpi=300)


if __name__ == '__main__':
    cfg = Configuration()
    cfg.readpos('configurations/fcc_lattice.txt')
