import math
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool

class SetWayPoint(Node):
    def __init__(self):
        super().__init__('set_way_point_node')
        self.way_point = (7.0, 7.0)
        self.current_pose = None
        self.Kp = 3.0    # Gain angulaire
        self.Kpl = 1.0   # Gain linéaire
        self.distance_tolerance = 0.1  # Seuil d'arrêt

        self.create_subscription(Pose, '/turtle1/pose', self.callback_pose, 10)
        self.cmd_vel_publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.is_moving_publisher = self.create_publisher(Bool, 'is_moving', 10)

    def callback_pose(self, msg: Pose):
        self.current_pose = (msg.x, msg.y)
        theta_robot = msg.theta

        # Calcul de l'angle désiré vers le waypoint
        theta_desire = self.calculate_angle(self.current_pose, self.way_point)

        # Erreur angulaire
        e = math.atan(math.tan((theta_desire - theta_robot) / 2.0))
        u = self.Kp * e

        # Erreur linéaire
        el = math.sqrt((self.way_point[0] - msg.x) ** 2 + (self.way_point[1] - msg.y) ** 2)
        v = self.Kpl * el

        twist = Twist()
        is_moving = Bool()

        if el > self.distance_tolerance:
            twist.linear.x = v
            twist.angular.z = u
            is_moving.data = True
            self.get_logger().info(f'[Commande ACTIVE] el={el:.2f} > tol={self.distance_tolerance}')
        else:
            twist.linear.x = 0.0
            twist.angular.z = 0.0
            is_moving.data = False
            self.get_logger().info(f'[Commande STOP] el={el:.2f} ≤ tol={self.distance_tolerance}')

        # Publication des commandes
        self.cmd_vel_publisher.publish(twist)
        self.is_moving_publisher.publish(is_moving)

        # Logs
        self.get_logger().info(f'[Pose] x={msg.x:.2f}, y={msg.y:.2f}, θ={theta_robot:.2f}')
        self.get_logger().info(f'[Commande] θ_desire={theta_desire:.2f}, erreur_ang={e:.2f}, u={u:.2f}, v={v:.2f}')
        self.get_logger().info(f'[is_moving] {is_moving.data}')

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
