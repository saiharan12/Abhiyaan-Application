#!/bin/bash
rosservice call /kill turtle1
rosservice call /kill turtle2
rosservice call /clear
rosservice call /spawn 4 5 1.570796326 turtle1
rosservice call /spawn 7 5 4.712388980 turtle2