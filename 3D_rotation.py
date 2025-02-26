"""
3D Rotation around Z-axis using Homogeneous Coordinates

This script demonstrates how to perform a 3D rotation around the Z-axis using homogeneous coordinates. Rotation is a linear transformation that preserves distances and angles. In 3D homogeneous coordinates (x, y, z, 1), rotation around the Z-axis is represented by:

    [cosθ  -sinθ   0    0]
    [sinθ   cosθ   0    0]
    [ 0      0     1    0]
    [ 0      0     0    1]

When this matrix multiplies a point [x, y, z, 1], it results in:
    [xcosθ - ysinθ, xsinθ + ycosθ, z, 1]

Examples included:
    1. Rotating (1, 0, 0) by 90° becomes (0, 1, 0)
    2. Rotating (0, 1, 0) by 180° becomes (0, -1, 0)
    3. Rotating (2, 0, 3) by 45° becomes (√2, √2, 3)
"""

import numpy as np
import matplotlib.pyplot as plt

def rotate_3d_z(point, degrees):
    """
    Rotate a 3D point around the Z-axis using homogeneous coordinates.

    Parameters
    ----------
    point : numpy.ndarray
        A 4-element array representing the point in homogeneous coordinates.
    degrees : float
        Rotation angle in degrees (counterclockwise).

    Returns
    -------
    numpy.ndarray
        The rotated point in homogeneous coordinates.

    Explanation:
    ------------
    The rotation matrix for Z-axis is:
        [cosθ  -sinθ   0   0]
        [sinθ   cosθ   0   0]
        [ 0      0     1   0]
        [ 0      0     0   1]
    """
    theta = np.radians(degrees)
    c, s = np.cos(theta), np.sin(theta)
    rotation_matrix = np.array([
        [c, -s, 0, 0],
        [s,  c, 0, 0],
        [0,  0, 1, 0],
        [0,  0, 0, 1]
    ])
    return rotation_matrix @ point

def visualize_rotation_3d(original, rotated, angle):
    """Visualize original and rotated points in 3D space."""
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot points
    ax.scatter(*original[:3], color='b', s=50, label='Original')
    ax.scatter(*rotated[:3], color='r', s=50, label='Rotated')
    
    # Draw rotation axis (Z-axis)
    ax.plot([0, 0], [0, 0], [min(original[2], rotated[2])-2, max(original[2], rotated[2])+2], 
            color='g', linestyle='--', label='Z-axis')
    
    # Configuration
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(f'3D Rotation ({angle}° around Z-axis)')
    ax.legend()
    plt.show()

def run_rotation_example(x, y, z, degrees):
    """Run and explain a rotation example."""
    point = np.array([x, y, z, 1])
    rotated = rotate_3d_z(point, degrees)
    theta = np.radians(degrees)
    c, s = np.cos(theta), np.sin(theta)
    
    print("-------------------------------------------------------")
    print(f"Example: Rotating ({x}, {y}, {z}) by {degrees}° around Z-axis")
    print("-------------------------------------------------------")
    print("Step 1: Homogeneous coordinates:")
    print(f"         Original point: {point}")
    print("\nStep 2: Rotation matrix:")
    print(f"        [{c:.2f}  {-s:.2f}  0  0]")
    print(f"        [{s:.2f}   {c:.2f}  0  0]")
    print(f"        [ 0     0   1  0]")
    print(f"        [ 0     0   0  1]")
    print("\nStep 3: Apply rotation formulas:")
    print(f"        x' = x*cosθ - y*sinθ = {x:.2f}*{c:.2f} - {y:.2f}*{s:.2f}")
    print(f"        y' = x*sinθ + y*cosθ = {x:.2f}*{s:.2f} + {y:.2f}*{c:.2f}")
    print(f"        z' remains {z}")
    print("\nResult:")
    print(f"        Calculated: [{x*c - y*s:.2f}, {x*s + y*c:.2f}, {z}, 1]")
    print(f"        Actual:     {rotated}")
    visualize_rotation_3d(point, rotated, degrees)

if __name__ == '__main__':
    # Example 1: 90° rotation of (1, 0, 0)
    run_rotation_example(1, 0, 0, 90)
    
    # Example 2: 180° rotation of (0, 1, 0)
    run_rotation_example(0, 1, 0, 180)
    
    # Example 3: 45° rotation of (2, 0, 3)
    run_rotation_example(2, 0, 3, 45)