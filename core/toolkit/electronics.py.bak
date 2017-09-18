import math
import vectools3d


def envGradientSubroutine(dp, population, grad=True):
    # Compute dipole population induced gradient at position of dp
    current = dp.idx
    gradvect = (0, 0, 0)
    for dpi in population:
        if dpi.idx == current:
            # Exclude field created by dipole in question
            pass
        else:
            # Dielectric constant
            epsilon = 1.0
            # Moment of iterated dipole
            p = dpi.moment
            # Unit vector from iterated dipole to dp
            r = vectools3d.connvector(dpi.pos, dp.pos)
            # Absolute distance
            dist = vectools3d.pointdist(dpi.pos, dp.pos)
            # Scalar product
            scalar = vectools3d.scalarproduct(p, r)

            # Distance scaling
            prefac = 1.0 / (4.0 * math.pi * epsilon * dist**3)

            # Claculate field
            ex = prefac * (3 * scalar * r[0] - p[0])
            ey = prefac * (3 * scalar * r[1] - p[1])
            ez = prefac * (3 * scalar * r[2] - p[2])

            # Append field (Could be written more nicely but was too lazy, although
            # writing this comment probably took longer than actually rewriting it...)
            gradvect = (gradvect[0] + ex, gradvect[1] + ey, gradvect[2] + ez)

    return gradvect
