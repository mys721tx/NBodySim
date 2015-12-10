"""
NBodySim.py: a simple n-body simulator
"""

import itertools
import numpy
import scipy.constants
import matplotlib.pyplot

def gravity(mass_1, mass_2, radius):
    """
    calculate the gravtional attraction between m1 and m2.
    """

    return scipy.constants.G * mass_1 * mass_2 / (radius ** 2)

def particle_to_particle():
    """
    the particale to particle simulator
    """

    positions = numpy.array([
        [-50, -50],
        [-50, 50],
        [50, 50],
        [50, -50]], dtype=numpy.float64)

    velocities = numpy.array([
        [0, 5],
        [5, 0],
        [0, -5],
        [-5, 0]], dtype=numpy.float64)

    #accelerations = numpy.array([[0, 0], [0, 0], [0, 0], [0, 0]], dtype = numpy.float64)

    masses = numpy.array(
        [100000000000, 100000000000, 100000000000, 100000000000],
        dtype=numpy.float64)

    d_t = 1

    fig, axis = matplotlib.pyplot.subplots()
    axis.set_xlim(-1000, 1000)
    axis.set_ylim(-1000, 1000)

    points, = axis.plot(positions[:, 0], positions[:, 1], marker='o', linestyle='None')

    for i in range(2):

        accelerations = numpy.array([
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0]], dtype=numpy.float64)

        for pair in itertools.combinations(range(len(masses)), 2):
            particle_a, particle_b = pair
            direction = positions[particle_b] - positions[particle_a]

            radius = numpy.linalg.norm(direction)

            force = gravity(masses[particle_a], masses[particle_b], radius)

            accelerations[particle_a] += force / masses[particle_a] * direction
            accelerations[particle_b] -= force / masses[particle_b] * direction

        velocities += accelerations * d_t

        positions += 0.5 * accelerations * d_t ** 2 + velocities * d_t

        points.set_data(positions[:, 0], positions[:, 1])

        matplotlib.pyplot.savefig("%03d.png" % i)

def main():
    """
    the simulator
    """

    particle_to_particle()

if __name__ == "__main__":
    main()
