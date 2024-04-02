#! /usr/bin/env python

import rospy
import time
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def callback(msg):
   print (msg.ranges[0])
   if (msg.ranges[0]<0.5):
   	turn.linear.x = 0
   	turn.angular.z = 0
   	pub.publish(turn)
   	time.sleep(0.5)
   	turn.angular.z = 0.5
   	pub.publish(turn)
   	time.sleep(2)
   	turn.linear.x = 0.5
   	turn.angular.z = 0
   	pub.publish(turn)
   	turn.angular.z = -0.5
   	turn.linear.x = 0
   	pub.publish(turn)
   	time.sleep(1)
   	turn.linear.x = 0
   	turn.angular.z = 0
   	pub.publish(turn)
   turn.linear.x = 0.5
   pub.publish(turn)
   	

rospy.init_node('scan_publisher')
sub = rospy.Subscriber('/scan', LaserScan, callback)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 1)

rate = rospy.Rate(2)
turn = Twist()

rospy.spin()
