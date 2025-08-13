from setuptools import setup, find_packages

package_name = 'vehicle_status_obd'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/vehicle_status_obd']),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', [
            'launch/run.launch.py',
            'launch/run_async.launch.py',
        ]),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mujin',
    maintainer_email='mujin@todo.todo',
    description='Publish vehicle velocity from OBD-II via python-OBD as geometry_msgs/TwistStamped',
    license='TODO',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'obd_send_vel = vehicle_status_obd.obd_send_vel:main',
            'obd_send_vel_async = vehicle_status_obd.obd_send_vel_async:main',
        ],
    },
) 