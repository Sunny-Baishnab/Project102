import cv2
import dropbox
import random
import time
startTime = time.time()

def take_picture():
    number = random.randint(0,100)
    videoPicture = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoPicture.read()
        imageName = 'picture'+ str(number) + '.png'
        cv2.imwrite(imageName,frame)
        result = False
    return imageName
    videoPicture.release()
    cv2.destroyAllWindows()
    print('picture has been captured')

def uploadPics(imageName):
    access_token = '_kdXQaWORScAAAAAAAAAAev3fi46cAMrii2jyYnETXDzuErkYiox6TyM0gDwssMe'
    filefrom = imageName
    fileto = '/Project102/'+imageName
    dbx = dropbox.Dropbox(access_token)
    with open(filefrom,'rb') as f:
        dbx.files_upload(f.read(),fileto,mode = dropbox.files.WriteMode.overwrite)
        print('file has been uploaded')

def main():
    while(True):
        if((time.time()-startTime)>=300and(time.time()-startTime)%300==0):
            name = take_snapshot()
            uploadPics(name)

main()

