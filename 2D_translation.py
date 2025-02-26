"""
2D Translation using Homogeneous Coordinates

This script demonstrates 2D translation using a 3x3 homogeneous matrix:
    [1 0 tx]
    [0 1 ty]
    [0 0 1 ]

Examples:
    1. Translating (2, 3) by (1, -1) → (3, 2)
    2. Translating (0, 0) by (5, 5) → (5, 5)
    3. Translating (-1, 4) by (2, -3) → (1, 1)
"""

import numpy as np
import matplotlib.pyplot as plt

def translate_2d(point, tx, ty):
    """Translate 2D point using homogeneous coordinates"""
    translation_matrix = np.array([
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1]
    ])
    return translation_matrix @ point

def visualize_translation_2d(original, translated):
    """Visualize 2D translation with arrows"""
    plt.figure(figsize=(8, 6))
    plt.scatter(*original[:2], color='b', s=100, label='Original')
    plt.scatter(*translated[:2], color='r', s=100, label='Translated')
    plt.quiver(*original[:2], translated[0]-original[0], translated[1]-original[1], 
               angles='xy', scale_units='xy', scale=1, color='k', linestyle='--')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('2D Translation Visualization')
    plt.grid(True)
    plt.legend()
    plt.axis('equal')
    plt.show()

def run_2d_translation_example(x, y, tx, ty):
    """Run complete translation example"""
    point = np.array([x, y, 1])
    translated = translate_2d(point, tx, ty)
    
    print("\n" + "="*50)
    print(f"Translating ({x},{y}) by ({tx},{ty})")
    print("="*50)
    print(f"Original point: [{x}, {y}, 1]")
    print(f"Translated: [{translated[0]}, {translated[1]}, 1]")
    visualize_translation_2d(point, translated)

if __name__ == '__main__':
    run_2d_translation_example(2, 3, 1, -1)
    run_2d_translation_example(0, 0, 5, 5)
    run_2d_translation_example(-1, 4, 2, -3)