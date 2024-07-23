from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='power_publisher', 
            executable='power_publisher',
            name='power_publisher', 
            output='screen' 
        )
    ])
