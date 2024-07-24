source ./install/setup.bash
sudo echo ""
ros2 launch power_publisher power_publisher.launch.py interval:=1000 ecu_name:=rqx58g
