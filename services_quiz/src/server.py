#! /usr/bin/python3
import rospy
from test_services.srv import srvmess, srvmessResponse
from geometry_msgs.msg import Twist

def my_callback(request):
    print("My_callback has been called")
    dir = 0
    if request.directie =="dreapta" :
        dir = 1
    else:
        dir = -1
    start_time = rospy.get_time()
    turn = Twist()
    Duration = request.durata
    while start_time + Duration > rospy.get_time():
        turn.linear.x = 0.1
        turn.angular.y = 0.7* dir
        pub.publish(turn)

    turn.linear.x = 0.0
    turn.angular.y = 0.0
    pub.publish(turn)

    response = ms1Response()
    response.succes = True
    return response
    
rospy.init_node('service_server')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

my_service = rospy.Service('/move_linear_y', srvmess , my_callback)
rospy.spin()


#linear
#y
#server si client #serviciul primeste un string care specifica poz sau neg
#si o durata
#se va misca timp de ac durata in dir resp
#returneaza bool
