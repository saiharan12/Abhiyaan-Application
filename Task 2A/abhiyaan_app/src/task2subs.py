#!/usr/bin/env python3
import rospy 
from std_msgs.msg import String
def callback(msg): 
	print (msg.data)
rospy.init_node('subs') 
sub1 = rospy.Subscriber('team_abhiyaan', String, callback)
sub2 = rospy.Subscriber('naayihba_maet', String, callback)
rospy.spin()