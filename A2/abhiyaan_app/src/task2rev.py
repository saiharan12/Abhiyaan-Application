#!/usr/bin/env python3 
import rospy #imports the library
from std_msgs.msg import String #imports String message type
rospy.init_node('reverser') #initialises node
def callback(msg): #function is called when subscriber receives a message, and the argument is the subscribed message
	rmsg = String()
	tem = msg.data #gets the string data from the imcoming message
	rmsg = tem[::-1] #reverses the string
	pub.publish(rmsg) #publishes the reversed string
sub = rospy.Subscriber("team_abhiyaan", String, callback) #subscribes to the same topic publisher is publishing to 
pub = rospy.Publisher("naayihba_maet", String) #Publishes to the reversal topic 'naayihba_maet'
rospy.spin() #Keeps the code running
