
import rclpy
from std_msgs.msg import IntMultiArray
import subprocess

command = ["sudo","tegrastats", "--interval", "1000" "--verbose"]
#command = ["sudo","/home/autoware/tegra/power_tegra/tegrastats", "--interval", "1000" "--verbose"]

process = subprocess.Popen(command, stdout = subprocess.PIPE, stderr=subprocess.PIPE)

def main():
    rclpy.init()
    node = rclpy.create_node('command_executor')

    # Create a publisher to publish the output
    publisher = node.create_publisher(String, '/powers', 10)
    while rclpy.ok():
        result = process.stdout.readline()
        result = result.strip().split(' ')
        #print(result)
        CPU = 0
        GPU = 0
        for i in range(len(result)):
            if result[i] == 'CPU':
                CPU = result[i+1]
            if result[i] == 'GPU':
                GPU = result[i+1]
        CPU = int(CPU)
        GPU = int(GPU)
        node.get_logger().info(f'Publishing: {result}')
        publisher.publish(result) 


    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()


