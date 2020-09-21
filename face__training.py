import cv2
import numpy as np
from PIL import Image
import os
def train():
    #path for face image database
    path = 'dataset'
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector = cv2.CascadeClassifier("face.xml") #xml file to recognise the faces
    # function to get the images and label data
    def getImagesAndLabels(path):
        imagePaths = [os.path.join(path,f) for f in os.listdir(path)] 
        faceSamples=[]
        ids = []
        for imagePath in imagePaths:
            PIL_img = Image.open(imagePath).convert('L') #grayscale
            img_numpy = np.array(PIL_img,'uint8') #creates an array of the images
            id = int(os.path.split(imagePath)[-1].split(".")[1])
            faces = detector.detectMultiScale(img_numpy) #detect the face
            for (x,y,w,h) in faces: #add the faces and ids into the arrays
                faceSamples.append(img_numpy[y:y+h,x:x+w])
                ids.append(id)
        return faceSamples,ids
    print ("\n [INFO] Training faces. It will take a few seconds. Wait ...")
    faces,ids = getImagesAndLabels(path) #does the above function for each face and id in the dataset folder
    recognizer.train(faces, np.array(ids))
    #save the model into trainer/trainer.yml
    recognizer.write('trainer/trainer.yml') #write the yml file with the faces
    #print the numer of faces trained and end program
    print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))
    f = open("captured.txt", 'w') #write into captured to show that the faces are captured and trained
    f.write("True")
    f.close()