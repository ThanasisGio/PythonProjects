import cv2,time


#method tha triggers video capture
#pass zero to acces laptop camera
video=cv2.VideoCapture(0)
#want to see how many frames arr generated
a=0
while True:
    a=a+1
#create frame object to see video
# check is boolean , frame is array
    check,frame = video.read()
#we will loop through frame

    print(check)
    print(frame)
    #convert frame into gray image

    gray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #time.sleep(3)
    cv2.imshow("Capturing",gray)
    key=cv2.waitKey(1)
# if i press q the code will stop
    if key==ord('q'):
        break
print(a)

#then acces the camera with release method
video.release()
cv2.destroyAllWindows
