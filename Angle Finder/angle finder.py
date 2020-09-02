import cv2
import math

path= 'angle.jpg'
img = cv2.imread(path)
pointsList = []  #Creating a points list in which we can store the xy points


#Defining a function for the mouse click

def mousePoints(events,x,y,flags,params):
    if events == cv2.EVENT_LBUTTONDOWN: #if we click the left mouse
        size = len(pointsList) #drawing line
        if size != 0 and size % 3 != 0:  # If the points are divisible by 3 but not equal to 0, draw the line
            cv2.line(img,tuple(pointsList[round((size-1)/3)*3]),(x,y),(0,50,255),2)
        cv2.circle(img,(x,y),5,(0,0,255),cv2.FILLED) #Circle the point we click
        pointsList.append([x,y])
        #print(x,y)
        #print(pointsList)


def gradient(pt1,pt2):
    return(pt2[1]-pt1[1])/(pt2[0]-pt1[0]) # Equation for gradient

def getAngle(pointsList):
    pt1, pt2, pt3 = pointsList[-3:] # -3 becoz only after the 3 click, the result will be displayed
    #print(pt1, pt2,pt3)
    m1=gradient(pt1,pt2)
    m2=gradient(pt1,pt3)
    angR = math.atan(m2-m1)/(1+(m2*m1))  # Value in Radians
    angD = round(math.degrees(angR))     # Value in degree
    print(angD)
    cv2.putText(img,str(angD),(pt1[0]-40,pt1[1]-20), cv2.FONT_HERSHEY_COMPLEX,1.5,(0,0,255),2)  # Displaying the angle



while True:
    if len(pointsList) % 3 == 0 and len(pointsList) !=0:   # %3 coz three points consicutes an angle, so it must be divisible by 3
        getAngle(pointsList)
    cv2.imshow('Image', img)
    cv2.setMouseCallback('Image',mousePoints) # will display the x and y points in the image

    # setting a button to clear the selected point

    if cv2.waitKey(1) & 0xFF== ord('q'):
        pointsList= []
        img = cv2.imread(path)
