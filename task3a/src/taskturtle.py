import pylab
import math
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import time
from std_srvs.srv import Empty

rospy.init_node('two_body_turtle')


pos1path = "/turtle1/pose"
pos2path = "/turtle2/pose"

pos1 = rospy.Subs










G = 6.67e-11
Ma = 2.0e30
Mb = 2.0e30
AU = 1.5e11
daysec = 24.0*60*60

gravconst = G*Ma*Mb

xa = 1*AU
ya = 0

xb = -1*AU
yb = 0

xva = 0.0
yva = 10000.0

xvb = 0
yvb = -10000.0

t=0.0
dt = 0.01*daysec

xalist =[]
yalist =[]

xblist =[]
yblist =[]

while t<1000.0*daysec:
	#Force computation
	rx = xb-xa
	ry = yb-ya

	modr3 = (rx**2 + ry**2)**1.5

	fx = -1*gravconst*rx/modr3
	fy = -1*gravconst*ry/modr3

	#Updation
	xvb += fx*dt/Mb
	yvb += fy*dt/Mb

	xb += xvb*dt
	yb += yvb*dt

	xva += -1*fx*dt/Ma
	yva += -1*fy*dt/Ma

	xa += xva*dt
	ya += yva*dt

	t+=dt

	xalist.append((xa/0.25e11)+6.8)
	yalist.append((ya/0.25e11)+3.8)

	xblist.append((xb/0.25e11)+6.8)
	yblist.append((yb/0.25e11)+3.8)

pylab.plot(xalist,yalist,"-g")
pylab.plot(xblist,yblist,"-k")
pylab.axis("equal")
pylab.show()