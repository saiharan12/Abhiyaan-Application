#!/usr/bin/env python3
import rospy 
from std_msgs.msg import String
rospy.init_node('reverser')
def callback(msg): 
	rmsg = String()
	tem = msg.data
	rmsg = tem[::-1]
	# rmsg = ""
	# for t in msg:
	# 	rmsg=t+rmsg
	pub.publish(rmsg)
sub = rospy.Subscriber("team_abhiyaan", String, callback)
pub = rospy.Publisher("naayihba_maet", String)
rospy.spin()