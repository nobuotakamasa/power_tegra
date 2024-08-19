
import rclpy
from std_msgs.msg import Float32
from std_msgs.msg import String
import subprocess
import re


#format 2024/08/18 21:58:35.907, 4.69
def get_power(output):
    numbers = re.findall(r'\d+',output)
    #print(numbers)
    p = numbers[-2:]
    #print(p)
    power = float(p[0]) + float(p[1]) / 1000.0
    #print(power)
    return power

def main():
    rclpy.init()
    node = rclpy.create_node('nvidia_publisher')
    #interval time
    node.declare_parameter('interval', 1000)
    interval = node.get_parameter('interval').value
    #topic name
    node.declare_parameter('ecu_name', "no_name")
    ecu_name = node.get_parameter('ecu_name').value
    topic_name = '/ecu/'+ecu_name+"/gpu"
    #print("topic_name ", topic_name)

    command = ["nvidia-smi", "--query-gpu=timestamp,power.draw",
               "--format=csv,noheader,nounits", "-lms", str(interval)]
    #node.get_logger().info(f'interval: {interval}')
    process = subprocess.Popen(command, stdout = subprocess.PIPE, stderr=subprocess.PIPE)

    # Create a publisher to publish the output
    publisher = node.create_publisher(Float32, topic_name, 10)
    while rclpy.ok():
        output = str(process.stdout.readline().strip())
        #node.get_logger().info(f'get: {output}')
        power = get_power(output)
        msg = Float32(data=power)
        node.get_logger().info(f'Publishing: {power}')
        publisher.publish(msg)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()


