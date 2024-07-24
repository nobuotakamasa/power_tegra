from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    interval = DeclareLaunchArgument(
        'interval',
        default_value='1002',
        description='interval time'
    )

    node = Node(
        package='power_publisher',
        executable='power_publisher',
        name='power_publisher',
        output='screen',
        parameters=[{
            'interval': LaunchConfiguration('interval')
        }]
    )

    return LaunchDescription([
        interval,
        node
    ])
