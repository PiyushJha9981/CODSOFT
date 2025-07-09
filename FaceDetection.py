import cv2

# Use raw string literal to avoid issues with backslashes in file paths
harcascade = r"haarcascade_frontalface_default.xml"
facecascade = cv2.CascadeClassifier(harcascade)

cap=cv2.VideoCapture(0)

cap.set(3,640)  #width
cap.set(4,480)  #height

while True:
    sucess,img = cap.read()
    img = cv2.flip(img, 1)

    # No need to redefine facecascade inside the loop
    img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    face=facecascade.detectMultiScale(img_gray, 1.1, 5, minSize=(30, 30), flags= cv2.CASCADE_SCALE_IMAGE)

    for (x,y,w,h) in face:
        cv2.rectangle(img, (x,y), (x+w,y+h),(0,255,0),2)
    
    cv2.imshow("Face Detection Tool",img)    

    # Break if 'p' is pressed or window is closed
    if cv2.waitKey(1) & 0xFF == ord('p'):
        break
    if cv2.getWindowProperty('Face Detection Tool', cv2.WND_PROP_VISIBLE) < 1:
        break

# Release VideoCapture object outside of the loop
cap.release()
cv2.destroyAllWindows()