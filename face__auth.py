import cv2
import numpy as np
import os 
def authenticate():
    recognizer = cv2.face.LBPHFaceRecognizer_create() #creates the recogniser
    recognizer.read('trainer/trainer.yml') #reads the yml file
    cascadePath = "face.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath) #uses the face.xml file for the faces
    font = cv2.FONT_HERSHEY_SIMPLEX #font
    #iniciate id counter
    id = 0
    #names for the ids
    names = ['None', 'User'] 
    #initialize and start video capture
    cam = cv2.VideoCapture(0)
    cam.set(3, 640) #set video widht
    cam.set(4, 480) #set video height
    #define min window size to be recognized as a face
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)
    while True:
        ret, img = cam.read() #reads th ewebcam
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #to greyscale
        
        #detect the faces
        faces = faceCascade.detectMultiScale( 
            gray,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
        )
        for(x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
            id, confidence = recognizer.predict(gray[y:y+h,x:x+w]) #see how much like the faces that it was trained to look for the face is like
            
            #if confidence is less than 100 then it shows the confidence and the name of the user and creates the authenticated file to show that it has been authenticated
            if (confidence < 100):
                id = names[id]
                confidence = "  {0}%".format(round(100 - confidence))
                f = open('authenticated.txt', 'w')
                f.write("True")
                f.close()
            else:
                id = "unknown"
                confidence = "  {0}%".format(round(100 - confidence)) #prints unknown if the face is not the trained face
            
            #show captions with the id and confidence and instruction to press 'ESC'
            cv2.putText(
                        img, 
                        str(id), 
                        (x+5,y-5), 
                        font, 
                        1, 
                        (255,255,255), 
                        2
                    )
            cv2.putText(
                        img, 
                        str(confidence), 
                        (x+5,y+h-5), 
                        font, 
                        1, 
                        (255,255,0), 
                        1
                    )
            cv2.putText(img, "Press ESC to continue.", (x-100,y+h+30), font, 1, (255, 255, 0), 2)  
        
        cv2.imshow('camera',img) 
        k = cv2.waitKey(10) & 0xff #press 'ESC' for exiting video
        if k == 27:
            break
    #release webcam
        
    print("Exiting Program")
    cam.release()
    cv2.destroyAllWindows()