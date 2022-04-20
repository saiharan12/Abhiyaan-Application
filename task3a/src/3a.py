#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

pos1 = Pose()
pos2 = Pose()
omega = 0
def callback1(p1):
	global pos1
	pos1.x = p1.x
	pos1.y = p1.y
	pos1.theta = p1.theta


def callback2(p2):
	global pos1
	global pos2
	global pub1
	global pub2
	global omega
	pos2.x = p2.x
	pos2.y = p2.y

	dist = math.sqrt((pos1.x-pos2.x)**2 + (pos1.y - pos2.y)**2)

	# force = 1.0/float(dist**2)
	# acc = force
	if pos1.x != pos2.x:
		theta=math.atan((pos1.y - pos2.y)/(pos1.x - pos2.x))
	else:
		if pos1.y>pos2.y:
			theta = (math.pi)/2.0
		else:
			theta = (math.pi)/-2.0

	#if theta>0:

	#totaltheta
	sintheta = math.fabs(math.sin(-theta+pos1.theta))

	r=dist/2.0

	v0 = 1.7
	r0 = 1.5
	m = 1.0
	G = 1.0
	E0 = m*v0*v0 - (G*m*m)/(2*r0)
	L0 = 2*m*r0*v0
	
	vel = math.sqrt((E0/m) + (G*m/(2*r)))
	vel1=Twist()
	vel2=Twist()

	# T=41.1417
	# omega = ((math.pi)*(12)*math.sqrt(35))/(T*r*r)

	vel1.linear.x = vel
	vel1.linear.y = 0
	vel1.linear.z = 0

	vel1.angular.x = 0
	vel1.angular.y = 0
	vel1.angular.z = -1*omega
	pub1.publish(vel1)

	vel2.linear.x = vel
	vel2.linear.y = 0
	vel2.linear.z = 0

	vel2.angular.x = 0
	vel2.angular.y = 0
	vel2.angular.z = -1*omega
	pub2.publish(vel2)
	omega = L0/(2*m*r*vel*sintheta)
def a3():
	global pub1
	global pub2
	rospy.init_node('task3')
	pub1 = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
	pub2 = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size=10)
	rospy.Subscriber('/turtle1/pose',Pose, callback1)
	rospy.Subscriber('/turtle2/pose',Pose, callback2)
	rospy.spin()

if __name__ == '__main__':
    try:
        a3()
    except rospy.ROSInterruptException:
        pass