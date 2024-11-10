# PCL_CPP_Playground

This repository is a playground for learning, practicing, and implementing various PointCloud algorithms using the Point Cloud Library (PCL) and modern C++.

## Prerequisites

To build and run this project, you need:

- **C++20-compatible compiler** (e.g., GCC 11 or newer)
- **CMake** (version 3.15 or higher)
- **Conan** (version 2.0 or higher)

### Install Conan

If you don’t have Conan installed, you can install it with:

```
python3 -m pip install conan
```

## Setting Up Dependencies
The project uses Conan to manage dependencies like PCL, CMake, and Eigen. Follow these steps to install the required libraries:
```
$cd conan
$conan install . --build=missing
```

## Building the Project
Once the dependencies are installed, follow these steps to build the project:
```
$cd ..
$mkdir build && cd build
$cmake -DCMAKE_BUILD_TYPE=Release ..
$make
```