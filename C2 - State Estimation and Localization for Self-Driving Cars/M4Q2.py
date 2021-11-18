from numpy import *


def sph_to_cart(epsilon, alpha, r):
    """
    Transform sensor readings to Cartesian coordinates in the sensor
    frame. The values of epsilon and alpha are given in radians, while
    r is in metres. Epsilon is the elevation angle and alpha is the
    azimuth angle (i.e., in the x,y plane).
    """
    p = zeros(3)  # Position vector

    # Your code here
    p[0] = r * cos(alpha) * cos(epsilon)
    p[1] = r * sin(alpha) * cos(epsilon)
    p[2] = r * sin(epsilon)

    return p


def estimate_params(P):
    """
    Estimate parameters from sensor readings in the Cartesian frame.
    Each row in the P matrix contains a single 3D point measurement;
    the matrix P has size n x 3 (for n points). The format is:

    P = [[x1, y1, z1],
         [x2, x2, z2], ...]

    where all coordinate values are in metres. Three parameters are
    required to fit the plane, a, b, and c, according to the equation

    z = a + bx + cy

    The function should return the parameters as a NumPy array of size
    three, in the order [a, b, c].
    """
    param_est = zeros(3)

    # Your code here
    a1 = ones((P.shape[0], 1))
    A = array([a1[:, 0], P[:, 0], P[:, 1]]).T
    b = P[:, 2]
    x_hat = linalg.inv(A.T @ A) @ A.T @ b
    param_est[0] = x_hat[0]
    param_est[1] = x_hat[1]
    param_est[2] = x_hat[2]

    return param_est

P = random.rand(20, 3)

print(estimate_params(P))