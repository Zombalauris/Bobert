#! /usr/bin/python3
import rospy
from test_services.srv import srvmess, srvmessRequest 

rospy.init_node('service_client')
rospy.wait_for_service('/move_linear_y')
move_linear = rospy.ServiceProxy('/move_linear_y', srvmess)
move_linear_obj = srvmessRequest()
move_linear_obj.duration = 10
move_linear_obj.direction = "poz"

result = move_linear(move_linear_obj)
print(result)
