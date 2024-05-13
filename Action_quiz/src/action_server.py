#!/usr/bin/env python

import rospy
import actionlib
from your_package_name.msg import Action2Action, Action2Feedback, Action2Result
from geometry_msgs.msg import PoseStamped

class Action2Server:
    def __init__(self):
        self.server = actionlib.SimpleActionServer('action2', Action2Action, self.execute, False)
        self.server.start()
        self.pose_subscriber = rospy.Subscriber('/pose_topic', PoseStamped, self.pose_callback)
        self.current_orientation_y = 0.0

    def pose_callback(self, msg):
        self.current_orientation_y = msg.pose.position.y

    def execute(self, goal):
        rate = rospy.Rate(1)
        orientations = []  
        start_time = rospy.Time.now()

        while (rospy.Time.now() - start_time).to_sec() < goal.duration:
            if self.server.is_preempt_requested():
                self.server.set_preempted()
                break
            feedback = Action2Feedback()
            feedback.orientation_y = self.current_orientation_y
            self.server.publish_feedback(feedback)
            rate.sleep()

        result = Action2Result()
        self.server.set_succeeded(result)

if __name__ == '__main__':
    rospy.init_node('action2_server')
    server = Action2Server()
    rospy.spin()

