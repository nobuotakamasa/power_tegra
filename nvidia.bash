#source ./dds.bash
source ./install/setup.bash
echo "hostname=$HOSTNAME"
ros2 launch power_publisher nvidia_publisher.launch.py interval:=1000 ecu_name:=$HOSTNAME
