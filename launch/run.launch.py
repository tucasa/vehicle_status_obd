from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    port = LaunchConfiguration('port')
    rate = LaunchConfiguration('rate')
    
    return LaunchDescription([
        DeclareLaunchArgument(
            'port',
            default_value='/dev/ttyUSB0',
            description='The port to use for the OBD-II connection'
        ),
        DeclareLaunchArgument(
            'rate',
            default_value='30.0',
            description='The rate to publish the CAN twist messages'
        ),
		Node(
			package='vehicle_status_obd',
			executable='obd_send_vel',
			name='obd_send_vel',
			output='screen',
			parameters=[
				{'port': port},
				{'rate': rate},
			],
		),
	]) 