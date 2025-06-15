import cv2

import mediapipe as mp

import time

import pyautogui


cap = cv2.VideoCapture(0)
previousTime=0
prev = 0
tres = 10
should =0
prevl=0

mpPose = mp.solutions.pose

pose = mpPose.Pose()

mpDraw =mp.solutions.drawing_utils

while True:
    lmlist = []
    success,img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    

    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h,w,c = img.shape

            cx, cy = int(lm.x * w) , int(lm.y * h)
            lmlist.append([id, cx,cy])

            cv2.circle(img, (cx,cy), 10, (255,0,0), cv2.FILLED)
    

    currentTime = time.time()
    fps = 1/(currentTime-previousTime)
    pTime=currentTime
    

    cv2.putText(img, str(int(fps)), (70,50), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 3)

    cv2.imshow("img",img)


    
    
    currs = lmlist[12][2] #shoulder
    curr = lmlist[16][2] # new position of right hand
    currl= lmlist[15][2] #new positio of left hand
    mov = curr - prev    #distance of how much right hand moved
    movl = currl - prevl #distance of hoe much left hand moved
    prev = curr          #to store the previous value of position of right hand
    prevl=currl          #to store the prevuous value of position of left hand
    movs = currs - should 
    should = currs       #to store the old value of shoulder position

    relb = lmlist[14][2] #right elbow
    lelb = lmlist[13][2] #left elbow

    mid = (lmlist[11][2]+lmlist[23][2])/2
    


      
    if  movl < 0 and abs(movl) > tres and lelb > mid:
             pyautogui.scroll(abs(movl)*-35)
            
         
         
    elif mov > 0 and abs(mov) > tres and relb < mid  :

             pyautogui.scroll(abs(mov)*35)
     



       
      
       
        
   
      
      
       

    cv2.waitKey(4)


    


