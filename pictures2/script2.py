import cv2
import glob
# * go through all of list
images=glob.glob("*.jpg")

for image in images:
    img=cv2.imread(image,0)
    re=cv2.resize(img,(100,100))
    cv2.imshow("Hey",re)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    # stores in re
    cv2.imwrite("resized_"+image,re)