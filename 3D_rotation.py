"""
3D Rotation around X, Y, and Z axes using Homogeneous Coordinates

This script demonstrates 3D rotations around the X, Y, and Z axes using homogeneous coordinates.
Rotation matrices for each axis:

Z-axis:
    [cosθ  -sinθ   0    0]
    [sinθ   cosθ   0    0]
    [ 0      0     1    0]
    [ 0      0     0    1]

X-axis:
    [1    0      0     0]
    [0  cosθ  -sinθ   0]
    [0  sinθ   cosθ   0]
    [0    0      0    1]

Y-axis:
    [cosθ   0   sinθ   0]
    [ 0     1    0     0]
    [-sinθ  0   cosθ   0]
    [ 0     0    0     1]
"""

import numpy as np
import matplotlib.pyplot as plt

def rotate_3d_z(point, degrees):
    """Rotate around Z-axis."""
    theta = np.radians(degrees)
    c, s = np.cos(theta), np.sin(theta)
    rotation_matrix = np.array([
        [c, -s, 0, 0],
        [s,  c, 0, 0],
        [0,  0, 1, 0],
        [0,  0, 0, 1]
    ])
    return rotation_matrix @ point

def rotate_3d_x(point, degrees):
    """Rotate around X-axis."""
    theta = np.radians(degrees)
    c, s = np.cos(theta), np.sin(theta)
    rotation_matrix = np.array([
        [1, 0,  0, 0],
        [0, c, -s, 0],
        [0, s,  c, 0],
        [0, 0,  0, 1]
    ])
    return rotation_matrix @ point

def rotate_3d_y(point, degrees):
    """Rotate around Y-axis."""
    theta = np.radians(degrees)
    c, s = np.cos(theta), np.sin(theta)
    rotation_matrix = np.array([
        [c,  0, s, 0],
        [0,  1, 0, 0],
        [-s, 0, c, 0],
        [0,  0, 0, 1]
    ])
    return rotation_matrix @ point

def visualize_rotation_3d(original, rotated, angle, axis):
    """Visualize rotation with correct axis."""
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    ax.scatter(*original[:3], color='b', s=50, label='Original')
    ax.scatter(*rotated[:3], color='r', s=50, label='Rotated')
    
    # Determine axis line coordinates
    orig_coords = original[:3]
    rot_coords = rotated[:3]
    if axis == 'Z':
        min_val, max_val = min(orig_coords[2], rot_coords[2]), max(orig_coords[2], rot_coords[2])
        line = ([0, 0], [0, 0], [min_val-2, max_val+2])
    elif axis == 'X':
        min_val, max_val = min(orig_coords[0], rot_coords[0]), max(orig_coords[0], rot_coords[0])
        line = ([min_val-2, max_val+2], [0, 0], [0, 0])
    elif axis == 'Y':
        min_val, max_val = min(orig_coords[1], rot_coords[1]), max(orig_coords[1], rot_coords[1])
        line = ([0, 0], [min_val-2, max_val+2], [0, 0])
    
    ax.plot(*line, color='g', linestyle='--', label=f'{axis}-axis')
    ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
    ax.set_title(f'3D Rotation ({angle}° around {axis}-axis)')
    ax.legend()
    plt.show()

def run_rotation_example(x, y, z, degrees, axis):
    """Run rotation example for specified axis."""
    point = np.array([x, y, z, 1])
    theta = np.radians(degrees)
    c, s = np.cos(theta), np.sin(theta)
    
    # Select rotation function
    if axis == 'Z':
        rotated = rotate_3d_z(point, degrees)
    elif axis == 'X':
        rotated = rotate_3d_x(point, degrees)
    elif axis == 'Y':
        rotated = rotate_3d_y(point, degrees)
    
    # Matrix and formula explanations
    if axis == 'Z':
        matrix = [
            f"[{c:.2f}  {-s:.2f}   0    0]",
            f"[{s:.2f}   {c:.2f}   0    0]",
            "[ 0     0    1    0]",
            "[ 0     0    0    1]"
        ]
        calc_x = x*c - y*s
        calc_y = x*s + y*c
        calc_z = z
        formulas = [
            f"x' = x*cosθ - y*sinθ = {x:.2f}*{c:.2f} - {y:.2f}*{s:.2f}",
            f"y' = x*sinθ + y*cosθ = {x:.2f}*{s:.2f} + {y:.2f}*{c:.2f}",
            f"z' remains {z}"
        ]
    elif axis == 'X':
        matrix = [
            "[1.00  0.00   0.00   0.00]",
            f"[0.00  {c:.2f}  {-s:.2f}   0.00]",
            f"[0.00  {s:.2f}   {c:.2f}   0.00]",
            "[0.00  0.00   0.00   1.00]"
        ]
        calc_x = x
        calc_y = y*c - z*s
        calc_z = y*s + z*c
        formulas = [
            f"y' = y*cosθ - z*sinθ = {y:.2f}*{c:.2f} - {z:.2f}*{s:.2f}",
            f"z' = y*sinθ + z*cosθ = {y:.2f}*{s:.2f} + {z:.2f}*{c:.2f}",
            f"x' remains {x}"
        ]
    elif axis == 'Y':
        matrix = [
            f"[{c:.2f}  0.00  {s:.2f}   0.00]",
            "[0.00  1.00  0.00   0.00]",
            f"[{-s:.2f}  0.00  {c:.2f}   0.00]",
            "[0.00  0.00  0.00   1.00]"
        ]
        calc_x = x*c + z*s
        calc_z = -x*s + z*c
        calc_y = y
        formulas = [
            f"x' = x*cosθ + z*sinθ = {x:.2f}*{c:.2f} + {z:.2f}*{s:.2f}",
            f"z' = -x*sinθ + z*cosθ = -{x:.2f}*{s:.2f} + {z:.2f}*{c:.2f}",
            f"y' remains {y}"
        ]
    
    print(f"\nExample: Rotating ({x}, {y}, {z}) by {degrees}° around {axis}-axis")
    print("Rotation Matrix:")
    for row in matrix: print(f"        {row}")
    print("\nRotation Formulas:")
    for formula in formulas: print(f"        {formula}")
    print(f"\nResult: [{calc_x:.2f}, {calc_y:.2f}, {calc_z:.2f}, 1]")
    print(f"Actual: {rotated}\n")
    
    visualize_rotation_3d(point, rotated, degrees, axis)

if __name__ == '__main__':
    # Z-axis examples
    run_rotation_example(1, 0, 0, 90, 'Z')
    run_rotation_example(0, 1, 0, 180, 'Z')
    run_rotation_example(2, 0, 3, 45, 'Z')
    
    # X-axis example
    run_rotation_example(0, 1, 0, 90, 'X')
    
    # Y-axis example
    run_rotation_example(1, 0, 0, 90, 'Y')
