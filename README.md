# vehicle_status_obd (ROS 2 Humble)

A minimal ROS 2 package that reads vehicle speed from an OBD-II adapter via python-OBD and publishes it as `geometry_msgs/TwistStamped` on the `can_twist` topic.

## Features
- Uses python-OBD to query OBD-II SPEED
- Publishes `geometry_msgs/TwistStamped`
- Supports synchronous and asynchronous (callback-based) modes
- Configurable serial port via launch argument/ROS parameter (`port`)

## Requirements
- ROS 2 Humble (Ubuntu 22.04 recommended)
- Python 3.8+
- python-OBD
- An OBD-II adapter (e.g., ELM327) connected via serial/USB

Install python-OBD:
```bash
pip3 install obd
```

You may need serial port permissions:
```bash
sudo usermod -a -G dialout $USER
# log out and log back in to apply group changes
```

## Build
From your workspace root:
```bash
source /opt/ros/humble/setup.bash
colcon build --packages-select vehicle_status_obd
source install/setup.bash
```

## Run
Synchronous node (periodic polling):
```bash
ros2 launch vehicle_status_obd run.launch.py
```

Asynchronous node (callback-based):
```bash
ros2 launch vehicle_status_obd run_async.launch.py
```

Override the OBD-II serial port (default: `/dev/ttyUSB0`):
```bash
ros2 launch vehicle_status_obd run.launch.py port:=/dev/ttyUSB1
# or
ros2 launch vehicle_status_obd run_async.launch.py port:=/dev/ttyUSB1
```

## Nodes and Parameters
- Node executables:
  - `obd_send_vel` (synchronous)
  - `obd_send_vel_async` (asynchronous)
- Parameters:
  - `port` (string, default: `/dev/ttyUSB0`): Serial device for the OBD-II adapter

## Topics
- Published
  - `can_twist` (`geometry_msgs/TwistStamped`)
    - `header.frame_id` = `/vehicle`
    - `twist.linear.x` = speed magnitude reported by python-OBD
      - Note: python-OBD typically provides speed in km/h. The raw magnitude is published as-is.

## Package Layout
- Build type: `ament_python`
- Launch files: `launch/run.launch.py`, `launch/run_async.launch.py`
- Python entry points:
  - `vehicle_status_obd/obd_send_vel.py:main`
  - `vehicle_status_obd/obd_send_vel_async.py:main`

## Troubleshooting
- No OBD device detected / permission denied:
  - Ensure the adapter appears as `/dev/ttyUSB*` or similar and you have permissions (`dialout` group)
  - Try another port via `port:=/dev/ttyUSB1`
- python-OBD not found:
  - `pip3 install obd`
- No speed value published:
  - Ensure the vehicle ignition is on and the adapter is properly connected
  - Some vehicles/adapters require a specific baud rate or protocol; refer to python-OBD docs
