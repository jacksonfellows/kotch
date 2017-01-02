from turtle import *
from math import sqrt, atan, degrees

startx = -600
starty = -200

colors = ['red','orange','yellow4','green','blue','purple'] # This list will be looped through to display each iteration with different colors of the rainbow

def tri(p1,p2):
	x1 = p1[0]; y1 = p1[1]; x2 = p2[0]; y2 = p2[1]
	d = sqrt(((x2-x1)**2)+((y2-y1)**2)) # Distance formula
	up()
	setpos(x1,y1)
	down()
	angle = 60 + degrees(atan((y2-y1)/(x2-x1))) # Find angle from rise/run and add 60 for triangle
	seth(angle)
	if x2 < x1: bk(d) # Backwards line
	else: fd(d)
	top = pos()
	angle -= 120
	seth(angle)
	if x2 < x1: bk(d) # Backwards line
	else: fd(d)

	return top # Returns the top of the triangle so it can be added as a new point

def third(p1,p2):
	up()
	x1 = p1[0]; y1 = p1[1]; x2 = p2[0]; y2 = p2[1]
	d = sqrt(((x2-x1)**2)+((y2-y1)**2)) # Distance formula
	setpos(x1,y1)
	angle = degrees(atan((y2-y1)/(x2-x1))) # Find angle from rise/run
	seth(angle)
	if x2 < x1: bk(d/3) # Backwards line
	else: fd(d/3)
	#pencolor("blue")
	#down()
	first = pos()
	if x2 < x1: bk(d/3) # Backwards line
	else: fd(d/3)
	second = pos()
	down()
	#pencolor("red")

	return [first,second] # Returns the first and second third points on the line in between p1 and p2

def kotch(iter):
	fd(1200)
	display(0)
	points = [(startx, starty),(startx+1200,starty)] # Sets up list of points that will be looped through and added to to draw the fractal
	newpoints = list(points)

	for i in range(0,iter):
		if (iter<6):
			speed(iter+5)
		color(colors[i%6])
		points = list(newpoints)
		buf = 0 # This buffer deals with the fact that we are adding points to newpoints as we go
		for j in range(0,len(points)-1):
			middle = third(points[j],points[j+1])
			top = tri(middle[0],middle[1])
			newpoints.insert(j+1+buf,middle[0])
			newpoints.insert(j+2+buf,top)
			newpoints.insert(j+3+buf,middle[1])
			buf += 3
		display(i+1)

def display(i): # Display the iteration and the lenght of the line
	ht()
	up()
	setpos((startx-100,(starty*-1)+100-(i-1)*20))
	length = (4/3)**i
	write('Iteration %i: the line is ' % i, True, align = 'left', font=('Verdana', 14, 'normal'))
	write('%.2f long' % length, True, align = 'left', font=('Verdana', 14, 'normal'))
	down()
	st()

def main(): # Main loop
	window = Screen()
	window.screensize()
	window.setup(width = 1.0, height = 1.0) # Make the window fullscreen
	up()
	setpos(startx,starty)
	down()
	title('The Kotch Fractal: An Infinite Length in a Finite Space')
	kotch(10) # Run the function to display a kotch fractal, with 10 iterations

if __name__ == '__main__':
	main()
	mainloop()