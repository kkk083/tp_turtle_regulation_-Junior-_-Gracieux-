import math
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

class SetWayPoint(Node):
    def __init__(self):
        super().__init__('set_way_point_node')
        self.way_point = (7.0, 7.0)
        self.current_pose = None
        self.Kp = 3.0  # Constante proportionnelle

        self.create_subscription(Pose, '/turtle1/pose', self.callback_pose, 10)
        self.cmd_vel_publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

    def callback_pose(self, msg: Pose):
        self.current_pose = (msg.x, msg.y)
        theta_robot = msg.theta

        # Calcul de l'angle désiré vers le way point
        theta_desire = self.calculate_angle(self.current_pose, self.way_point)

        # Calcul de l'erreur (angle entre la direction du robot et du waypoint)
        e = math.atan(math.tan((theta_desire - theta_robot) / 2.0))

        # Calcul de la commande en orientation (vitesse angulaire)
        u = self.Kp * e

        # Création du message Twist
        twist = Twist()
        twist.linear.x = 0.0
        twist.angular.z = u
        self.cmd_vel_publisher.publish(twist)

        # Affichage debug
        self.get_logger().info(f'[Pose] x={msg.x:.2f}, y={msg.y:.2f}, θ={theta_robot:.2f}')
        self.get_logger().info(f'[Commande] θ_desire={theta_desire:.2f}, erreur={e:.2f}, u={u:.2f}')

    def calculate_angle(self, current_position, way_point):
        dx = way_point[0] - current_position[0]
        dy = way_point[1] - current_position[1]
        return math.atan2(dy, dx)

def main(args=None):
    rclpy.init(args=args)
    node = SetWayPoint()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
