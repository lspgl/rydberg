import core.configuration as config
import core.optimizer as opt
import sys
from os import listdir
from os.path import isfile, join


def automated_routine(fn):
    print('Optimizing', fn)
    fn_stripped = fn.split('.')[0]
    init_name = fn_stripped + '_init'
    opt_name = fn_stripped + '_opt'
    cell = config.Configuration()
    cell.read(fn=fn)
    cell.plotdipoles(fn=init_name)
    optimizer = opt.Optimizer(maxit=1000)
    optcell = optimizer.optimize(cell)
    optcell.plotdipoles(fn=opt_name)
    optcell.write(fn=opt_name + '.csv')


if __name__ == '__main__':
    path = 'csv/'
    files = [f for f in listdir(path) if isfile(join(path, f))]
    files_csv = [f for f in files if f.split('.')[1] == 'csv']

    for fn in files_csv:
        automated_routine(fn)
