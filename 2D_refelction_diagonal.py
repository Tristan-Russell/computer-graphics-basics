"""
2D Reflection over Diagonal Lines

Special reflection cases:
1. Over y=x line: swaps coordinates
   Matrix: [0 1 0]
           [1 0 0]
           [0 0 1]

2. Over y=-x line: swaps and negates
   Matrix: [ 0 -1 0]
           [-1  0 0]
           [ 0  0 1]

Examples:
1. Reflect (2, 5) over y=x → (5, 2)
2. Reflect (3, 4) over y=-x → (-4, -3)
3. Reflect (-1, 2) over y=x → (2, -1)
"""
import numpy as np
import matplotlib.pyplot as plt
def reflect_2d_diagonal(point, line):
    """Reflect over y=x or y=-x"""
    if line.lower() == 'y=x':
        matrix = np.array([[0, 1, 0],
                           [1, 0, 0],
                           [0, 0, 1]])
    elif line.lower() == 'y=-x':
        matrix = np.array([[0, -1, 0],
                           [-1, 0, 0],
                           [0, 0, 1]])
    return matrix @ point

def visualize_diagonal_reflection(original, reflected, line):
    """Visualize reflection with diagonal mirror line"""
    plt.figure(figsize=(8, 6))
    
    # Plot points
    plt.scatter(*original[:2], color='b', s=100, label='Original')
    plt.scatter(*reflected[:2], color='r', s=100, label='Reflected')
    
    # Draw mirror line
    lim = max(abs(np.concatenate([original, reflected]))) + 1
    x = np.linspace(-lim, lim, 100)
    if line == 'y=x':
        plt.plot(x, x, 'g--', label='y=x')
    else:
        plt.plot(x, -x, 'g--', label='y=-x')
    
    plt.title(f'Reflection over {line}')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.axis('equal')
    plt.legend()
    plt.show()

def run_diagonal_reflection_example(x, y, line):
    """Run diagonal reflection example"""
    point = np.array([x, y, 1])
    reflected = reflect_2d_diagonal(point, line)
    
    print("\n" + "="*50)
    print(f"Reflecting ({x},{y}) over {line}")
    print("="*50)
    print("Reflection matrix:")
    if line == 'y=x':
        print("[0 1 0]\n[1 0 0]\n[0 0 1]")
    else:
        print("[ 0 -1 0]\n[-1 0 0]\n[ 0 0 1]")
    print(f"\nCalculation:")
    print(f"Original: ({x}, {y})")
    print(f"Reflected: ({reflected[0]}, {reflected[1]})")
    visualize_diagonal_reflection(point, reflected, line)

if __name__ == '__main__':
    run_diagonal_reflection_example(2, 5, 'y=x')
    run_diagonal_reflection_example(3, 4, 'y=-x')
    run_diagonal_reflection_example(-1, 2, 'y=x')