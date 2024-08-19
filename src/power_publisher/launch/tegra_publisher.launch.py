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

    ecu_name = DeclareLaunchArgument(
        'ecu_name',
        default_value='no_name',
        description='name of this ECU'
    )

    node = Node(
        package='power_publisher',
        executable='tegra_publisher',
        name='tegra_publisher',
        output='screen',
        parameters=[{
            'ecu_name': LaunchConfiguration('ecu_name')
        }]
    )

    return LaunchDescription([
        ecu_name,
        interval,
        node
    ])
