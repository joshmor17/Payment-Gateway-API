import cv2
import mediapipe as mp
# import time
import math
import numpy as np

class poseDetector(object):
    def __init__(self, mode=False, complex=2, smooth_L=True, segmentation=False, smooth_S=True,
                 detectionCon=0.95, trackCon=0.5, result=None, pose_landmarks = None):
        self.lmlist = None
        self.mode = mode
        self.complex = complex
        self.smooth_L = smooth_L
        self.segmentation = segmentation
        self.smooth_S = smooth_S
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        # self.result = result
        # self.pose_landmarks = pose_landmarks

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.Pose = self.mpPose.Pose(self.mode, self.complex, self.smooth_L, self.segmentation, self.smooth_S,
                                     self.detectionCon, self.trackCon)

    def findPose(self, img, draw=True):

        # imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.result = self.Pose.process(img)
        if self.result.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.result.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
        return img

    def findPosition(self, img, draw=True):
        self.lmlist = []
        if self.result.pose_landmarks:
            for id, lm in enumerate(self.result.pose_landmarks.landmark):
                h, w, c = img.shape
                # print(id, lm)
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.lmlist.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 3, (255, 0, 0), cv2.FILLED)
        return self.lmlist

    def Angle(self, img, p1, p2, p3, draw=True):
        # Get the landmarks
        x1, y1 = self.lmlist[p1][1:]
        x2, y2 = self.lmlist[p2][1:]
        x3, y3 = self.lmlist[p3][1:]

        # Calculate angle
        angle = math.degrees(math.atan2(y3 - y2, x3 - x2) -
                             math.atan2(y1 - y2, x1 - x2))
        if angle < 0:
            angle += 360
        # print(angle)
        if draw:
            cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 3)
            # cv2.line(img, (x3, y3), (x2, y2), (255, 255, 255), 3)
            cv2.circle(img, (x1, y1), 3, (255, 0, 0), cv2.FILLED)
            # cv2.circle(img, (x1, y1), 15, (255, 0, 0), 2)
            cv2.circle(img, (x2, y2), 3, (255, 0, 0), cv2.FILLED)
            # cv2.circle(img, (x2, y2), 15, (255, 0, 0), 2)
            cv2.circle(img, (x3, y3), 3, (255, 0, 0), cv2.FILLED)
            # cv2.circle(img, (x3, y3), 15, (255, 0, 0), 2)
            cv2.putText(img, str(int(angle)), (x2 - 20, y2 + 50),
                        cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 2)
        return angle

    def findAngle(self, img, p1, p2, p3, draw=True):
        # Get the landmarks
        x1, y1 = self.lmlist[p1][1:]
        x2, y2 = self.lmlist[p2][1:]
        x3, y3 = self.lmlist[p3][1:]

        # Calculate angle
        angle = math.degrees(math.atan2(y3 - y2, x3 - x2) -
                             math.atan2(y1 - y2, x1 - x2))
        if angle < 0:
            angle += 360
        # print(angle)
        if draw:
            cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 3)
            # cv2.line(img, (x3, y3), (x2, y2), (255, 255, 255), 3)
            cv2.circle(img, (x1, y1), 3, (255, 0, 0), cv2.FILLED)
            # cv2.circle(img, (x1, y1), 3, (255, 0, 0), 2)
            cv2.circle(img, (x2, y2), 3, (255, 0, 0), cv2.FILLED)
            # cv2.circle(img, (x2, y2), 3, (255, 0, 0), 2)
            cv2.circle(img, (x3, y3), 3, (255, 0, 0), cv2.FILLED)
            # cv2.circle(img, (x3, y3), 3, (255, 0, 0), 2)
            cv2.putText(img, str(int(angle)), (x2 - 20, y2 + 50),
                        cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 2)
        return angle, x1,y1, x2,y2, x3,y3


    def findAllAngle(self,img,p16,p14,p12, p24, p26, p28, p32, p15, p13, p11, p23, p25, p27, p31,color0,color1,color2):
        d16 = self.lmlist[p16][1:]
        d14 = self.lmlist[p14][1:]
        d12 = self.lmlist[p12][1:]
        d24 = self.lmlist[p24][1:]
        d26 = self.lmlist[p26][1:]
        d28 = self.lmlist[p28][1:]
        d32 = self.lmlist[p32][1:]
        d15 = self.lmlist[p15][1:]
        d13 = self.lmlist[p13][1:]
        d11 = self.lmlist[p11][1:]
        d23 = self.lmlist[p23][1:]
        d25 = self.lmlist[p25][1:]
        d27 = self.lmlist[p27][1:]
        d31 = self.lmlist[p31][1:]

        cv2.line(img, d16, d14, (color0,color1,color2), 3)
        cv2.line(img, d14, d12, (color0,color1,color2), 3)
        cv2.line(img, d12, d24, (color0,color1,color2), 3)
        cv2.line(img, d24, d26, (color0,color1,color2), 3)
        cv2.line(img, d26, d28, (color0,color1,color2), 3)
        cv2.line(img, d28, d32, (color0,color1,color2), 3)

        cv2.line(img, d15, d13, (color0,color1,color2), 3)
        cv2.line(img, d13, d11, (color0,color1,color2), 3)
        cv2.line(img, d11, d23, (color0,color1,color2), 3)
        cv2.line(img, d23, d25, (color0,color1,color2), 3)
        cv2.line(img, d25, d27, (color0,color1,color2), 3)
        cv2.line(img, d27, d31, (color0,color1,color2), 3)

        cv2.line(img, d12, d11, (color0,color1,color2), 3)
        cv2.line(img, d24, d23, (color0,color1,color2),3)

    def Correctpose(self, img,angle, limb,x1,y1,x2,y2,x3,y3,anglerange1,anglerange2,limbrange1,limbrange2,exact1,exact2):
        if (int(angle) <= anglerange1 and int(angle) >= anglerange2):  # 28
            cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 4)
            # cv2.line(img, (x3, y3), (x2, y2), (0, 0, 255), 4)

            if (int(limb) <= limbrange1 and int(limb) >= limbrange2):
                cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 4)
                cv2.line(img, (x3, y3), (x2, y2), (0, 255, 0), 4)

                addkanan = np.interp(limb, (limbrange2, exact1), (1, 15))
                minuskanan = np.interp(limb, (exact2, limbrange1), (0, 15))
                bar = int(addkanan) - int(minuskanan)

                if bar == 15:
                    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 4)
                    cv2.line(img, (x3, y3), (x2, y2), (0, 255, 0), 4)

                elif bar >= 5:
                    cv2.line(img, (x1, y1), (x2, y2), (0, 165, 255), 4)
                    cv2.line(img, (x3, y3), (x2, y2), (0, 165, 255), 4)

                else:
                    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 255), 4)
                    cv2.line(img, (x3, y3), (x2, y2), (0, 255, 255), 4)

                return int(bar)

        else:
            cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 4)
            cv2.line(img, (x3, y3), (x2, y2), (0, 0, 255), 4)

    def Correctfoot(self, img, limb, x1, y1, x2, y2, x3, y3, x4,y4, limbrange1, limbrange2, exact1, exact2):

        if (int(limb) <= limbrange1 and int(limb) >= limbrange2):
            cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 4)
            cv2.line(img, (x3, y3), (x2, y2), (0, 255, 0), 4)

            # cv2.line(img, (x2, y2), (x4, y4), (0, 255, 0), 4)
            # cv2.line(img, (x3, y3), (x4, y4), (0, 255, 0), 4)

            addkanan = np.interp(limb, (limbrange2, exact1), (1, 5))
            minuskanan = np.interp(limb, (exact2, limbrange1), (0, 5))
            bar = int(addkanan) - int(minuskanan)

            if bar == 5:
                cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 4)
                cv2.line(img, (x3, y3), (x2, y2), (0, 255, 0), 4)

                # cv2.line(img, (x2, y2), (x4, y4), (0, 255, 0), 4)
                # cv2.line(img, (x3, y3), (x4, y4), (0, 255, 0), 4)


            elif bar >= 2:
                cv2.line(img, (x1, y1), (x2, y2), (0, 165, 255), 4)
                cv2.line(img, (x3, y3), (x2, y2), (0, 165, 255), 4)

                # cv2.line(img, (x2, y2), (x4, y4), (0, 165, 255), 4)
                # cv2.line(img, (x3, y3), (x4, y4), (0, 165, 255), 4)

            else:
                cv2.line(img, (x1, y1), (x2, y2), (0, 255, 255), 4)
                cv2.line(img, (x3, y3), (x2, y2), (0, 255, 255), 4)

                # cv2.line(img, (x2, y2), (x4, y4),(0, 255, 255), 4)
                # cv2.line(img, (x3, y3), (x4, y4),(0, 255, 255), 4)

            return int(bar)

        else:
            cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 4)
            cv2.line(img, (x3, y3), (x2, y2), (0, 0, 255), 4)

            # cv2.line(img, (x2, y2), (x4, y4), (0, 0, 255), 4)
            # cv2.line(img, (x3, y3), (x4, y4), (0, 0, 255), 4)

    def findFoot(self, img, p1, p2, p3, p4,draw=True):
        # Get the landmarks
        x1, y1 = self.lmlist[p1][1:]
        x2, y2 = self.lmlist[p2][1:]
        x3, y3 = self.lmlist[p3][1:]
        x4, y4 = self.lmlist[p4][1:]

        # Calculate angle
        angle = math.degrees(math.atan2(y3 - y2, x3 - x2) -
                             math.atan2(y1 - y2, x1 - x2))
        if angle < 0:
            angle += 360
        # print(angle)
        if draw:
            cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 3)
            cv2.line(img, (x3, y3), (x2, y2), (255, 255, 255), 3)
            cv2.circle(img, (x1, y1), 3, (255, 0, 0), cv2.FILLED)
            # cv2.circle(img, (x1, y1), 3, (255, 0, 0), 2)
            cv2.circle(img, (x2, y2), 3, (255, 0, 0), cv2.FILLED)
            # cv2.circle(img, (x2, y2), 3, (255, 0, 0), 2)
            cv2.circle(img, (x3, y3), 3, (255, 0, 0), cv2.FILLED)
            # cv2.circle(img, (x3, y3), 3, (255, 0, 0), 2)
            #cv2.putText(img, str(int(angle)), (x2 - 20, y2 + 50),
                        #cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 2)
        return angle, x1,y1, x2,y2, x3,y3, x4,y4

    def Accuracycolor(self,bartotal,canvas,rectangle):

        if bartotal >= 90:
            canvas.itemconfig(rectangle, fill='green')
        elif bartotal >= 70:
            canvas.itemconfig(rectangle, fill='orange')
        elif bartotal >= 60:
            canvas.itemconfig(rectangle, fill='yellow')
        else:
            canvas.itemconfig(rectangle, fill='red')

    def Accuracytext(self,averageaccuracy):

        if averageaccuracy >= 90:
            text = "EXCELLENT"
        elif averageaccuracy >= 70:
            text = "GOOD JOB"
        elif averageaccuracy >= 60:
            text = "NICE JOB"
        else:
            text = "TRY AGAIN"

        return text

    def findChest(self, img, p1, p2, p3, p4, p5, draw=True):
        # Get the landmarks
        x1, y1 = self.lmlist[p1][1:]
        x2, y2 = self.lmlist[p2][1:]
        x3, y3 = self.lmlist[p3][1:]
        x4, y4 = self.lmlist[p4][1:]
        x5, y5 = self.lmlist[p5][1:]

        # Calculate angle
        angle = math.degrees(math.atan2(y3 - y2, x3 - x2) -
                             math.atan2(y1 - y2, x1 - x2))
        if angle < 0:
            angle += 360
        # print(angle)
        if draw:
            cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 3)
            # cv2.line(img, (x3, y3), (x2, y2), (255, 255, 255), 3)
            cv2.circle(img, (x1, y1), 3, (255, 0, 0), cv2.FILLED)
            # cv2.circle(img, (x1, y1), 3, (255, 0, 0), 2)
            cv2.circle(img, (x2, y2), 3, (255, 0, 0), cv2.FILLED)
            # cv2.circle(img, (x2, y2), 3, (255, 0, 0), 2)
            cv2.circle(img, (x3, y3), 3, (255, 0, 0), cv2.FILLED)
            # cv2.circle(img, (x3, y3), 3, (255, 0, 0), 2)
            cv2.putText(img, str(int(angle)), (x2 - 20, y2 + 50),
                        cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 2)
        return angle, x1,y1, x2,y2, x4, y4, x5, y5

    def CorrectChest(self, img, limb,x1,y1,x2,y2,x3,y3,x4,y4,limbrange1,limbrange2,exact1,exact2):
        if (int(limb) <= limbrange1 and int(limb) >= limbrange2):
            cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 4)

            addkanan = np.interp(limb, (limbrange2, exact1), (1, 30))
            minuskanan = np.interp(limb, (exact2, limbrange1), (0, 30))
            bar = int(addkanan) - int(minuskanan)

            if bar == 30:
                cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 4)
                cv2.line(img, (x2, y2), (x3, y3), (0, 255, 0), 4)
                cv2.line(img, (x3, y3), (x4, y4), (0, 255, 0), 4)
                cv2.line(img, (x4, y4), (x1, y1), (0, 255, 0), 4)

            elif bar >= 15:
                cv2.line(img, (x1, y1), (x2, y2), (0, 165, 255), 4)
                cv2.line(img, (x2, y2), (x3, y3), (0, 165, 255), 4)
                cv2.line(img, (x3, y3), (x4, y4), (0, 165, 255), 4)
                cv2.line(img, (x4, y4), (x1, y1), (0, 165, 255), 4)

            else:
                cv2.line(img, (x1, y1), (x2, y2), (0, 255, 255), 4)
                cv2.line(img, (x2, y2), (x3, y3), (0, 255, 255), 4)
                cv2.line(img, (x3, y3), (x4, y4), (0, 255, 255), 4)
                cv2.line(img, (x4, y4), (x1, y1), (0, 255, 255), 4)

            return int(bar)

        else:
            cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 4)
            cv2.line(img, (x2, y2), (x3, y3), (0, 0, 255), 4)
            cv2.line(img, (x3, y3), (x4, y4), (0, 0, 255), 4)
            cv2.line(img, (x4, y4), (x1, y1), (0, 0, 255), 4)

    def Left(self, frame, kaliwakamay, angle_kaliwakamay, kanankamay, angle_kanankamay, paakaliwa, angle_paakaliwa,
             paakanan, angle_paakanan, footkaliwa, footkanan,chest):
        cv2.putText(frame, "LeftLimb = " + str(int(kaliwakamay)), (20, 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
        cv2.putText(frame, "LeftPit = " + str(int(angle_kaliwakamay)), (20, 60), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255),2)
        cv2.putText(frame, "RightLimb = " + str(int(kanankamay)), (20, 90), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
        cv2.putText(frame, "RightPit = " + str(int(angle_kanankamay)), (20, 120), cv2.FONT_HERSHEY_PLAIN, 2,(0, 0, 255), 2)
        cv2.putText(frame, "LeftLeg = " + str(int(paakaliwa)), (20, 150), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
        cv2.putText(frame, "LeftHip = " + str(int(angle_paakaliwa)), (20, 180), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255),2)
        cv2.putText(frame, "RightLeg = " + str(int(paakanan)), (20, 210), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
        cv2.putText(frame, "RightHip = " + str(int(angle_paakanan)), (20, 240), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255),2)
        cv2.putText(frame, "LeftFoot= " + str(int(footkaliwa)), (20, 270), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
        cv2.putText(frame, "RightFoot = " + str(int(footkanan)), (20, 300), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
        cv2.putText(frame, "Chest = " + str(int(chest)), (20, 330), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)

        # if timeforending % total_time + 1 >= total_time + 1 - delay_time:
        #     # For video display
        #     cv2.putText(frame, "Up Next11111", (30, 280), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 4)
        #     cv2.putText(frame, poseName[index], (30, 370), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 5)
        #     cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #
        #     # for timer
        #     # cv2.putText(frame, str(timeforending % total_time + 1 - minus), (780, 70), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 2)
        #
        # else:
        #     # for video display
        #     cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        #
        #     # for timer
        #     cv2.putText(frame, str(timeforending % total_time + 1), (780, 70), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255),
        #                 2)