#source ./dds.bash
source ./install/setup.bash
sudo echo ""
ARCH=$(uname -m)
if [ "$ARCH" = "x86_64" ]; then
    #for test
    export PATH="./:$PATH"
fi
echo "arch=$ARCH"
HOSTNAME=$(uname -n)
echo "hostname=$HOSTNAME"
#echo $PATH
ros2 launch power_publisher tegra_publisher.launch.py interval:=1000 ecu_name:=$HOSTNAME
