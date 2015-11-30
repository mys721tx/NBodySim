"""
NBodySim.py: a simple n-body simulator
"""

import numpy
import scipy.constants
import itertools
import matplotlib.pyplot

def gravity(m1, m2, r):
    return scipy.constants.G * m1 * m2 / (r ** 2)

positions = numpy.array([[-50, -50], [-50, 50], [50, 50], [50, -50]], dtype = numpy.float64)

velocities = numpy.array([[0, 5], [5, 0], [0, -5], [-5, 0]], dtype = numpy.float64)

#accelerations = numpy.array([[0, 0], [0, 0], [0, 0], [0, 0]], dtype = numpy.float64)

masses = numpy.array([100000000000, 100000000000, 100000000000, 100000000000], dtype = numpy.float64)

d_t = 1

fig, ax = matplotlib.pyplot.subplots()
ax.set_xlim(-1000, 1000)
ax.set_ylim(-1000, 1000)

points, = ax.plot(positions[:, 0], positions[:, 1], marker='o', linestyle='None')

for i in range(500):
    
    accelerations = numpy.array([[0, 0], [0, 0], [0, 0], [0, 0]], dtype = numpy.float64)

    for pair in itertools.combinations(range(len(masses)), 2):
        particle_a, particle_b = pair
        d = positions[particle_b] - positions[particle_a]

        r = numpy.linalg.norm(d)
    
        f = gravity(masses[particle_a], masses[particle_b], r)

        accelerations[particle_a] += f / masses[particle_a] * d
        accelerations[particle_b] -= f / masses[particle_b] * d

    velocities += accelerations * d_t

    positions += 0.5 * accelerations * d_t ** 2 + velocities * d_t

    points.set_data(positions[:, 0], positions[:, 1])
    
    matplotlib.pyplot.savefig("%03d.png" % i)
