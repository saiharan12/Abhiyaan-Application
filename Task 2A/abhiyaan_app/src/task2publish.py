#!/usr/bin/env python3
import rospy #import the library
from std_msgs.msg import String #import String message datatype
rospy.init_node('pub') #initialise node
pub = rospy.Publisher('team_abhiyaan', String) #declare publisher
rate = rospy.Rate(2) #set message rate
while not rospy.is_shutdown(): #runs only until it's not stopped, or roscore is closed
	pub.publish("Team Abhiyaan rocks:") #publish the message
	rate.sleep() #delay
