"""
3D Scaling using Homogeneous Coordinates

This script demonstrates 3D scaling using homogeneous coordinates. Scaling transforms an object's size by multiplying each coordinate by a scaling factor. The scaling matrix is:

    [sx  0   0   0]
    [0   sy  0   0]
    [0   0   sz  0]
    [0   0   0   1]

When multiplied by [x, y, z, 1], it results in:
    [sx*x, sy*y, sz*z, 1]

Examples included:
    1. Scaling (2, 3, 4) by (2, 1, 0.5) → (4, 3, 2)
    2. Scaling (1, 1, 1) by (0.5, 0.5, 0.5) → (0.5, 0.5, 0.5)
    3. Scaling (3, -2, 5) by (-1, 2, 1) → (-3, -4, 5)
"""

import numpy as np
import matplotlib.pyplot as plt

def scale_3d(point, sx, sy, sz):
    """
    Scale a 3D point using homogeneous coordinates.

    Parameters
    ----------
    point : numpy.ndarray
        Homogeneous coordinates [x, y, z, 1]
    sx, sy, sz : float
        Scaling factors for each axis

    Returns
    -------
    numpy.ndarray
        Scaled point in homogeneous coordinates
    """
    scaling_matrix = np.array([
        [sx, 0,  0,  0],
        [0,  sy, 0,  0],
        [0,  0,  sz, 0],
        [0,  0,  0,  1]
    ])
    return scaling_matrix @ point

def visualize_scaling_3d(original, scaled):
    """Visualize original and scaled points in 3D space."""
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot points and vectors
    for pt, color, label in [(original, 'b', 'Original'), (scaled, 'r', 'Scaled')]:
        ax.scatter(*pt[:3], color=color, s=50, label=label)
        ax.plot([0, pt[0]], [0, pt[1]], [0, pt[2]], 
                color=color, linestyle=':', alpha=0.5)
    
    # Configuration
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Scaling Transformation')
    ax.legend()
    plt.show()

def run_scaling_example(x, y, z, sx, sy, sz):
    """Run and explain a scaling example."""
    point = np.array([x, y, z, 1])
    scaled = scale_3d(point, sx, sy, sz)
    
    print("-------------------------------------------------------")
    print(f"Example: Scaling ({x}, {y}, {z}) by ({sx}, {sy}, {sz})")
    print("-------------------------------------------------------")
    print("Step 1: Homogeneous coordinates:")
    print(f"         Original point: {point}")
    print("\nStep 2: Scaling matrix:")
    print(f"        [{sx}  0   0   0]")
    print(f"        [0   {sy}  0   0]")
    print(f"        [0   0   {sz}  0]")
    print(f"        [0   0   0   1]")
    print("\nStep 3: Apply scaling formulas:")
    print(f"        x' = {x}*{sx} = {x*sx}")
    print(f"        y' = {y}*{sy} = {y*sy}")
    print(f"        z' = {z}*{sz} = {z*sz}")
    print("\nResult:")
    print(f"        Calculated: [{x*sx}, {y*sy}, {z*sz}, 1]")
    print(f"        Actual:     {scaled}")
    visualize_scaling_3d(point, scaled)

if __name__ == '__main__':
    # Example 1: Scale (2, 3, 4) by (2, 1, 0.5)
    run_scaling_example(2, 3, 4, 2, 1, 0.5)
    
    # Example 2: Scale (1, 1, 1) by (0.5, 0.5, 0.5)
    run_scaling_example(1, 1, 1, 0.5, 0.5, 0.5)
    
    # Example 3: Scale (3, -2, 5) by (-1, 2, 1)
    run_scaling_example(3, -2, 5, -1, 2, 1)