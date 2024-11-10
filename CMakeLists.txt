cmake_minimum_required(VERSION 3.15)
project(PCLPlayground)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Include Conan dependencies
# include(${CMAKE_SOURCE_DIR}/conan/conanbuildinfo.cmake)

# Specify where to look for Conan-generated package configuration files
list(APPEND CMAKE_PREFIX_PATH "${CMAKE_SOURCE_DIR}/conan/build/Release/generators")

find_package(PCL 1.13.1 REQUIRED)
include_directories(${PCL_INCLUDE_DIRS})
link_directories(${PCL_LIBRARY_DIRS})
add_definitions(${PCL_DEFINITIONS})

add_executable(main src/main.cpp)
target_link_libraries(main ${PCL_LIBRARIES})