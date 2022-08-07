import cv2
import cvzone
import time
import random
from cvzone.HandTrackingModule import HandDetector
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

detector =HandDetector(maxHands=1)
timer=0
startresult=False
startgame=False
score=[0,0]
turn=0

while True:
    bg=cv2.imread("resources/bg.png")
    ro=cv2.imread("resources/ro.png")
    sc = cv2.imread("resources/sc.png")
    pa = cv2.imread("resources/pa.png")
    ro=cv2.resize(ro, (465, 465))
    sc = cv2.resize(sc, (465, 465))
    pa = cv2.resize(pa, (465, 465))
    cv2.imwrite('resources/1.png', ro)
    cv2.imwrite('resources/2.png', pa)
    cv2.imwrite('resources/3.png', sc)


    success , img = cap.read()
    imscaled = cv2.resize(img,(0,0),None,0.968,0.968)

    imscaled=imscaled[:,77:542]
    hands, img = detector.findHands(imscaled)

    if(startgame and turn < 5):
        if startresult is False:
            timer=time.time() - intialtime
            cv2.putText(bg,str(int(timer)),(930,650),cv2.FONT_HERSHEY_PLAIN,6,(255,0,255),4)
        if(timer > 2):
            startresult=True
            timer=0

            if(hands):
                hand=hands[0]
                fingers=detector.fingersUp(hand)
                play=0
                if fingers == [1,0,0,0,0] or fingers == [0,0,0,0,0]:
                    play=1
                if fingers == [0,1,1,0,0]:
                    play=2
                if fingers == [1,1,1,1,1]:
                    play=3
                d = random.randint(1,3)
                print("play,random",play,d)
                imgai=cv2.imread(f'resources/{d}.png',cv2.IMREAD_UNCHANGED)
                if((play==1 and d == 3 ) or (play == 2 and d== 2) or (play == 3 and d== 1)):
                    score[1]=score[1]+1
                elif ((play == 1 and d == 2) or (play == 2 and d == 1) or (play == 3 and d == 3)):
                    score[0] = score[0] + 1
                turn=turn+1



                bg[393:858, 154:619]= imgai
    else:
        if(score[0]>score[1]):
            cv2.putText(bg, " CPU Win the", (690,400), cv2.FONT_HERSHEY_PLAIN, 4, (0, 0, 0), 4)
            cv2.putText(bg, " game", (750, 450), cv2.FONT_HERSHEY_PLAIN, 4, (0, 0, 0), 4)
        elif(score[0]<score[1]):
            cv2.putText(bg, " You Win the", (690,400), cv2.FONT_HERSHEY_PLAIN, 4, (0, 0, 0), 4)

            cv2.putText(bg, " game", (750, 450), cv2.FONT_HERSHEY_PLAIN, 4, (0, 0, 0), 4)
        elif(score[0] == score[1] != 0 ):
            cv2.putText(bg, "Game tie", (670,450), cv2.FONT_HERSHEY_PLAIN, 4, (0, 0, 0), 4)



                #print(play)
                #print(fingers)
    bg[393:858,1313:1778]=imscaled
    if(startresult):
        bg[393:858, 154:619]= imgai

    cv2.putText(bg," CPU " +str(int(score[0])), (250, 275), cv2.FONT_HERSHEY_PLAIN, 4, (0, 0, 0), 4)
    cv2.putText(bg, " YOUR  " + str(int(score[1])), (1400, 275), cv2.FONT_HERSHEY_PLAIN, 4, (0, 0, 0), 4)


    cv2.imshow("image1", bg)
    #cv2.imshow("image",img)
    #cv2.imshow("imagescaled", imscaled)

    key=cv2.waitKey(1)
    if key == ord('s'):

        startgame = True
        intialtime=time.time()
        startresult = False



