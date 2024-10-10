#source ./dds.bash
source ./install/setup.bash
ros2 launch power_publisher nvidia_publisher.launch.py interval:=1000 ecu_name:=nvidia
