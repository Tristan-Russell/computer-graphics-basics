# Graphics and Game Design Transformations
This repository contains Python scripts demonstrating various 2D and 3D transformations using homogeneous coordinates. Each script includes detailed explanations, formulas, and visualizations.

## Table of Contents
- [2D Transformations](#2d-transformations)
- [3D Transformations](#3d-transformations)
- [Reflections](#reflections)
- [Usage](#usage)

## 2D Transformations
### 1. 2D Translation
- **File**: [2D_Translation.py](2D_Translation.py)
- **Formula**:
  ```
  [1 0 tx]
  [0 1 ty]
  [0 0 1 ]
  ```
- **Description**: Moves a point by `(tx, ty)` in 2D space.

### 2. 2D Scaling
- **File**: [2D_Scaling.py](2D_Scaling.py)
- **Formula**:
  ```
  [sx  0   0]
  [0   sy  0]
  [0   0   1]
  ```
- **Description**: Scales a point by `(sx, sy)` in 2D space. Negative values create reflections.

### 3. 2D Rotation
- **File**: [2D_Rotation.py](2D_Rotation.py)
- **Formula**:
  ```
  [cosθ  -sinθ  0]
  [sinθ   cosθ  0]
  [0      0     1]
  ```
- **Description**: Rotates a point by angle `θ` around the origin.

## 3D Transformations
### 1. 3D Translation
- **File**: [3D_Translation.py](3D_Translation.py)
- **Formula**:
  ```
  [1  0  0  tx]
  [0  1  0  ty]
  [0  0  1  tz]
  [0  0  0   1]
  ```
- **Description**: Moves a point by `(tx, ty, tz)` in 3D space.

### 2. 3D Scaling
- **File**: [3D_Scaling.py](3D_Scaling.py)
- **Formula**:
  ```
  [sx  0   0   0]
  [0   sy  0   0]
  [0   0   sz  0]
  [0   0   0   1]
  ```
- **Description**: Scales a point by `(sx, sy, sz)` in 3D space.

### 3. 3D Rotation (Z-axis)
- **File**: [3D_Rotation_Z.py](3D_Rotation_Z.py)
- **Formula**:
  ```
  [cosθ  -sinθ  0  0]
  [sinθ   cosθ  0  0]
  [0      0     1  0]
  [0      0     0  1]
  ```
- **Description**: Rotates a point around the Z-axis by angle `θ`.

## Reflections
### 1. 2D Reflections
- **File**: [2D_Reflections.py](2D_Reflections.py)
- **Formulas**:
  - Over X-axis:
    ```
    [1  0  0]
    [0 -1  0]
    [0  0  1]
    ```
  - Over Y-axis:
    ```
    [-1  0  0]
    [ 0  1  0]
    [ 0  0  1]
    ```
  - Over y=x:
    ```
    [0  1  0]
    [1  0  0]
    [0  0  1]
    ```
  - Over y=-x:
    ```
    [ 0 -1  0]
    [-1  0  0]
    [ 0  0  1]
    ```
- **Description**: Reflects a point over the specified axis or line.

### 2. 3D Reflections
- **File**: [3D_Reflections.py](3D_Reflections.py)
- **Formulas**:
  - Over XY-plane:
    ```
    [1  0  0  0]
    [0  1  0  0]
    [0  0 -1  0]
    [0  0  0  1]
    ```
  - Over XZ-plane:
    ```
    [1  0  0  0]
    [0 -1  0  0]
    [0  0  1  0]
    [0  0  0  1]
    ```
  - Over YZ-plane:
    ```
    [-1  0  0  0]
    [ 0  1  0  0]
    [ 0  0  1  0]
    [ 0  0  0  1]
    ```
- **Description**: Reflects a point over the specified plane in 3D space.

## Usage
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/graphics-transformations.git
   ```
2. Navigate to the desired script:
   ```
   cd graphics-transformations
   ```
3. Run the script:
   ```
   python 3D_Translation.py
   ```
4. View the console output and visualizations.

## Dependencies
- Python 3.x
- NumPy (`pip install numpy`)
- Matplotlib (`pip install matplotlib`)

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.