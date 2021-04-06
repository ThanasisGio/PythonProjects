import cv2,time,pandas
from datetime import datetime
status_list=[None,None]
times=[]
#create dataframestructure for us
df=pandas.DataFrame(columns=["Start","End"])
#create frist frame variable,assign none value
#NOne value is a value of nothing so python can recognize

first_frame=None

#method tha triggers video capture
#pass zero to acces laptop camera
video=cv2.VideoCapture(0)

while True:
    
#create frame object to see video
# check is boolean , frame is array
    check,frame = video.read()
    status=0
#we will loop through frame

    #print(check)
    #print(frame)
    #convert frame into gray image

    gray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)

    if first_frame is None:
        first_frame=gray
        continue
    delta_frame=cv2.absdiff(first_frame,gray)

    #make threshold
    thresh_frame=cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1]
    #now i want to smoth out shadows of threshold frame delete them
    thresh_frame=cv2.dilate(thresh_frame,None,iterations=2)
    #find contures
    
    (cnts,_)  = cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 9500:
            continue
        status=1

#we create rectangle
        (x,y,w,h)=cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(x+w,y+w),(0,255,0),3)

    status_list.append(status)

    status_list=status_list[-2:]
    if status_list[-1] ==1 and status_list[-2]==0: 

        times.append(datetime.now()) 
    if status_list[-1] ==0 and status_list[-2]==1: 

        times.append(datetime.now()) 




    cv2.imshow("Gray Frame ",gray)
    cv2.imshow("Delta Frame ",delta_frame)
    cv2.imshow("Threshold Frame",thresh_frame)
    cv2.imshow("Color Frame",frame)

 
    #continue is so the conditional can go back to the beginning
#after we catch first frame
    
    #cv2.imshow("Capturing",gray)
    key=cv2.waitKey(1)
    #print(gray)
    #print(delta_frame)
# if i press q the code will stop
    if key==ord('q'):
        if status==1:
            times.append(datetime.now())

        break
print(status_list)
print(times)

for i in range(0,len(times),2):
    df=df.append({"Start":times[i],"End":times[i+1]},
    ignore_index=True)

    df.to_csv("Times.csv")



#then acces the camera with release method
video.release()
cv2.destroyAllWindows
