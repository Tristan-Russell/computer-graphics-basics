"""
2D Reflection using Homogeneous Coordinates

Reflection matrices:
- Over X-axis: [[1, 0, 0], [0, -1, 0], [0, 0, 1]]
- Over Y-axis: [[-1, 0, 0], [0, 1, 0], [0, 0, 1]]

Examples:
    1. Reflect (3, 2) over X → (3, -2)
    2. Reflect (-1, 4) over Y → (1, 4)
    3. Reflect (2, -3) over X → (2, 3)
"""
import numpy as np
import matplotlib.pyplot as plt
def reflect_2d(point, axis):
    """Reflect point over specified axis ('x' or 'y')"""
    if axis.lower() == 'x':
        matrix = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 1]])
    elif axis.lower() == 'y':
        matrix = np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 1]])
    return matrix @ point

def visualize_reflection_2d(original, reflected, axis):
    """Visualize reflection with mirror line"""
    plt.figure(figsize=(8, 6))
    plt.scatter(*original[:2], color='b', s=100, label='Original')
    plt.scatter(*reflected[:2], color='r', s=100, label='Reflected')
    
    # Draw mirror line
    if axis == 'x':
        plt.axhline(0, color='g', linestyle='--', label='X-axis Mirror')
    else:
        plt.axvline(0, color='g', linestyle='--', label='Y-axis Mirror')
    
    plt.title(f'2D Reflection over {axis.upper()}-axis')
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.show()

def run_2d_reflection_example(x, y, axis):
    """Run reflection example with explanations"""
    point = np.array([x, y, 1])
    reflected = reflect_2d(point, axis)
    
    print("\n" + "="*50)
    print(f"Reflecting ({x},{y}) over {axis}-axis")
    print("="*50)
    print(f"Reflection matrix:")
    print(f"[[{'1' if axis=='x' else '-1'}, 0, 0]")
    print(f" [0, {'-1' if axis=='x' else '1'}, 0]")
    print(f" [0, 0, 1]]")
    print(f"Result: ({reflected[0]}, {reflected[1]})")
    visualize_reflection_2d(point, reflected, axis)

if __name__ == '__main__':
    run_2d_reflection_example(3, 2, 'x')
    run_2d_reflection_example(-1, 4, 'y')
    run_2d_reflection_example(2, -3, 'x')