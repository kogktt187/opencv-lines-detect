import numpy as np
import cv2
from Tkinter import *
from PIL import Image, ImageTk
import imutils

class straightLines:  
    def __init__(self, x1, x2):  
        self.x1 = x1
        self.x2 = x2


def Hough():
	
	im = cv2.imread(E1.get())
	if(im==None):
		print "error"
	else:
	
		imHeight = imHeightVal.get()
		angleRange = angleRangeVal.get()
		Interval = IntervalVal.get()
		filter1 = filter1Val.get()
		filter2 = filter2Val.get()
		edge1 = edge1Val.get()
		edge2 = edge2Val.get()
		hough = houghVal.get()
	
	
		LinesInAngleRange = []
		FinalLines = [straightLines(0, 0)]
		screenCnt = []
		index = 1
	
		ratio = im.shape[0] / (imHeight +0.0)
		origHeight = im.shape[0]
		origWidth = im.shape[1]
		orig = im.copy()
		im = imutils.resize(im, height = imHeight)
	
	
		gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
		filter = cv2.bilateralFilter(gray,5,filter1,filter2)
		edges = cv2.Canny(filter,edge1,edge2,apertureSize = 5)
	
	
		lines = cv2.HoughLines(edges, 1, np.pi/180, hough)
	
	
	
		for rho,theta in lines[0]:
			angle = theta*180/np.pi
			if  angle>180-angleRange or angle<angleRange:
				a = np.cos(theta)
				b = np.sin(theta)
				tan = b/a
				x0 = a*rho
				y0 = b*rho
				x1 = int(rho/a)
				x2 = int(x1-imHeight*tan)
				LinesInAngleRange.append(straightLines(x1, x2))
		
		
		
		
		LinesInAngleRange.sort(key=lambda i: i.x1)
		FinalLines.append(LinesInAngleRange[0])
	
	
	
		for i in range(1, len(LinesInAngleRange), +1):
			
			
			if abs(LinesInAngleRange[i].x1-FinalLines[index].x1) > Interval and abs(LinesInAngleRange[i].x2-FinalLines[index].x2) > Interval:
                		
				FinalLines.append(LinesInAngleRange[i])
				index = index + 1	
				
		
		FinalLines.append(straightLines(origWidth, origWidth))
	


		for i in range(0, len(FinalLines)-1, +1):
		
			cnt = np.array([[int(FinalLines[i].x1*ratio), 0], 
							[int(FinalLines[i].x2*ratio), origHeight], 
							[int(FinalLines[i+1].x2*ratio), origHeight], 
							[int(FinalLines[i+1].x1*ratio), 0]])
						
						
						
			cnt1 = np.array([[FinalLines[i].x1, 0], 
							[FinalLines[i].x2, imHeight], 
							[FinalLines[i+1].x2, imHeight],
							[FinalLines[i+1].x1, 0]])

			cv2.drawContours(orig, [cnt], -1, (0, 255, 0), 5)
	
	
		orig = imutils.resize(orig, height = 700)
		cv2.imshow("111",orig)




# A root window for displaying objects
root = Tk()
imHeightVal = IntVar()
imHeightVal.set(300)
angleRangeVal = IntVar()
angleRangeVal.set(30)
IntervalVal = IntVar()
IntervalVal.set(20)
filter1Val = IntVar()
filter1Val.set(20)
filter2Val = IntVar()
filter2Val.set(20)
edge1Val = IntVar()
edge1Val.set(300)
edge2Val = IntVar()
edge2Val.set(500)
houghVal = IntVar()
houghVal.set(105)


frame = Frame(root)
frame.pack()

L1 = Label(frame, text="file name")
L1.pack( side = LEFT)
E1 = Entry(frame,font ="Helvetica 30")
E1.insert(10,"test.jpg")
E1.pack(side = RIGHT)

frame1 = Frame(root)
frame1.pack()
frame2 = Frame(root)
frame2.pack()
frame3 = Frame(root)
frame3.pack()
frame4 = Frame(root)
frame4.pack()
frame5 = Frame(root)
frame5.pack()
frame6 = Frame(root)
frame6.pack()
frame7 = Frame(root)
frame7.pack()
frame8 = Frame(root)
frame8.pack()


# Convert the Image object into a TkPhoto object


# Put it in the display window



name = Label(frame1, text = "imHeight")
name.pack(side = LEFT, padx = 10)


scale = Scale( frame1, 
			variable = imHeightVal, 
			orient = HORIZONTAL , 
			from_ = 200,
			to = 500,
			length = 300,
			resolution = 10,
			)
scale.pack() 


name1 = Label(frame2, text = "angleRange")
name1.pack(side = LEFT, padx = 10)


scale1 = Scale( frame2, 
			variable = angleRangeVal, 
			orient = HORIZONTAL , 
			from_ = 10,
			to = 40,
			length = 300
			)
scale1.pack() 

name2 = Label(frame3, text = "Interval")
name2.pack(side = LEFT, padx = 10)


scale2 = Scale( frame3, 
			variable = IntervalVal, 
			orient = HORIZONTAL , 
			from_ = 20,
			to = 30,
			length = 300,
			)
scale2.pack() 


name3 = Label(frame4, text = "filter1")
name3.pack(side = LEFT, padx = 10)


scale3 = Scale( frame4, 
			variable = filter1Val, 
			orient = HORIZONTAL , 
			from_ = 15,
			to = 100,
			length = 300,
			resolution = 5,
			)
scale3.pack() 


name4 = Label(frame5, text = "filter2")
name4.pack(side = LEFT, padx = 10)


scale4 = Scale( frame5, 
			variable = filter2Val, 
			orient = HORIZONTAL , 
			from_ = 15,
			to = 100,
			length = 300,
			resolution = 5,
			)
scale4.pack() 


name5 = Label(frame6, text = "edge1")
name5.pack(side = LEFT, padx = 10)


scale5 = Scale( frame6, 
			variable = edge1Val, 
			orient = HORIZONTAL , 
			from_ = 0,
			to = 500,
			length = 300,
			resolution = 25,
			)
scale5.pack() 

name6 = Label(frame7, text = "edge2")
name6.pack(side = LEFT, padx = 10)


scale6 = Scale( frame7, 
			variable = edge2Val, 
			orient = HORIZONTAL , 
			from_ = 0,
			to = 500,
			length = 300,
			resolution = 25,
			)
scale6.pack() 

name7 = Label(frame8, text = "hough")
name7.pack(side = LEFT, padx = 10)


scale7 = Scale( frame8, 
			variable = houghVal, 
			orient = HORIZONTAL , 
			from_ = 50,
			to = 200,
			length = 300,
			resolution = 5,
			)
scale7.pack() 

button = Button(root, text="Start Hough", command=Hough)
button.pack(anchor=CENTER)



Hough()

root.mainloop() # Start the GUI










