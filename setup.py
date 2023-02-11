"""webots_ros2_jetbot package setup file."""

from setuptools import setup


package_name = 'webots_ros2_jetbot'
data_files = []
data_files.append(('share/ament_index/resource_index/packages', [
    'resource/' + package_name
]))
data_files.append(('share/' + package_name + '/launch', [
    'launch/robot_launch.py',
    # 'launch/robot_tools_launch.py',
    # 'launch/robot_with_tools_launch.py',
    # 'launch/rats_life_launch.py',
    # 'launch/rats_life_waypoints_launch.py'
]))
data_files.append(('share/' + package_name + '/worlds', [
    'worlds/jetbot.wbt',
    # 'worlds/.epuck_world.wbproj',
    # 'worlds/rats_life_benchmark.wbt',
    # 'worlds/.rats_life_benchmark.wbproj'
]))
data_files.append(('share/' + package_name + '/protos', [
    # 'protos/LegoTallInterval.proto',
    # 'protos/LegoTallWall.proto'
]))
data_files.append(('share/' + package_name + '/resource', [
    # 'resource/all.rviz',
    # 'resource/nav2_params.yaml',
    # 'resource/map_rats_life.pgm',
    # 'resource/map_rats_life.yaml',
    # 'resource/nav2_rats_life_waypoints.yaml',
    # 'resource/epuck_world_map.pgm',
    # 'resource/epuck_world_map.yaml',
    # 'resource/epuck_webots.urdf',
    'resource/webots_robot_description.urdf',
    # 'resource/ros2_control.yml',
]))
data_files.append(('share/' + package_name, [
    'package.xml'
]))


setup(
    name=package_name,
    version='1.0.0',
    packages=[package_name],
    data_files=data_files,
    install_requires=['setuptools', 'launch'],
    zip_safe=True,
    author='Matthew Lock',
    author_email='mwlock@kth.se',
    maintainer='Matthew Lock',
    maintainer_email='mwlock@kth.se',
    keywords=['ROS', 'Webots', 'Robot', 'Simulation', 'Examples'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='webots_ros2_jetbot driver for Webots simulated robot',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # 'epuck_node = webots_ros2_epuck.epuck_node:main',
            # 'drive_calibrator = webots_ros2_epuck.drive_calibrator:main',
            # 'simple_mapper = webots_ros2_epuck.simple_mapper:main',
            # 'epuck_state_publisher = webots_ros2_epuck.epuck_state_publisher:main',
        ],
        'launch.frontend.launch_extension': ['launch_ros = launch_ros']
    }
)