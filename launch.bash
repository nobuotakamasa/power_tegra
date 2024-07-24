source ./dds.bash
source ./install/setup.bash
sudo echo ""
ARCH=$(uname-m)
if ["$ARCH" = "x86_64"]; then
    export PATH=./:$PATH
fi
ros2 launch power_publisher power_publisher.launch.py interval:=1000 ecu_name:=rqx58g
