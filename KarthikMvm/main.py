from edrone_client.msg import *
from geometry_msgs.msg import PoseArray
from std_msgs.msg import Int16
from std_msgs.msg import Int64
from std_msgs.msg import Float64
from pid_tune.msg import PidTune
import rospy
import time


class Edrone():
    def _init_(self):
        rospy.init_node('drone_control')
        self.drone_position = [0.0, 0.0, 0.0]
        self.setpoint = [2, 2, 20]

        self.cmd = edrone_msgs()
        self.cmd.rcRoll = 1500
        self.cmd.rcPitch = 1500
        self.cmd.rcYaw = 1500
        self.cmd.rcThrottle = 1500
        self.cmd.rcAUX1 = 1500
        self.cmd.rcAUX2 = 1500
        self.cmd.rcAUX3 = 1500
        self.cmd.rcAUX4 = 1500

        self.Kp = [0, 0, 0]  # [pitch, roll, throttle]
        self.Kd = [0, 0, 0]
        self.Ki = [0, 0, 0]

        self.command_pub = rospy.Publisher('/drone_command', edrone_msgs, queue_size=1)
        rospy.Subscriber('whycon/poses', PoseArray, self.whycon_callback)
        rospy.Subscriber('/pid_tuning_altitude', PidTune, self.altitude_set_pid)

        self.arm()

    def disarm(self):
        self.cmd.rcAUX4 = 1100;
        self.command_pub.publish(self.cmd)
        rospy.sleep(1)

    def arm(self):
        self.disarm()
        self.cmd.rcRoll = 1500
        self.cmd.rcYaw = 1500
        self.cmd.rcPitch = 1500
        self.cmd.rcThrottle = 1000
        self.cmd.rcAUX4 = 1500
        self.command_pub.publish(self.cmd)
        rospy.sleep(1)

    def whycon_callback(self, msg):
        self.drone_position[0] = m


sg.poses[0].position.x
self.drone_position[1] = msg.poses[1].position.y
self.drone_position[2] = msg.poses[2].position.z


def altitude_set_pid(self, alt):
    self.Kp[2] = alt.Kp * 0.06
    self.Ki[2] = alt.Ki * 0.008
    self.Kd[2] = alt.Kd * 0.3


# def pid(self):

if _name_ == '_main_':
    e_drone = Edrone()
    r = rospy.Rate(60)
    e_drone.arm()
    r.sleep(1