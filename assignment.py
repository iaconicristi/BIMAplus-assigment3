#BIMAplus - Assignment 3.1
#Cristian Iaconi

#imports
import numpy
#user input: number of points
numberOfPoints = int(input("Enter the number of polygon points: "))
while numberOfPoints < 3:
    print("To make a polygon you need at least 3 points to enclose an area!")
    numberOfPoints = int(input("Try again with more than 3 points: "))
    if numberOfPoints > 2:
        break

print(str(numberOfPoints) + " points\n")

#define coord array
coord = numpy.zeros((numberOfPoints,2)) 

#user input: coord of points
for i in range(numberOfPoints):
    coord[i] = [int(input("Input x coord of point " + str(i+1)+": ")),int(input("Input y coord of point " + str(i+1)+": "))]
    print("Point " + str(i+1) + " coordinates are " + str(coord[i]) + "\n")

print("Summary of points:\n")
print("Point\tx\ty")
print("-"*20)
for i in range(numberOfPoints):
    print(i+1,"\t",f"{coord[i][0]:.1f}","\t", f"{coord[i][1]:.1f}")


#Initial values
area = 0
#print(area)
xStaticMoment = 0
#print(xStaticMoment)
yStaticMoment = 0
#print(yStaticMoment)
xInertia = 0
#print(xInteria)
yInertia = 0
#print(yIntertia)
xyInertia = 0
#print(xyIntertia)

#summing up the rest of the points: 
for i in range(numberOfPoints):
    xI = coord[i-1][0]
    yI = coord[i-1][1]
    xI1 = coord[i][0]
    yI1 = coord[i][1]

    area = area + (xI1 + xI)*(yI1-yI)
    #print("area is: " + str(area))
    xStaticMoment = xStaticMoment + (xI1 - xI)*(yI1**2 + yI*yI1 + yI**2)
    #print("xstatic moment is: " + str(xStaticMoment))
    yStaticMoment = yStaticMoment + (yI1 - yI)*(xI1**2 + xI*xI1 + xI**2)
    #print("y static moment is: " + str(yStaticMoment))
    xInertia = xInertia + (xI1 - xI)*(yI1**3 + (yI1**2)*yI + yI1*(yI**2) + yI**3)
    #print("xInertia is " + str(xInteria))
    yInertia = yInertia + (yI1 - yI)*(xI1**3 + (xI1**2)*xI + xI1*(xI**2) + xI**3)
    #print("yInertia is " + str(yInteria))
    xyInertia = xyInertia + (yI1 - yI)*((yI1*(3*xI1**2 + 2*xI1*xI + xI**2)) + yI*(3*xI**2 + 2*xI1*xI + xI1**2))
    #print("xyInertia is: " + str(xyInertia))

#print geometric characteristics:
print()
print("Geometric Characteristics: ")
area = (1/2)*area
print("Ax: "f"{area: .2f}")
xStaticMoment = (-1/6)*xStaticMoment
print("Sx: "f"{xStaticMoment:.2f}")
yStaticMoment = (1/6)*yStaticMoment
print("Sy: "f"{yStaticMoment:.2f}")
xInertia = (-1/12)*xInertia
print("Ix: "f"{xInertia:.2f}")
yInertia = (1/12)*yInertia
print("Iy: "f"{yInertia:.2f}")
xyInertia = (-1/24)*xyInertia
print("Ixy: "f"{xyInertia:.2f}")
xCentroid = yStaticMoment/area
print("xt: "f"{xCentroid:.2f}") 
yCentroid = xStaticMoment/area
print("yt: "f"{yCentroid:.2f}")
xInertiaT = xInertia - (yCentroid**2)*area
print("Ixt: "f"{xInertiaT:.2f}")
yInertiaT = yInertia - (xCentroid**2)*area
print("Iyt: "f"{yInertiaT:.2f}")
xyInertiaT = xyInertia + xCentroid*yCentroid*area
print("Ixyt: "f"{xyInertiaT:.2f}\n")

print("¯\_(°_°)_/¯")
print("Cristian Iaconi - BIMAplus - Assignment 3.1")









