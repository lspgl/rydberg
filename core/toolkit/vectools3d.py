# Vector calculation tools

import math


def normvector(v):
    x, y, z = v
    n = math.sqrt(x**2 + y**2 + z**2)
    if n == 0:
        print 'WARNING: Zero norm'
        return (0, 0, 0)
    xn = x / n
    yn = y / n
    zn = z / n

    return (xn, yn, zn)


def connvector(p1, p2, norm=True):
    # Vector from p1 to p2

    vx = p2[0] - p1[0]
    vy = p2[1] - p1[1]
    vz = p2[2] - p1[2]

    if norm:
        n = math.sqrt(vx**2 + vy**2 + vz**2)
        if n == 0:
            return (0, 0, 0)
        vx = vx / n
        vy = vy / n
        vz = vz / n

    vector = (vx, vy, vz)
    return vector


def pointdist(p1, p2):
    # Magnitude of distance between p1 and p2

    dist = math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)
    return dist


def vectormags(v_arr):
    # Magnitudes of vectors in an array

    mags = []
    for vect in v_arr:
        mag_i = pointdist((0, 0, 0), vect)
        mags.append(mag_i)
    return mags


def scalarproduct(v1, v2):
    # Dot product v1.v2
    v1x, v1y, v1z = v1
    v2x, v2y, v2z = v2
    scalar = (v1x * v2x) + (v1y * v2y) + (v1z * v2z)

    return scalar


if __name__ == '__main__':
    print 'TESTING VECTOR TOOLS'

    testvect_a = (1, 1, 1)
    testvect_b = (0, 0, 0)

    comparator = [math.sqrt(3), 0.0]

    vectarr = [testvect_a, testvect_b]

    mags = vectormags(vectarr)
    assert mags == comparator
    print 'vectormags OK'

    dist = pointdist(testvect_a, testvect_b)
    assert dist == math.sqrt(3)
    print 'pointdist OK'

    conn = connvector(testvect_a, testvect_b, norm=False)
    assert conn == (-1, -1, -1)
    print 'connvector OK'

    s1 = scalarproduct(testvect_a, testvect_b)
    s2 = scalarproduct(testvect_b, testvect_a)
    assert s1 == s2
    assert s1 == 0
    print 'scalarproduct OK'

    print 'VECTOR TOOLS OK'
