
import rclpy
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import String
import subprocess

def main():
    rclpy.init()
    node = rclpy.create_node('power_publisher')
    #interval time
    node.declare_parameter('interval', 1001)
    interval = node.get_parameter('interval').value
    #topic name
    node.declare_parameter('ecu_name', "no_name")
    ecu_name = node.get_parameter('ecu_name').value
    topic_name = '/ecu/'+ecu_name.replace('-','')
    #print("topic_name ", topic_name)

    command = ["sudo", "tegrastats", "--interval", str(interval), "--verbose"]
    #print(command)
    process = subprocess.Popen(command, stdout = subprocess.PIPE, stderr=subprocess.PIPE)

    # Create a publisher to publish the output
    publisher = node.create_publisher(Float32MultiArray, topic_name, 10)
    while rclpy.ok():
        result0 = str(process.stdout.readline().strip())
        #node.get_logger().info(f'Publishing: {result0}')

        #print(result)
        result = result0.split(' ')
        #print(result)
        CPU = 0
        GPU = 0
        for i in range(len(result)):
            #print(result[i], result[i+1])
            if result[i] == 'CPU':
                CPU = result[i+1].split('/')[0]
            elif result[i] == 'GPU':
                GPU = result[i+1].split('/')[0]
        CPU = float(CPU) / 1000.0
        GPU = float(GPU) / 1000.0
        msg = Float32MultiArray(data=[CPU,GPU])
        node.get_logger().info(f'Publishing: {CPU} {GPU}')
        publisher.publish(msg)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()


