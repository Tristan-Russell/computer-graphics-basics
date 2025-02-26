"""
3D Reflection using Homogeneous Coordinates

Reflection matrices:
- XY-plane: [[1,0,0,0], [0,1,0,0], [0,0,-1,0], [0,0,0,1]]
- XZ-plane: [[1,0,0,0], [0,-1,0,0], [0,0,1,0], [0,0,0,1]]
- YZ-plane: [[-1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]]

Examples:
    1. Reflect (2, 3, 4) over XY → (2, 3, -4)
    2. Reflect (1, -2, 3) over YZ → (-1, -2, 3)
    3. Reflect (4, 5, 6) over XZ → (4, -5, 6)
"""
import numpy as np
import matplotlib.pyplot as plt

def reflect_3d(point, plane):
    """Reflect 3D point over specified plane"""
    matrix = np.eye(4)
    if plane.lower() == 'xy':
        matrix[2,2] = -1
    elif plane.lower() == 'xz':
        matrix[1,1] = -1
    elif plane.lower() == 'yz':
        matrix[0,0] = -1
    return matrix @ point

def visualize_reflection_3d(original, reflected, plane):
    """3D visualization of reflection"""
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot points
    ax.scatter(*original[:3], s=100, label='Original')
    ax.scatter(*reflected[:3], s=100, label='Reflected')
    
    # Draw reflection plane
    if plane == 'xy':
        xx, yy = np.meshgrid(range(-5,6), range(-5,6))
        ax.plot_surface(xx, yy, np.zeros_like(xx), alpha=0.3, color='g')
    elif plane == 'xz':
        xx, zz = np.meshgrid(range(-5,6), range(-5,6))
        ax.plot_surface(xx, np.zeros_like(xx), zz, alpha=0.3, color='g')
    elif plane == 'yz':
        yy, zz = np.meshgrid(range(-5,6), range(-5,6))
        ax.plot_surface(np.zeros_like(yy), yy, zz, alpha=0.3, color='g')
    
    ax.set_title(f'3D Reflection over {plane.upper()}-plane')
    ax.legend()
    plt.show()

def run_3d_reflection_example(x, y, z, plane):
    """Run 3D reflection example"""
    point = np.array([x, y, z, 1])
    reflected = reflect_3d(point, plane)
    
    print("\n" + "="*50)
    print(f"Reflecting ({x},{y},{z}) over {plane}-plane")
    print("="*50)
    print(f"Result: ({reflected[0]}, {reflected[1]}, {reflected[2]})")
    visualize_reflection_3d(point, reflected, plane)

if __name__ == '__main__':
    run_3d_reflection_example(2, 3, 4, 'xy')
    run_3d_reflection_example(1, -2, 3, 'yz')
    run_3d_reflection_example(4, 5, 6, 'xz')