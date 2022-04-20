The code attached here is imcomplete, because I spent wayy too long on TurtleSim (TvT). Anyways, I will mention the logic here:<br>
1. Use the cv2.drawContour to draw a line while iterating i from 0 to 359, and using i as the angle, from an arbitary point X.
2. Then use the numpy.logical_and(contours, line_mask) function to find the interection of the line and the contour.
3. Then use distance formula to find the distance from X.
4. Append to a dictionary with key:value as angle:distance
5. Plot it using matplotlib pyplot.