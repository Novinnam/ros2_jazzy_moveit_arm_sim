cmake_minimum_required(VERSION 3.16)
project(my_cpp_pkg)

set(my_cpp_pkg_MAJOR_VERSION 0)
set(my_cpp_pkg_MINOR_VERSION 0)
set(my_cpp_pkg_PATCH_VERSION 0)
set(my_cpp_pkg_VERSION
  ${my_cpp_pkg_MAJOR_VERSION}.${my_cpp_pkg_MINOR_VERSION}.${my_cpp_pkg_PATCH_VERSION})

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()


# find dependencies
find_package(rclcpp REQUIRED)
