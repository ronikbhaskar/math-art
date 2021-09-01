"""
This file contains functions that represent the systems of ordinary
differential equations that govern certain strange attractors.
"""

def lorenz(xyz, t, sigma, beta, rho):
    """The most famous of the strange attractors."""

    x, y, z = xyz

    dx = sigma * (y - x)   # dt
    dy = x * (rho - z) - y # dt
    dz = x * y - beta * z  # dt

    return dx, dy, dz

def halvorsen(xyz, t, a):
    """Like a rose with only three petals. Cyclically symmetric."""

    x, y, z = xyz

    dx = - a * x - 4 * (y + z) - y ** 2 # dt
    dy = - a * y - 4 * (z + x) - z ** 2 # dt
    dz = - a * z - 4 * (x + y) - x ** 2 # dt

    return dx, dy, dz

def aizawa(xyz, t, alpha, beta, gamma, delta, epsilon, zeta):
    """Visually resembles a magnetic field. Almost spherical."""

    x, y, z = xyz

    dx = x * (z - beta) - delta * y                                  # dt
    dy = y * (z - beta) + delta * x                                  # dt
    dz = gamma + alpha * z - z ** 3 / 3 - \
         (x ** 2 + y ** 2) * (1 + epsilon * z) + zeta * z * (x ** 3) # dt

    return dx, dy, dz
