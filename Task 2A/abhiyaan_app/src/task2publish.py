#!/usr/bin/env python3
import rospy 
from std_msgs.msg import String
rospy.init_node('pub') 
pub = rospy.Publisher('team_abhiyaan', String) 
rate = rospy.Rate(2)
while not rospy.is_shutdown(): 
	pub.publish("Team Abhiyaan rocks:") 
	rate.sleep()