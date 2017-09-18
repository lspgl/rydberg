import numpy as np
import math
import sys
from toolkit.aux import colors
from toolkit import electronics, vectools3d
from functools import partial
import multiprocessing as mp
import random as rand
import copy


class Optimizer:

    def __init__(self, criterion=1, maxit=100):
        self.criterion = criterion
        self.maxit = maxit

        self.mismatchTracker = []

        self.ncpu = mp.cpu_count()
        self.pool = mp.Pool(self.ncpu)
        self.conv_counter = 0

    def optimize(self, system):
        self.system = system
        self.population = self.system.population
        self.subsetRoutine()
        self.system.population = self.population
        self.plotConvergence()
        return self.system

    def subsetRoutine(self, fraction=.5, seed=None):
        # Prepare randomness
        rand.seed(seed)

        # Compute initial gradient
        self.envGradient()

        # number of reoriented dipoles
        npartial = int(len(self.population) * fraction)

        converged = False

        while True:
            # Whilst convergence criterion is not fulfilled calculate gradient
            # and reorient dipoles along vector

            # Generate subset indices
            subset = []
            idx = -1
            for _ in range(npartial):
                while True:
                    idx = rand.randint(0, len(self.population) - 1)
                    if idx not in subset:
                        subset.append(copy.copy(idx))
                        break
            # Calculate gradient
            self.envGradient()

            # Check for convergence
            if self.maxMismatch < self.criterion:
                converged = True
                break
            elif self.conv_counter > self.maxit:
                break

            for i, particle in enumerate(self.population):
                if i in subset:
                    newmom = vectools3d.normvector(self.gradvect[i])
                    particle.setDipole(moment=newmom)
            self.conv_counter += 1
            sys.stdout.write("Step %d   \r" % (self.conv_counter))
            sys.stdout.flush()

            # if self.maxMismatch < criterion:
            #    break
        if converged:
            print colors.YEL + 'Convergence after ' + str(self.conv_counter) + ' Steps.' + colors.ENDC
        else:
            print colors.WARNING + 'No convergence after ' + str(self.conv_counter) + ' Steps.' + colors.ENDC
            print 'Using current state as best guess...'
        self.conv_counter = 0

    def mismatchAngle(self):
        self.angularMismatch = list(np.zeros(len(self.population)))

        for i, particle in enumerate(self.population):
            mn = vectools3d.normvector(particle.moment)
            gn = vectools3d.normvector(self.gradvect[i])
            # print 'scalar:', vectools3d.scalarproduct(mn, gn)

            equality = [False] * 3
            rel_tol = 0.001
            for j, m in enumerate(mn):
                if abs(m - gn[j]) <= rel_tol * max(abs(m), abs(gn[j])):
                    equality[j] = True

            if equality == [True] * 3:
                mm_tmp = 0.0
            else:
                mm_tmp = math.degrees(math.acos(vectools3d.scalarproduct(mn, gn)))
            if mm_tmp > 180:
                mm_tmp = abs(mm_tmp - 360)
            self.angularMismatch[i] = mm_tmp
        self.mismatchTracker.append(self.angularMismatch[:])
        self.maxMismatch = max(self.angularMismatch)

    def envGradient(self):
        # Calculate gradient

        # Prepare partial function for MP
        partial_envGradientSubroutine = partial(electronics.envGradientSubroutine, population=self.population)

        # Map MP
        self.gradvect = self.pool.map(partial_envGradientSubroutine, self.population)

        # Calculate angular mismatch
        self.mismatchAngle()

    def plotConvergence(self):
        print colors.RED + 'Plotting Convergence' + colors.ENDC
        import matplotlib.pyplot as plt
        fig = plt.figure(figsize=(12, 8))
        ax = fig.add_subplot(111)
        ax.set_title('Convergence Plot')
        ax.set_xlabel('Iteration')
        ax.set_ylabel('Mismatch Angle')

        ax.plot(self.mismatchTracker[1:],
                color='#d03600',
                lw=0.15)

        fig.savefig('img/convergence.png', dpi=300)
