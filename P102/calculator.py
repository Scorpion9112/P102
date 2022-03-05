import cv2
import time
import random
import dropbox

start_time=time.time()
print(start_time)

def Take_SnapShot():
    randomNumber=random.randint(0,100)

    videoCaptureObject=cv2.VideoCapture(0)

    result=True
    while(result):
        ret, frame=videoCaptureObject.read()
        imageName="image"+str(randomNumber)+".png"
        cv2.imwrite(imageName,frame) #image storage
        start_time=time.time
        result=False

    return imageName
    videoCaptureObject.release() #closing webcam
    cv2.destoryAllWindows() #closes windows opened by camera

def UploadFile(imageName):
    accessToken=""
    file_from=imageName
    file_to="/securityImages/"+imageName

    dbx=dropbox.Dropbox(accessToken)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode.overwrite) 


def Main():
    while(True):
        if((time.time()-start_time>=180)):
            imageName=Take_SnapShot()
            uploadFile(imageName)

Main()