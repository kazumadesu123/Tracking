import cv2
import time
import numpy as np
import pyautogui as pg
pg.PAUSE = 0.2

video = cv2.VideoCapture(0)
count = video.get(cv2.CAP_PROP_FRAME_COUNT)
threshold = 50

kernel = np.ones((3,3),np.uint8)

wbs = 5
hbs = 5


W = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
H = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(W/5)
print(H/5)

wb = int(W/wbs)
hb = int(H/hbs)


wc = W/2
hc = H/2
wk = int(wc-W/2)
hk = int(hc-H/2)


number=0

while True:
    ret, frame = video.read()
    
    img_thresh = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret2, img_thresh = cv2.threshold(img_thresh, threshold, 255, cv2.THRESH_BINARY)
    img_thresh = cv2.bitwise_not(img_thresh)
    img_thresh = cv2.dilate(img_thresh,kernel,iterations = 3)
    contours, hierarchy = cv2.findContours(img_thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    if len(contours) != 0:
        max_area = 0
        max_contour = contours[0]
        i = 0
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if max_area < area:
                max_area = area
                max_contour = cnt
        mu = cv2.moments(max_contour)
        x,y = int(mu["m10"]/mu["m00"]) , int(mu["m01"]/mu["m00"])
        
        if(0<= x <=128 and 0<= y <=96):
            #if(number != 1):
                pg.keyDown('e')
                number=1
                #time.sleep(0.003)
                pg.keyUp('e')
                


        if(129<= x <=256 and 0<= y <=96):
            #if(number != 2):
                pg.keyDown('a')
                number=2
                #time.sleep(0.003)
                pg.keyUp('a')
            
          
        if(257<= x <=384 and 0<= y <=96):
            if(number != 3): 
                pg.keyDown('w')
                number=3
                time.sleep(0.003)
                pg.keyUp('w')
            
        
        if(385<= x <=512 and 0<= y <=96):
           # if(number != 4):
                pg.keyDown('d')
                number=4
                #time.sleep(0.003)
                pg.keyUp('d')

        
        if(513<= x <=640 and 0<= y <=96):
            if(number != 5):
                pg.keyDown('e')
                number=5
                time.sleep(0.003)
                pg.keyUp('e')
            
        
        if(0<= x <=128 and 97<= y <=192):
            #if(number != 6):  
                pg.keyDown('s')
                number=6
                #time.sleep(0.003)
                pg.keyUp('s')
            
            
        if(129<= x <=256 and 97<= y <=192):
            if(number != 7):
                pg.keyDown('e')
                number=7
                time.sleep(0.003)
                pg.keyUp('e')
            
        
        if(257<= x <=384 and 97<= y <=192):
           #if(number != 8):
                pg.keyDown('w')
                number=8
                #time.sleep(0.003)
                pg.keyUp('w')
                
        
        if(385<= x <=512 and 97<= y <=192):
            #if(number != 9):
                pg.keyDown('e')
                number=9
                #time.sleep(0.003)
                pg.keyUp('e')
                
        
        if(513<= x <=640 and 97<= y <=192):
            if(number != 10):
                pg.keyDown('s')
                number=10
                time.sleep(0.003)
                pg.keyUp('s')
            
            
        if(0 <= x <=128 and 193<= y <=288):
           # if(number != 11):
                pg.keyDown('d')
                number=11
                #time.sleep(0.003)
                pg.keyUp('d')
            
        
        if(129<= x <=256 and 193<= y <=288):
           # if(number != 12): 
                pg.keyDown('a')
                number=12
                #time.sleep(0.003)
                pg.keyUp('a')
    
        
        if(257<= x <=384 and 193<= y <=288):
            #if(number != 13):
                pg.keyDown('e')
                number=13
                #time.sleep(0.003)
                pg.keyUp('e')
                
        
        if(385<= x <=512 and 193<= y <=288):
           # if(number != 14):
                pg.keyDown('d')
                number=14
               # time.sleep(0.003)
                pg.keyUp('d')
            
           
        if(513<= x <=640 and 193<= y <=288):
           # if(number != 15):   
                pg.keyDown('o')
                number=15
               # time.sleep(0.003)
                pg.keyUp('o')
            
        
        if(0<= x <=128 and 289<= y <=384):
           # if(number != 16):
                pg.keyDown('w')
                number=16
               # time.sleep(0.003)
                pg.keyUp('w')

        if(129<= x <=256 and 289<= y <=384):
           # if(number != 17):
                pg.keyDown('d')
                number=17
               # time.sleep(0.003)
                pg.keyUp('d')

        if(257<= x <=384 and 289<= y <=384):
           # if(number != 18):
                pg.keyDown('s')
                number=18
               # time.sleep(0.003)
                pg.keyUp('s')

        if(385<= x <=512 and 289<= y <=384):
          #  if(number != 19):
                pg.keyDown('e')
                number=19
               # time.sleep(0.003)
                pg.keyUp('e')

        if(513<= x <=640 and 289<= y <=384):
            if(number != 20):
                pg.keyDown('w')
                number=20
                time.sleep(0.003)
                pg.keyUp('w')
                

        if(0<= x <=128 and 385<= y <=480):
            #if(number != 21):
                pg.keyDown('e')
                number=21
              #  time.sleep(0.003)
                pg.keyUp('e')

        if(129<= x <=256 and 385<= y <=480):
           # if(number != 22):
                pg.keyDown('s')
                number=22
                #time.sleep(0.003)
                pg.keyUp('s')

        if(257<= x <=384 and 385<= y <=480):
           # if(number != 23):
                pg.keyDown('s')
                number=23
               # time.sleep(0.003)
                pg.keyUp('s')

        if(385<= x <=512 and 358<= y <=480):
            #if(number != 124):
                pg.keyDown('a')
                number=24
                #time.sleep(0.003)
                pg.keyUp('a')

        if(513<= x <=640 and 358<= y <=480):
           # if(number != 25):
                pg.keyDown('e')
                number=25
               # time.sleep(0.003)
                pg.keyUp('e')
            
        cv2.circle(frame, (x,y), 4, 100, 2, 4)
        #cv2.putText(frame, str(max_area), (x-30, y+50), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        frame[hb:H:hb, :, :] = 255
        frame[:,wb:W:wb, :] = 255
        cv2.imshow('adada', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
