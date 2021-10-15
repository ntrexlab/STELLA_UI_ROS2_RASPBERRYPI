#!/usr/bin/python3

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='stella_ui',
            executable='stella_ui_node',
            name='stella_ui_node',
            output='screen'
        )
    ])


