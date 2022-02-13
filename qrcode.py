#Assignment 10

#Contact Tracing App
	#- Create a python program that will read QRCode using your webcam
	#- You may use any online QRCode generator to create QRCode
	#- All personal data are in QRCode 
	#- You may decide which personal data to include
	#- All data read from QRCode should be stored in a text file including the date and time it was read

#Note: 
	#- Search how to generate QRCode
	#- Search how to read QRCode using webcam
	#- Search how to create and write to text file
	#- Your source code should be in github before Feb 19
	#- Create a demo of your program (1-2 min) and send it directly to my messenger.

# Import
import cv2
from pyzbar.pyzbar import decode
from datetime import datetime
import time

# Set Camera
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
camera = True

# Read QR Code
while camera == True: # habang walang ini-iscan, mag rrun/display yung camera.
    success, frame = cap.read()
    for code in decode(frame):
        qrdata = code.data.decode("utf-8")
        time.sleep(3) # Indicator when scanning is complete.
        camera = False
    cv2.imshow("QR Scanner", frame)
    cv2.waitKey(1)

# Store QR Data in Information
information = []
for line in qrdata.split("\n"):
    information.append(line)


# Set Information
name = information[0]
birthday = information[1]
address = information[2]
contactNumber = information[3]
email = information[4]

# Get Date and Time
now = datetime.now()
time = now.strftime("%H:%M:%S")
date = now.date()

# Create Text File
textFile = open('Contact Tracing.txt', 'w')

# Write on Text File
textFile.write("Name: " + name + "\n")
textFile.write("Birthday: " + birthday + "\n")
textFile.write("Address: " + address + "\n")
textFile.write("Contact Number: " + contactNumber + "\n")
textFile.write("Email: " + email + "\n")
textFile.write("Time: " + time + "\n")
textFile.write("Date: " + str(date))

print("Contact Tracing Done!")