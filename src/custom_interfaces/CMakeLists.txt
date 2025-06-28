cmake_minimum_required(VERSION 3.8)
project(custom_interfaces)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(geometry_msgs REQUIRED)

# Generate interfaces
rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/TargetCoordinates.msg"
  "srv/SetLed.srv"
  "action/CountUntil.action"
  DEPENDENCIES geometry_msgs
)

# Export dependencies
ament_export_dependencies(
  rosidl_default_runtime
  geometry_msgs
)

ament_package()
