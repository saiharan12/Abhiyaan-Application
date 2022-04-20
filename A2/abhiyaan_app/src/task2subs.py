#!/usr/bin/env python3
import rospy #imports the library 
from std_msgs.msg import String #imports String message datatype
def callback(msg): #called when subscriber receives a message
	print (msg.data) #prints the data in the message received
rospy.init_node('subs') #initialises node
sub1 = rospy.Subscriber('team_abhiyaan', String, callback) # Subscibes to the topic normal string is publishing to 'team_abhiyaan'
sub2 = rospy.Subscriber('naayihba_maet', String, callback) # Also subscribes to the reversed string topic 'naayihba_maet'
rospy.spin() #keeps the code running
