"""
3D Translation using Homogeneous Coordinates

This script demonstrates how to perform a 3D translation using homogeneous
coordinates. In 3D, a point (x, y, z) is represented as:
    [x, y, z, 1]

This extra coordinate allows us to represent translations (which are not linear
transformations in the usual 3D space) as a matrix multiplication.

The translation is represented by a 4x4 matrix:
    [1  0  0  tx]
    [0  1  0  ty]
    [0  0  1  tz]
    [0  0  0   1]

When this matrix multiplies a point in homogeneous coordinates, it produces:
    [x + tx, y + ty, z + tz, 1]
which corresponds to moving the point by tx, ty, and tz along the x, y, and z axes respectively.

Examples included:
    1. Translating point (2, 3, 4) by (3, 2, -1) results in (5, 5, 3)
    2. Translating point (0, 0, 0) by (1, 1, 1) results in (1, 1, 1)
    3. Translating point (1, -1, 2) by (-3, 4, 5) results in (-2, 3, 7)

This code is ideal for teaching because it prints detailed explanations of the math,
shows the matrix used, calculates the result step-by-step, and visualizes the translation.
"""

import numpy as np
import matplotlib.pyplot as plt
def translate_3d(point, tx, ty, tz):
    """
    Translate a 3D point in homogeneous coordinates by tx, ty, and tz.

    Parameters
    ----------
    point : numpy.ndarray
        A 4-element array representing the point in homogeneous coordinates [x, y, z, 1].
    tx : float
        Translation amount in the x-direction.
    ty : float
        Translation amount in the y-direction.
    tz : float
        Translation amount in the z-direction.

    Returns
    -------
    numpy.ndarray
        The translated point in homogeneous coordinates [x+tx, y+ty, z+tz, 1].
    
    Explanation:
    ------------
    The translation matrix in homogeneous coordinates is defined as:
        [1  0  0  tx]
        [0  1  0  ty]
        [0  0  1  tz]
        [0  0  0   1]
    
    Multiplying this matrix by the point [x, y, z, 1] results in:
        [x + tx, y + ty, z + tz, 1]
    which is equivalent to moving the point by (tx, ty, tz).
    """
    translation_matrix = np.array([
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1, tz],
        [0, 0, 0,  1]
    ])
    translated_point = translation_matrix @ point
    return translated_point

def visualize_translation_3d(point, translated_point, tx, ty, tz):
    """
    Visualize the original and translated 3D points using matplotlib.

    Parameters
    ----------
    point : numpy.ndarray
        The original point in homogeneous coordinates [x, y, z, 1].
    translated_point : numpy.ndarray
        The translated point in homogeneous coordinates.
    tx : float
        The translation in the x-direction.
    ty : float
        The translation in the y-direction.
    tz : float
        The translation in the z-direction.

    Explanation:
    ------------
    This function creates a 3D scatter plot to show:
      - The original point (blue)
      - The translated point (red)
    
    It draws an arrow from the original point to the translated point using the quiver function,
    illustrating the translation vector.
    """
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot the original and translated points.
    ax.scatter(point[0], point[1], point[2], color='b', s=50, label='Original Point')
    ax.scatter(translated_point[0], translated_point[1], translated_point[2], color='r', s=50, label='Translated Point')
    
    # Draw an arrow from the original to the translated point.
    ax.quiver(point[0], point[1], point[2], tx, ty, tz, arrow_length_ratio=0.1, color='k')
    
    # Set axis labels and title.
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    ax.set_title('3D Translation using Homogeneous Coordinates')
    ax.legend()
    
    # Set axis limits for clear visualization.
    min_vals = np.minimum(point[:3], translated_point[:3])
    max_vals = np.maximum(point[:3], translated_point[:3])
    ax.set_xlim([min_vals[0] - 2, max_vals[0] + 5])
    ax.set_ylim([min_vals[1] - 2, max_vals[1] + 5])
    ax.set_zlim([min_vals[2] - 2, max_vals[2] + 5])
    
    plt.show()

def run_example_3d(x, y, z, tx, ty, tz):
    """
    Run a 3D translation example by printing detailed explanations and visualizing the result.

    Parameters
    ----------
    x : float
        The x-coordinate of the original point.
    y : float
        The y-coordinate of the original point.
    z : float
        The z-coordinate of the original point.
    tx : float
        Translation in the x-direction.
    ty : float
        Translation in the y-direction.
    tz : float
        Translation in the z-direction.
    """
    # Create the original point in homogeneous coordinates.
    point = np.array([x, y, z, 1])
    
    # Compute the translated point.
    translated_point = translate_3d(point, tx, ty, tz)
    
    # Print detailed explanation to the console.
    print("-------------------------------------------------------")
    print("Example: Translating point ({}, {}, {}) by the vector ({}, {}, {})".format(x, y, z, tx, ty, tz))
    print("-------------------------------------------------------")
    print("Step 1: Represent the point in homogeneous coordinates:")
    print("         [x, y, z, 1]  -> In our case: {}".format(point))
    print("")
    print("Step 2: Define the translation matrix for 3D:")
    print("         [1  0  0  tx]")
    print("         [0  1  0  ty]")
    print("         [0  0  1  tz]")
    print("         [0  0  0   1]")
    print("         For our example, this becomes:")
    print("         ", np.array([[1, 0, 0, tx],
                             [0, 1, 0, ty],
                             [0, 0, 1, tz],
                             [0, 0, 0,  1]]))
    print("")
    print("Step 3: Apply the translation formula:")
    print("         x' = x + tx")
    print("         y' = y + ty")
    print("         z' = z + tz")
    print("")
    print("Calculation:")
    print("         x' = {} + {} = {}".format(x, tx, x + tx))
    print("         y' = {} + {} = {}".format(y, ty, y + ty))
    print("         z' = {} + {} = {}".format(z, tz, z + tz))
    print("")
    print("Resulting translated point in homogeneous coordinates:")
    print("         {}".format(translated_point))
    difference = translated_point - point
    print("")
    print("Difference (translated_point - original_point): {}".format(difference))
    print("This difference should equal the translation vector: ({}, {}, {})".format(tx, ty, tz))
    print("")
    
    # Visualize the 3D translation.
    visualize_translation_3d(point, translated_point, tx, ty, tz)

if __name__ == '__main__':
    # Example 1:
    # Translating point (2, 3, 4) by (3, 2, -1) should yield (5, 5, 3)
    run_example_3d(2, 3, 4, 3, 2, -1)
    
    # Example 2:
    # Translating point (0, 0, 0) by (1, 1, 1) should yield (1, 1, 1)
    run_example_3d(0, 0, 0, 1, 1, 1)
    
    # Example 3:
    # Translating point (1, -1, 2) by (-3, 4, 5) should yield (-2, 3, 7)
    run_example_3d(1, -1, 2, -3, 4, 5)
