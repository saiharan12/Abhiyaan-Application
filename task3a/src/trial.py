#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

pos2 = Pose()
pos1 = Pose()

def pos2dec(p2):
	pos2.x = p2.x
	pos2.y = p2.y
	rate.sleep()

def move_turtle(p1):

	pos1.x = p1.x
	pos1.y = p1.y


	dist = math.sqrt((p1.x-p2.x)**2 + (p1.y - p2.y)**2)

	force = 1.0/float(dist**2)

	vel1=Twist()
	vel2=Twist()

	vel1.linear.x = 1
	vel1.linear.y = 0
	vel1.linear.z = 0

	vel1.angular.x = 0
	vel1.angular.y = 0
	vel1.angular.z = 2
	pub1.publish(vel1)

	vel2.linear.x = 1
	vel2.linear.y = 0
	vel2.linear.z = 0

	vel2.angular.x = 0
	vel2.angular.y = 0
	vel2.angular.z = 2
	pub2.publish(vel2)
	rate.sleep()

rospy.init_node("turtlemove")
pub1 = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
sub1 = rospy.Subscriber('turtle1/pose',Pose,move_turtle)
pub2 = rospy.Publisher('/turtle2/cmd_vel',Twist,queue_size=10)
sub2 = rospy.Subscriber('turtle2/pose',Pose,pos2dec)
rate = rospy.Rate(10)
