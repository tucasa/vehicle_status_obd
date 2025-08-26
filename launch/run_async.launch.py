from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    port = LaunchConfiguration('port')
    
    return LaunchDescription([
        DeclareLaunchArgument(
            'port',
            default_value='/dev/ttyUSB0',
            description='The port to use for the OBD-II connection'
        ),
		Node(
			package='vehicle_status_obd',
			executable='obd_send_vel_async',
			name='obd_send_vel_async',
			output='screen',
			parameters=[
				{'port': port},
			],
		),
	]) 