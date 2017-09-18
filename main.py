import core.configuration as config
import core.optimizer
import sys

if __name__ == '__main__':
    # Initialize Cell
    cell = config.Configuration()

    # Parameters
    # nparticles = 100
    # cellsize = 100
    # moment = (1, 0, 0)

    # Initialize randomly:
    # cell.makeRandom(nparticles, cellsize)

    # Initialize aligned:
    # cell.makeAligned(nparticles, cellsize, moment)

    # Initialize from TXT positions
    #cell.readpos('configurations/Ba_LJ.txt', m=None)

    cell.read(fn='configuration_random_LJ.csv')
    # Plot dipoles & Write CSV
    cell.plotdipoles(fn='random_LJ')
    # cell.write(fn='configuration_random_LJ.csv')

    cell.read(fn='configuration_optimal_LJ.csv')
    cell.plotdipoles(fn='optimal_LJ')

    sys.exit()

    # Initialize Optimizer
    optimizer = core.optimizer.Optimizer(maxit=1000)

    # Optimize Cell
    optcell = optimizer.optimize(cell)
    # Plot dipoles & write CSV
    optcell.plotdipoles(fn='optimal_LJ')
    optcell.write(fn='configuration_optimal_LJ.csv')
