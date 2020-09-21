import cv2
import os
def capture():
    cam = cv2.VideoCapture(0) #uses the webcam
    cam.set(3, 640) #set video width
    cam.set(4, 480) #set video height
    face_detector = cv2.CascadeClassifier('face.xml') #uses the data from the xml file
    #give the face an id
    face_id = "1"
    print("Starting face capture.")
    #setting the count for number of images
    count = 0
    while(True):
        ret, img = cam.read() #reads the data from the camera
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #changes it to greyscale
        faces = face_detector.detectMultiScale(gray, 1.3, 5) #find the face
        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2) #shows a rectangle around the face
            count += 1
            #save the captured image into the dataset folder as a jpg
            cv2.imwrite("dataset/User." + str(face_id) + '.' +  
                        str(count) + ".jpg", gray[y:y+h,x:x+w])
            cv2.imshow('image', img)
        k = cv2.waitKey(100) & 0xff #press 'ESC' to force exit
        if k == 27:
            break
        elif count >= 30: #take 30 face sample and stop the video
            break
    #stop the webcam and close the window
    print("Exiting the capturing stage")
    cam.release()
    cv2.destroyAllWindows()