cmake_minimum_required(VERSION 3.5)
project(vehicle_status_obd)

find_package(ament_cmake REQUIRED)

# No C++/C build targets; Python package is installed via setup.py

install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
