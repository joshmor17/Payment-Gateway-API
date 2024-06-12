from tkinter import *
import tkinter as tk
import tkinter.font as font
import time
import cv2
from PIL import Image, ImageTk
import numpy as np
import pygame
import webbrowser
from tkinter import ttk
from tkinter import filedialog
from tktooltip import ToolTip
import re

import datetime
from datetime import date, timedelta
import calendar

from tkinter import messagebox

from CreatePaymentIntent import *
from CreatePaymentMethod import *
from AttachToPaymentIntent import *


#import mysql.connector
import module as pm
import class_function as cf
# import sample_cf as cf


window = tk.Tk()
window.title("Yoga With LeAnne")
# window.iconbitmap("images/")
window.geometry("1366x768")
window.state("zoomed")
# window.resizable(False, False)
pygame.mixer.init()

get_data = cf.get_data()
get_accuracy = cf.get_accuracy()
tkinter_design = cf.tkinter_design()
yoga_function = cf.yoga_function()
gmail_verification = cf.gmail_verification()
yoga_cert = cf.yoga_cert()

# to get user setting values
user_settings_value = yoga_function.open_setting()

detector = pm.poseDetector(complex=user_settings_value[0])
user_volume_level = user_settings_value[2]
user_selected_music = user_settings_value[3]

#mydb = mysql.connector.connect(
#    host="localhost",
#    user="jasmin",
#    password="pass123",
#    database="yoga_database"

#)

# to get all acount
#mycursor = mydb.cursor()
#mycursor.execute('SELECT * FROM yoga_accounts')
#users_mysql = mycursor.fetchall()

#computer date
date_today = date.today()

def Page1():
    Background_Frame = Frame(Page_frame)
    Background_Frame.place(x=0, y=0)
    Label(Background_Frame, image=bG_image, borderwidth=0).pack()

    def retry_frame_container(items, items2, items3):
        for widgets in retry_Frame.winfo_children():
            widgets.destroy()

        retry_Frame.tkraise()

        def end_frame(items, items2, items3):
            for widgets in retry_Frame.winfo_children():
                widgets.destroy()

            Label(retry_Frame, image=bg, borderwidth=0).place(x=0, y=0)

            f = Frame(retry_Frame, bg="#f8f2f2")
            f.grid(row=0, column=0, pady=30)
            yoganame = items[0]
            percent_yoga = items2[0]

            if len(yoganame) == 1:
                pady = 101
            elif len(yoganame) == 2:
                pady = 41
            elif len(yoganame) == 3:
                pady = 21
            elif len(yoganame) == 4:
                pady = 11
            else:
                pady = 5

            for idx, i in enumerate(yoganame):
                if idx <= 4:
                    Label(f, text=i, font=('Book Antiqua', 20), bg="#f8f2f2").grid(row=idx, column=0, padx=10,
                                                                                   pady=pady)
                    Label(f, text=percent_yoga[idx], font=('Book Antiqua', 20), bg="#f8f2f2").grid(row=idx, column=1,
                                                                                                   padx=10)
                else:
                    Label(f, text=" ", bg="#f8f2f2").grid(row=idx - 5, column=2, padx=30)
                    Label(f, text=i, font=('Book Antiqua', 20), bg="#f8f2f2").grid(row=idx - 5, column=3, padx=10)
                    Label(f, text=percent_yoga[idx], font=('Book Antiqua', 20), bg="#f8f2f2").grid(row=idx - 5,
                                                                                                   column=4)

            g = Frame(retry_Frame, bg="#f8f2f2")
            g.grid(row=2, column=0)
            tkinter_design.end_frame_text(g, items2[1])

            k = Canvas(retry_Frame, bg="#f8f2f2", width=600, height=50, highlightthickness=0)
            k.grid(row=3, column=0, pady=5, padx=150)
            bargraph = np.interp(items2[1], (0, 100), (3, 597))
            k.create_rectangle(3, 47, bargraph, 3, fill="green")  # rectangle fill
            k.create_rectangle(3, 47, 597, 3, width=2)  # rectangle borderwidth

            k.create_text(300, 25, text=f"{items2[1]}%", font=('Book Antiqua', 30), anchor=CENTER)

            t = Frame(retry_Frame, bg="#f8f2f2")
            t.grid(row=4, column=0, pady=22)
            Button(t, text="Pick Poses", font=('Book Antiqua', 15),
                   command=lambda: practice_session(items, items2, items3)).grid(row=0, column=0, padx=40, )
            Button(t, text="START", font=('Book Antiqua', 20),
                   command=lambda: camera_check(items, items2, items3)).grid(row=0, column=1, padx=40, pady=10,
                                                                             ipadx=20)
            Button(t, text="Exit", font=('Book Antiqua', 15), command=Home_Frame).grid(row=0, column=2, padx=40,
                                                                                       ipadx=15)

            window.mainloop()

        def practice_session(items, items2, items3):
            for widgets in retry_Frame.winfo_children():
                widgets.destroy()
            Label(retry_Frame, image=bg, borderwidth=0).place(x=0, y=0)

            a = Frame(retry_Frame, bg="#f8f2f2")
            a.grid(row=0, column=0, pady=24, padx=25)
            text = "Practice makes perfect! Improve your yoga poses! Tick the box\nso you can select on yoga poses."
            text2 = "Note: Practice session will not be counted as a progress.You must complete the whole session to record your progress."
            Label(a, text=text, font=('Book Antiqua', 18), bg="#f8f2f2").grid(row=0, column=0)
            Label(a, text=text2, font=('Book Antiqua', 12), bg="#f8f2f2", fg="red").grid(row=1, column=0)

            b = Frame(retry_Frame, bg="#f8f2f2")
            b.grid(row=1, column=0)

            def checkbox_totaltime():
                global user_want_pose
                global user_want_list
                user_want_pose = 0

                user_want_list = []  # to know how many yoganame.get()
                for i in range(len(yoganame)):
                    user_want_list.append(my_variables["var" + str(i)].get())

                for i in user_want_list:
                    if i == 1:
                        user_want_pose += 1

                if user_want_pose == 0:
                    practice_startbutton['state'] = DISABLED
                else:
                    practice_startbutton['state'] = NORMAL

                yogatime, preptime, cdtime, lp = int(yoga_time.get()), int(prep_time.get()), int(cd_time.get()), int(
                    loop.get())

                convert = yoga_function.set_time_formula(yogatime, user_want_pose, lp, preptime, cdtime)
                total_time.config(text=convert)

            user_want_pose = 0
            yoganame = items[0]
            yogapercent = items2[0]

            pady = yoga_function.yoganame_pady(len(yoganame))
            my_variables = {}

            for idx, j in enumerate(yoganame):
                if idx <= 4:
                    my_variables["var" + str(idx)] = IntVar()
                    tkinter_design.practice_checkbutton(b, yoganame[idx], yogapercent[idx],
                                                        my_variables["var" + str(idx)],
                                                        16, checkbox_totaltime, idx, pady)
                else:
                    my_variables["var" + str(idx)] = IntVar()
                    tkinter_design.practice_checkbutton2(b, yoganame[idx], yogapercent[idx],
                                                         my_variables["var" + str(idx)],
                                                         16, checkbox_totaltime, idx)

            b1 = Frame(retry_Frame, bg="#f8f2f2")
            b1.grid(row=2, ipadx=330)
            tkinter_design.practice_session_label(b1, "Set Timer", 17, 0, 0, 10, W)

            b2 = Frame(retry_Frame, bg="#f8f2f2")
            b2.grid(row=3)

            tkinter_design.practice_session_label(b2, "", 15, 0, 0, 280, None)  # for spance
            Label(b2, text="Total Time:", bg="#f8f2f2", font=('Book Antiqua', 15)).grid(row=0, column=1)
            total_time = Label(b2, text="20", bg="#f8f2f2", font=('Book Antiqua', 15))
            total_time.grid(row=0, column=2, padx=2)

            c = Frame(retry_Frame, bg="#f8f2f2")
            c.grid(row=4, column=0)

            tkinter_design.practice_session_label(c, "", 15, 2, 3, 20, None)  # for space

            def limit_characters(k, limit, empty, *args):
                global user_want_pose
                if k.get().isdigit() == FALSE:  # to accept digit only
                    song_renames = k.get()
                    k.set(str(''.join(k for k in song_renames if k.isdigit())))

                if len(k.get()) > limit:  # limit user enter
                    k.set(k.get()[:limit])

                if len(k.get()) == 0 or int(k.get()) < empty:  # set number if empty and limit to certain above value
                    k.set(empty)

                yogatime, preptime, cdtime, lp = int(yoga_time.get()), int(prep_time.get()), int(cd_time.get()), int(
                    loop.get())
                # convert_min = int(((yogatime * user_want_pose) * (lp + 1)) + ((preptime * user_want_pose) * (lp + 1)) + (
                #         (cdtime) * (lp)))
                convert = yoga_function.set_time_formula(yogatime, user_want_pose, lp, preptime, cdtime)
                total_time.config(text=convert)

            yoga_time = yoga_function.int_only(3, 5, limit_characters)
            prep_time = yoga_function.int_only(3, 5, limit_characters)
            cd_time = yoga_function.int_only(3, 5, limit_characters)
            loop = yoga_function.int_only(1, 0, limit_characters)

            tkinter_design.practice_session_entry(c, "Yoga Time:", yoga_time, 15, 2, 0, 1)
            tkinter_design.practice_session_entry(c, "Preparation Time:", prep_time, 15, 3, 0, 1)
            tkinter_design.practice_session_entry(c, "Repetetion:", loop, 15, 2, 4, 2)
            tkinter_design.practice_session_entry(c, "Cooldown:", cd_time, 15, 3, 4, 1)
            Label(c, text=" ", bg="#f8f2f2", font=('Book Antiqua', 15)).grid(row=3, column=6,
                                                                             padx=80)  # for space in rigth side

            d = Frame(retry_Frame, bg="#f8f2f2")
            d.grid(row=5, column=0, pady=20)

            def start():

                user_yoganame = []
                user_kaliwa_bar = []
                user_kanan_bar = []
                user_paakaliwabar = []
                user_paakananbar = []
                user_kaliwafoot = []
                user_kananfoot = []
                user_rightchest = []
                user_pictures = []

                for idx, i in enumerate(user_want_list):
                    if i == 1:
                        user_yoganame.append(items[0][idx])
                        user_kaliwa_bar.append(items[1][idx])
                        user_kanan_bar.append(items[2][idx])
                        user_paakaliwabar.append(items[3][idx])
                        user_paakananbar.append(items[4][idx])
                        user_kaliwafoot.append(items[5][idx])
                        user_kananfoot.append(items[6][idx])
                        user_rightchest.append(items[7][idx])
                        user_pictures.append(items[12][idx])

                # yoganame,kaliwabar_list, kananbar_list, paakaliwabar_list, paakananbar_list, kaliwafoot_list, kananfoot_list, rightchest_list, \
                # yogatime, preparationtime, loop, cooldown
                user_items1 = [user_yoganame, user_kaliwa_bar, user_kanan_bar, user_paakaliwabar, user_paakananbar,
                               user_kaliwafoot, user_kananfoot, user_rightchest, \
                               int(yoga_time.get()), int(prep_time.get()), int(loop.get()), int(cd_time.get()),
                               user_pictures]
                user_items2 = [0, 0, items[2]]
                user_items3 = False
                # easyfirstsession(user_items1,user_items2,user_items3)
                camera_check(user_items1, user_items2, user_items3)

            practice_startbutton = Button(d, text="Start", font=('Book Antiqua', 18), command=start)
            practice_startbutton.grid(row=0, column=0, ipadx=10, padx=20)
            Button(d, text="Cancel", font=('Book Antiqua', 18), command=lambda: end_frame(items, items2, items3)).grid(
                row=0, column=1, padx=20)
            checkbox_totaltime()

        def camera_check(items, items2, items3):
            cam = cv2.VideoCapture(0)
            useable, __ = cam.read()

            if useable == True:
                easyfirstsession(items, items2, items3)
                # sample(items, items2, items3)

            else:
                print("ey")
                for widgets in option_music_frame.winfo_children():
                    widgets.destroy()

                Change_Frame.tkraise()
                option_music_frame.tkraise()
                Label(option_music_frame, image=option_image, borderwidth=0).place(x=0, y=0)
                #
                Label(option_music_frame, bg='#f8f2f2').pack(pady=5)
                text = "It looks like another app \nis using the camera already."
                Label(option_music_frame, text=text, font=('Book Antiqua', 16), bg='#f8f2f2').pack(padx=67)
                Button(option_music_frame, text="Okay", font=('Book Antiqua', 14),
                       command=lambda: retry_Frame.tkraise()).pack(pady=10)

        end_frame(items, items2, items3)
        window.mainloop()


    def sample(items,items2,items3):
        global present_account

        details = present_account[8]
        data_split = details.split('-')

        change_array = "100/100/100/100/100/100/100/100/100/100"

        data_split[items2[2]] = change_array # items2[2] is for index
        listToStr = '-'.join([str(elem) for elem in data_split])

        #may error, need it to change yung tuple
        present_account = list(present_account)

        #to update accuracy
        present_account[8] = listToStr
        # sql = f"UPDATE yoga_accounts SET user_accuracy = '{listToStr}' WHERE id = '{present_account[0]}'"
        # mycursor.execute(sql)
        # mydb.commit()

        # to update number of tries
        split_user_try = present_account[7].split("/")

        print(present_account[7])
        if items2[2] > 5:
            plus_try = int(split_user_try[2]) + 1
            changed_try = f"{split_user_try[0]}/{split_user_try[1]}/{plus_try}"
        elif items2[2] >2:
            plus_try = int(split_user_try[1]) + 1
            changed_try = f"{split_user_try[0]}/{plus_try}/{split_user_try[2]}"
        else:
            plus_try = int(split_user_try[0]) + 1
            changed_try = f"{plus_try}/{split_user_try[1]}/{split_user_try[2]}"

        present_account[7] = changed_try

        #sql = f"UPDATE yoga_accounts SET user_accuracy = '{listToStr}', user_try = '{changed_try}' WHERE id = '{present_account[0]}'"
        #mycursor.execute(sql)
        #mydb.commit()


    def easyfirstsession(items, items2, items3):
        print(detector.complex)
        global my_img
        global index
        global count
        global totalaccuracy
        global averageaccuracy
        global ptime
        global ctime
        global labeltime
        global checker
        global display_low
        global sound_countdown
        global sound_countdown_bool

        cap = cv2.VideoCapture(0)

        pygame.mixer.Channel(1).play(pygame.mixer.Sound(user_selected_music), loops=-1)

        poseName = items[0]
        kaliwabar_list = items[1]
        kananbar_list = items[2]
        paakaliwabar_list = items[3]
        paakananbar_list = items[4]
        kaliwafoot_list = items[5]
        kananfoot_list = items[6]
        rightchest_list = items[7]

        numberofyoga = len(poseName)

        set_time = items[8]
        delay_time = items[9]
        numberofloop = items[10] + 1
        timeforcooldown = items[11]
        total_time = set_time + delay_time
        minus = total_time - delay_time
        time_s = total_time * numberofyoga * numberofloop

        pictures = items[12]
        index = 0

        top = Toplevel(window)
        top.title("SESSION 1")
        top.geometry('1366x768')
        # top.resizable(False, False)
        top.configure(bg='indigo')

        videoframe = Frame(top, width=420, height=240, bg='indigo')
        videoframe.place(x=0, y=0)

        image = Image.open(pictures[index])
        img = image.resize((420, 240))
        my_img = ImageTk.PhotoImage(img)
        panel = Label(videoframe, image=my_img, borderwidth=0)
        panel.pack()

        timeframe = Frame(top, height=240, width=420, bg="indigo", bd=1, relief=FLAT)
        timeframe.place(x=0, y=240)
        labeltime = Label(timeframe, font=('Orbitron-Black', 80), bg="indigo", fg="white")
        labeltime.place(relx=0.5, rely=0.5, anchor=CENTER)

        imageFrame = Frame(top, width=900, height=720, bg='red')
        imageFrame.place(x=440, y=5)

        lmain = Label(imageFrame, borderwidth=0)
        lmain.place(x=0, y=0)

        def countdown(count1):
            global timer
            global labeltime
            global index
            global pose_detector
            global taccuracy
            global timeforending
            global timer_stop
            global checker

            taccuracy = count1 % total_time
            timeforending = count1

            # change text in label
            if count1 % total_time + 1 >= total_time + 1 - delay_time:
                # print(count1 % total_time + 1)
                labeltime['text'] = str(count1 % total_time + 1 - minus)
                pose_detector = True

            else:
                labeltime['text'] = str(count1 % total_time + 1)
                pose_detector = True

            if count1 > 0:
                # call countdown again after 1000ms (1s)
                timer_stop = window.after(1000, countdown, count1 - 1)
                checker = True

            if count1 != time_s - 1 and count1 % (time_s / numberofloop) == time_s / numberofloop - 1:  # 23 11
                index = 0
                showvideo()
                window.after_cancel(timer_stop)
                cooldown(timeforcooldown)

            if count1 != time_s - 1 and count1 % total_time == total_time - 1 and count1 % (
                    time_s / numberofloop) != time_s / numberofloop - 1:
                index += 1
                showvideo()

        def cooldown(cool):
            global timeforending
            global cooldown_duration

            if cool >= 0:
                cooldown_duration = window.after(1000, cooldown, cool - 1)
                labeltime['text'] = str(cool)
            if cool == 0:
                window.after_cancel(cooldown_duration)
                countdown(timeforending - 1)

        def treePose():
            global pose_detector
            global count
            global totalaccuracy
            global averageaccuracy
            global ctime
            global ptime
            global frame
            global tocount
            global checker
            global display_low
            global sound_countdown
            global sound_countdown_bool

            _, frame = cap.read()
            frame = cv2.flip(frame, 1)
            frame = cv2.resize(frame, (900, 720))

            frame = detector.findPose(frame, False)
            lmlist = detector.findPosition(frame, False)

            if len(lmlist) != 0:

                footkaliwa = detector.findFoot(frame, 26, 28, 32, 30)
                footkaliwabar = detector.Correctfoot(frame, footkaliwa[0], footkaliwa[1], footkaliwa[2], footkaliwa[3],
                                                     footkaliwa[4], footkaliwa[5], footkaliwa[6], footkaliwa[7],
                                                     footkaliwa[8],
                                                     kaliwafoot_list[index][0], kaliwafoot_list[index][1],
                                                     kaliwafoot_list[index][2],
                                                     kaliwafoot_list[index][3])

                footkanan = detector.findFoot(frame, 25, 27, 31, 29)
                footkananbar = detector.Correctfoot(frame, footkanan[0], footkanan[1], footkanan[2], footkanan[3],
                                                    footkanan[4], footkanan[5], footkanan[6], footkanan[7],
                                                    footkanan[8],
                                                    kananfoot_list[index][0], kananfoot_list[index][1],
                                                    kananfoot_list[index][2],
                                                    kananfoot_list[index][3])

                kaliwakamay = detector.findAngle(frame, 12, 14, 16)
                angle_kaliwakamay = detector.Angle(frame, 24, 12, 14)

                kaliwabar = detector.Correctpose(frame, angle_kaliwakamay, kaliwakamay[0],
                                                 kaliwakamay[1], kaliwakamay[2], kaliwakamay[3], kaliwakamay[4],
                                                 kaliwakamay[5], kaliwakamay[6],
                                                 kaliwabar_list[index][0], kaliwabar_list[index][1],
                                                 kaliwabar_list[index][2], kaliwabar_list[index][3],
                                                 kaliwabar_list[index][4], kaliwabar_list[index][
                                                     5])  # angle1,angle2, limb1,limb2, correct1,correct2, lower1, lower2

                kanankamay = detector.findAngle(frame, 11, 13, 15)
                angle_kanankamay = detector.Angle(frame, 23, 11, 13)

                kananbar = detector.Correctpose(frame, angle_kanankamay, kanankamay[0],
                                                kanankamay[1], kanankamay[2], kanankamay[3], kanankamay[4],
                                                kanankamay[5], kanankamay[6],
                                                kananbar_list[index][0], kananbar_list[index][1],
                                                kananbar_list[index][2], kananbar_list[index][3],
                                                kananbar_list[index][4],
                                                kananbar_list[index][
                                                    5])  # angle1,angle2, limb1,limb2, correct1,correct2, lower1, lower2

                kaliwapaa = detector.findAngle(frame, 24, 26, 28)
                angle_kaliwapaa = detector.Angle(frame, 12, 24, 26)

                paakaliwabar = detector.Correctpose(frame, angle_kaliwapaa, kaliwapaa[0],
                                                    kaliwapaa[1], kaliwapaa[2], kaliwapaa[3], kaliwapaa[4],
                                                    kaliwapaa[5], kaliwapaa[6],
                                                    paakaliwabar_list[index][0], paakaliwabar_list[index][1],
                                                    paakaliwabar_list[index][2], paakaliwabar_list[index][3],
                                                    paakaliwabar_list[index][4], paakaliwabar_list[index][
                                                        5])  # angle1,a5gle2, limb1,limb2, correct1,correct2, lower1, lower2

                kananpaa = detector.findAngle(frame, 23, 25, 27)
                angle_kananpaa = detector.Angle(frame, 11, 23, 25)

                paakananbar = detector.Correctpose(frame, angle_kananpaa, kananpaa[0],
                                                   kananpaa[1], kananpaa[2], kananpaa[3], kananpaa[4], kananpaa[5],
                                                   kananpaa[6],
                                                   paakananbar_list[index][0], paakananbar_list[index][1],
                                                   paakananbar_list[index][2], paakananbar_list[index][3],
                                                   paakananbar_list[index][4], paakananbar_list[index][
                                                       5])  # angle1,angle2, limb1,limb2, correct1,correct2, lower1, lower2

                right_chest = detector.findChest(frame, 12, 24, 26, 23, 11)
                left_chestbar = detector.CorrectChest(frame, right_chest[0], right_chest[1], right_chest[2],
                                                      right_chest[3], right_chest[4],
                                                      right_chest[5], right_chest[6],
                                                      right_chest[7], right_chest[8],
                                                      rightchest_list[index][0], rightchest_list[index][1],
                                                      rightchest_list[index][2], rightchest_list[index][3])

                # detector.Left(frame, kaliwakamay[0], angle_kaliwakamay, kanankamay[0], angle_kanankamay, kaliwapaa[0],
                #               angle_kaliwapaa, kananpaa[0], angle_kananpaa, footkaliwa[0], footkanan[0],right_chest[0])

                bartotal = int(kaliwabar or 0) + int(kananbar or 0) + int(paakaliwabar or 0) + int(
                    paakananbar or 0) + int(
                    footkaliwabar or 0) + int(footkananbar or 0) + int(left_chestbar or 0)

                if timeforending > 0:
                    canvas = Canvas(top, height=240, width=420, bg="indigo", highlightthickness=0, borderwidth=0)
                    canvas.pack()
                    canvas.place(x=0, y=480)
                    canvas.create_rectangle(30, 10, 390, 200, outline="#fb0", width=5)  # for rectangle outlline

                    # for changing accuracy rectangle fill and color
                    bargraph = np.interp(bartotal, (0, 100), (30, 387))
                    rectangle = canvas.create_rectangle(33, 13, int(bargraph), 197, fill="green")

                    per = np.interp(bartotal, (0, 100), (0, 100))
                    canvas.create_text(205, 110, anchor=CENTER, text=f'{int(per)}%', fill='white',
                                       font=('Helvetica 15 bold', '100'))

                    if timeforending % total_time + 1 >= total_time + 1 - delay_time:
                        canvas.itemconfig(rectangle, fill='gray')
                    else:
                        detector.Accuracycolor(bartotal, canvas, rectangle)

            else:
                bartotal = 0
                canvas = Canvas(top, height=240, width=420, bg="indigo", highlightthickness=0)
                canvas.pack()
                canvas.place(x=0, y=480)
                canvas.create_rectangle(30, 10, 390, 200, outline="#fb0", width=5)  # for rectangle outlline

                # for changing accuracy rectangle fill and color
                bargraph = np.interp(bartotal, (0, 100), (30, 387))
                rectangle = canvas.create_rectangle(33, 13, int(bargraph), 197, fill="green")

                per = np.interp(bartotal, (0, 100), (0, 100))
                canvas.create_text(205, 110, anchor=CENTER, text=f'{int(per)}%', fill='white',
                                   font=('Helvetica 15 bold', '100'))

            # to get accuracy once per second
            if timeforending % total_time + 1 < total_time + 1 - delay_time and checker == True:
                checker = False
                count[index] += 1
                totalaccuracy[index] += bartotal
                # averageaccuracy = totalaccuracy[index] / count
                # print(timeforending % total_time + 1, count, bartotal, totalaccuracy, int(averageaccuracy))
                print(str(count)+"          "+str(totalaccuracy))

            #     if bartotal < 20:
            #         display_low += 1
            #     else:
            #         display_low = 0
            #
            # if display_low >= 3:
            #     cv2.putText(frame, "Ayusin mo naman", (50, 100), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 255), 3)

            ctime = time.time()
            fps = 1 / (ctime - ptime)
            ptime = ctime
            cv2.putText(frame, str(int(fps)), (780, 70), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 2)

            if timeforending % total_time + 1 == sound_countdown and sound_countdown_bool == True:
                sound_countdown_bool = False
                pygame.mixer.music.load("sounds/timer.mp3")
                pygame.mixer.music.play(loops=0)

            if timeforending % total_time + 1 >= total_time + 1 - delay_time:
                cv2.putText(frame, "Up Next", (30, 280), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 4)
                cv2.putText(frame, poseName[index], (30, 370), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 5)
                cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                sound_countdown_bool = True
            else:
                cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

            img = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)
            lmain.imgtk = imgtk
            lmain.configure(image=imgtk)

            if timeforending > 0:
                lmain.after(10, treePose)

            # for overall accuracy
            else:
                cap.release()
                window.deiconify()
                top.destroy()

                pygame.mixer.music.stop()
                pygame.mixer.Channel(1).stop()

                arr2 = np.divide(totalaccuracy, set_time*numberofloop)

                print(arr2)

                arr3 = []
                for i in arr2:
                    arr3.append(int(i))

                print(arr3)

                k = np.sum(arr3) / numberofyoga

                kabas = [arr3, int(k), items2[2]]

                if items3 == True and items2[1] <= int(k):
                    change_array = '/'.join([str(elem) for elem in arr3])   # update yoga accuracy result

                    print("you are in")
                    global present_account

                    details = present_account[8]
                    data_split = details.split('-')

                    data_split[items2[2]] = change_array  # items2[2] is for index
                    listToStr = '-'.join([str(elem) for elem in data_split])

                    # to update in yoga app
                    present_account = list(present_account)
                    present_account[8] = listToStr



                    #to update in mysql
                    #sql = f"UPDATE yoga_accounts SET user_accuracy = '{listToStr}' WHERE id = '{present_account[0]}'"
                    #mycursor.execute(sql)
                    #mydb.commit()

                retry_frame_container(items, kabas, items3)

        def showvideo():
            image = Image.open(pictures[index])
            img = image.resize((420, 240))
            img = ImageTk.PhotoImage(img)
            panel.configure(image=img)
            panel.image = img

        def clickx():
            cap.release()
            window.deiconify()
            top.destroy()
            pygame.mixer.music.stop()
            pygame.mixer.Channel(1).stop()

        window.withdraw()

        ctime = 0
        ptime = 0

        count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        totalaccuracy = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        averageaccuracy = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        checker = False
        display_low = 0

        sound_countdown = 5
        sound_countdown_bool = True

        countdown(time_s)

        treePose()
        top.protocol("WM_DELETE_WINDOW", clickx)

    def Profile_Frame():
        Change_Frame.tkraise()
        pygame.mixer.Channel(1).stop()
        navigation_home_button.config(command=Home_Frame, image=navigation_home_image)
        navigation_setting_button.config(command=Setting_Frame, image=navigation_setting_image)
        navigation_profile_button.config(command=Profile_Frame, image=clicked_Profileframe_picture)

        for widgets in Change_Frame.winfo_children():
            widgets.destroy()

        def profile_change_password():
            navigation_profile_button.config(image=clicked_Back_picture)
            for widgets in Change_Frame.winfo_children():
                widgets.destroy()

            Label(Change_Frame, image=logo, borderwidth=0).place(x=380, y=10)
            Label(Change_Frame, text="Profile", font=('Book Antiqua', 20,), fg="#7163ba", bg='#f8f2f2').place(x=10,y=15)
            Label(Change_Frame, text="Change Password", font=('Book Antiqua', 21,"bold"), fg="#7163ba", bg='#f8f2f2').place(x=10, y=50)

            def confirm_current_pass():
                if profile_current_pass.get() =="":
                    current_pass_notif.config(text="* field is required")
                    return
                if present_account[2] != profile_current_pass.get():
                    current_pass_notif.config(text="* password is incorrect")
                    return

                current_pass_notif.config(text="* password successfully confirmed",fg="green")
                prof_current_passEntry.config(state=DISABLED,cursor="arrow")
                prof_current_passBtn.config(state=DISABLED,disabledforeground="#C0C0C0",cursor="arrow")

                prof_new_passEntry.config(state=NORMAL,cursor="xterm")
                prof_confirm_passEntry.config(state=NORMAL,cursor="xterm")
                prof_new_passBtn.config(state=NORMAL,cursor="hand2")

            def update_current_pass():
                global present_account

                if profile_new_pass.get() =="" or profile_confirm_pass.get() == "":
                    new_pass_notif.config(text="* all field are required")
                    return
                if profile_confirm_pass.get() != profile_new_pass.get():
                    new_pass_notif.config(text=" * password is not matching")
                    return
                if profile_new_pass.get() == present_account[2]:
                    new_pass_notif.config(text="* must not be the same password")
                    return

                new_pass_notif.config(text="* password successfully updated",fg="green")
                prof_new_passEntry.config(state=DISABLED,cursor="arrow")
                prof_confirm_passEntry.config(state=DISABLED,cursor="arrow")
                prof_new_passBtn.config(state=DISABLED,cursor="arrow")

                present_account = list(present_account)

                present_account[2] = profile_new_pass.get()

                #sql = f"UPDATE yoga_accounts SET password = '{profile_new_pass.get()}' WHERE id = '{present_account[0]}'"
                #mycursor.execute(sql)
                #mydb.commit()

                #to update command // to clear profile password
                navigation_home_button.config(command=lambda: clear_profile_password("home"))
                navigation_setting_button.config(command=lambda: clear_profile_password("setting"))
                navigation_profile_button.config(command=lambda: clear_profile_password("profile"))

            def clear_profile_password(nav):
                profile_current_pass.set("")
                profile_new_pass.set("")
                profile_confirm_pass.set("")

                if nav =="profile":
                    Profile_Frame()
                elif nav =="home":
                    Home_Frame()
                elif nav == "setting":
                    Setting_Frame()

            def show_pass(entry,eye):
                entry.config(show="")
                eye.config(command=lambda:hide_pass(entry,eye), image=hide_pw)

            def hide_pass(entry,eye):
                entry.config(show="*")
                eye.config(command=lambda:show_pass(entry,eye), image=show_pw)

            Label(Change_Frame, text="Current Password:", font=('Book Antiqua', 22,), fg="#7163ba", bg='#f8f2f2').place(x=128, y=200)
            prof_current_passEntry = Entry(Change_Frame, width=30, font=('Book Antiqua', 22), justify=CENTER,textvariable=profile_current_pass,show="*")
            prof_current_passEntry.place(x=400, y=200)
            eye_current_button = Button(Change_Frame, image=show_pw, borderwidth=0, cursor="hand2", command=lambda:show_pass(prof_current_passEntry,eye_current_button))
            eye_current_button.place(x=860,y=200)

            prof_current_passBtn = Button(Change_Frame, text="Confirm", font=('Book Antiqua', 18), fg="#f8f2f2", bg="#7163BA",cursor="hand2",command=confirm_current_pass)
            prof_current_passBtn.place(x=800,y=260)

            current_pass_notif = Label(Change_Frame, text="",font=('Book Antiqua', 20, "italic"), fg="red", bg='#f8f2f2')
            current_pass_notif.place(x=350, y=270)

            Label(Change_Frame, image=profile_line, borderwidth=0).place(x=200, y=350)

            Label(Change_Frame, text="New Password:", font=('Book Antiqua', 22,), fg="#7163ba", bg='#f8f2f2').place(x=166, y=400)
            Label(Change_Frame, text="Confirm Password:", font=('Book Antiqua', 22,), fg="#7163ba", bg='#f8f2f2').place(x=120, y=450)

            prof_new_passEntry = Entry(Change_Frame, width=30, font=('Book Antiqua', 22),textvariable=profile_new_pass, justify=CENTER,state=DISABLED,cursor="arrow",show="*")
            prof_new_passEntry.place(x=400, y=400)
            prof_confirm_passEntry = Entry(Change_Frame, width=30, font=('Book Antiqua', 22),textvariable=profile_confirm_pass, justify=CENTER,state=DISABLED,cursor="arrow",show="*")
            prof_confirm_passEntry.place(x=400, y=450)

            eye_new_button = Button(Change_Frame, image=show_pw, borderwidth=0, cursor="hand2",command=lambda: show_pass(prof_new_passEntry, eye_new_button))
            eye_new_button.place(x=860, y=400)

            prof_new_passBtn = Button(Change_Frame, text="Update", font=('Book Antiqua', 18),command=update_current_pass, fg="#f8f2f2", bg="#7163BA",state=DISABLED,disabledforeground="#C0C0C0")
            prof_new_passBtn.place(x=800,y=510)

            new_pass_notif = Label(Change_Frame, text="",font=('Book Antiqua', 20, "italic"), fg="red", bg='#f8f2f2')
            new_pass_notif.place(x=350, y=520)

        def profile_transanction_history():
            navigation_profile_button.config(image=clicked_Back_picture)
            for widgets in Change_Frame.winfo_children():
                widgets.destroy()

            Label(Change_Frame, image=logo, borderwidth=0).place(x=380, y=10)
            Label(Change_Frame, text="Profile", font=('Book Antiqua', 20,), fg="#7163ba", bg='#f8f2f2').place(x=10,y=15)
            Label(Change_Frame, text="Transaction History", font=('Book Antiqua', 21,"bold"), fg="#7163ba",bg='#f8f2f2').place(x=10, y=50)

            Label(Change_Frame, text="No.", font=('Book Antiqua', 23, "bold"), fg="#7163ba", bg='#f8f2f2').place(x=50,
                                                                                                                 y=200)
            Label(Change_Frame, text="Date Paid", font=('Book Antiqua', 23, "bold"), fg="#7163ba", bg='#f8f2f2').place(
                x=185, y=200)
            Label(Change_Frame, text="Payment Method", font=('Book Antiqua', 23, "bold"), fg="#7163ba",
                  bg='#f8f2f2').place(x=435, y=200)
            Label(Change_Frame, text="Amount", font=('Book Antiqua', 23, "bold"), fg="#7163ba", bg='#f8f2f2').place(
                x=760, y=200)

            Transaction_frame = Frame(Change_Frame)
            Transaction_frame.place(x=50, y=250)

            # kopya ko lang to kaya hindi ko alam
            my_canvas = Canvas(Transaction_frame, width=850, height=400, bg="#f8f2f2", borderwidth=0,
                               highlightthickness=0)
            my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
            my_scrollbar = ttk.Scrollbar(Transaction_frame, orient=VERTICAL, command=my_canvas.yview)
            my_scrollbar.pack(side=RIGHT, fill=Y)
            my_canvas.configure(yscrollcommand=my_scrollbar.set)
            my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
            second_frame = Frame(my_canvas, bg='#f8f2f2')
            my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

            user_transaction = present_account[9]

            user_transaction = user_transaction.split("&")

            history_datepad = []
            history_paymentmethod = []
            history_amount = []

            for i in range(len(user_transaction)):
                k = user_transaction[i].split(",")
                history_datepad.append(k[0])
                history_paymentmethod.append(k[1])
                history_amount.append(k[2])

            len_detail = len(history_datepad)

            for i in range(len_detail):
                len_detail -= 1
                Label(second_frame, text=len_detail + 1, font=('Book Antiqua', 21,), fg="#7163ba", bg='#f8f2f2').grid(
                    row=i, column=0, pady=20, padx=5)
                Label(second_frame, text=f'{history_datepad[i]}', font=('Book Antiqua', 21,), fg="#7163ba",
                      bg='#f8f2f2').grid(row=i, column=1, pady=20, padx=60)
                Label(second_frame, text=f'{history_paymentmethod[i]}', font=('Book Antiqua', 21,), fg="#7163ba",
                      bg='#f8f2f2').grid(row=i, column=2, pady=10, padx=15)
                Label(second_frame, text=f'{history_amount[i]}', font=('Book Antiqua', 21,), fg="#7163ba",
                      bg='#f8f2f2').grid(row=i, column=3, pady=10, padx=95)

        Label(Change_Frame, image=logo, borderwidth=0).place(x=380, y=10)
        Label(Change_Frame, text="Profile", font=('Book Antiqua', 45,), fg="#7163ba", bg='#f8f2f2').place(x=10, y=15)

        Label(Change_Frame,image = change_picture).place(x=30,y=180)
        Label(Change_Frame, text=full_name, font=('Book Antiqua', 30,), fg="#7163ba", bg='#f8f2f2').place(x=120, y=200)

        Label(Change_Frame, image=profile_line, borderwidth=0).place(x=120, y=270)

        Button(Change_Frame, text=">  Change Password", font=('Book Antiqua', 20,), fg="#7163ba", bg='#f8f2f2', borderwidth=0,
               cursor="hand2", command=profile_change_password).place(x=150, y=300)
        Button(Change_Frame, text=">  Payment Option", font=('Book Antiqua', 20,), fg="#7163ba", bg='#f8f2f2',
               borderwidth=0, cursor="hand2",command=profile_payment_option).place(x=150, y=350)
        Button(Change_Frame, text=">  Transaction History", font=('Book Antiqua', 20,), fg="#7163ba", bg='#f8f2f2',
               borderwidth=0, cursor="hand2",command=profile_transanction_history).place(x=150, y=400)

        expiration_date = datetime.datetime.strptime(present_account[6], "%Y-%m-%d").date()

        if date_today <= expiration_date:
            Label(Change_Frame, text="Subscription Until", font=('Book Antiqua', 25,), fg="#7163ba",
                  bg='#f8f2f2').place(x=750, y=10)
            Label(Change_Frame, text=present_account[6], font=('Book Antiqua', 20,), fg="#7163ba", bg='#f8f2f2').place(
                x=820, y=50)
        else:
            Label(Change_Frame, text="Subscription Ended", font=('Book Antiqua', 25,), fg="red",bg='#f8f2f2').place(x=750, y=10)
            Label(Change_Frame, text=present_account[6], font=('Book Antiqua', 20,), fg="red", bg='#f8f2f2').place(x=820, y=50)


        window.mainloop()

    def profile_payment_option():
        navigation_profile_button.config(image=clicked_Back_picture)
        for widgets in Change_Frame.winfo_children():
            widgets.destroy()

        def paymethod_function(event):
            for widgets in b.winfo_children():
                widgets.destroy()

            if paymethod.get() == "Credit/Debit Card":
                Label(b, text="", font=('Book Antiqua', 23), fg="#7163ba", bg='#f8f2f2').grid(row=0, column=0,padx=60)  # for left margin

                Label(b,text="Credit/Debit Card",font=('Book Antiqua', 30,"bold"), fg="#7163ba", bg='#f8f2f2').grid(row=0,column=1,pady=5,columnspan=3)

                Label(b, text="Card Number", font=('Book Antiqua', 23), fg="#7163ba", bg='#f8f2f2').grid(row=1, column=1)
                Label(b, text="Expiration Month", font=('Book Antiqua', 23), fg="#7163ba", bg='#f8f2f2').grid(row=2,column=1)
                Label(b, text="Expiration Year", font=('Book Antiqua', 23), fg="#7163ba", bg='#f8f2f2').grid(row=3,column=1)
                Label(b, text="CVC", font=('Book Antiqua', 23), fg="#7163ba", bg='#f8f2f2').grid(row=4, column=1)

                Label(b, text=":", font=('Book Antiqua', 23), fg="#7163ba", bg='#f8f2f2').grid(row=1,column=2)
                Label(b, text=":", font=('Book Antiqua', 23), fg="#7163ba", bg='#f8f2f2').grid(row=2, column=2)
                Label(b, text=":", font=('Book Antiqua', 23), fg="#7163ba", bg='#f8f2f2').grid(row=3, column=2)
                Label(b, text=":", font=('Book Antiqua', 23), fg="#7163ba", bg='#f8f2f2').grid(row=4, column=2)

                Entry(b, textvariable= cardNumber,font=('Book Antiqua', 18), justify=CENTER, width=20).grid(row=1,column=3,padx=10)
                Entry(b, textvariable= expMonth,font=('Book Antiqua', 18), justify=CENTER, width=8).grid(row=2, column=3, padx=10, sticky=W)
                Entry(b, textvariable= expYear, font=('Book Antiqua', 18), justify=CENTER, width=8).grid(row=3, column=3, padx=10, sticky=W)
                Entry(b, textvariable=cvc, font=('Book Antiqua', 18), justify=CENTER, width=8).grid(row=4, column=3, padx=10, sticky=W)

                submit_btn = Button(b,text="Submit",font=('Book Antiqua', 20),fg="#f8f2f2", bg="#7163BA",command=profile_submit)
                submit_btn.grid(row=5,column=1,columnspan=3,pady=10)


            else:
                Label(b, text="hello", font=('Book Antiqua', 20,), fg="#7163ba", bg='#f8f2f2').grid(row=0, column=0)

        Label(Change_Frame, image=logo, borderwidth=0).place(x=380, y=10)
        Label(Change_Frame, text="Profile", font=('Book Antiqua', 20,), fg="#7163ba", bg='#f8f2f2').place(x=10, y=15)
        Label(Change_Frame, text="Payment Option", font=('Book Antiqua', 21,"bold"), fg="#7163ba", bg='#f8f2f2').place(x=10,y=50)

        packFrame = Frame(Change_Frame,width=1040,height=400,bg="#f8f2f2")
        packFrame.place(x=0,y=200)

        a = Frame(packFrame,bg='#f8f2f2')
        a.pack()
        b = Frame(packFrame, bg='#f8f2f2')
        b.pack(pady=20)

        Label(a, text="", font=('Book Antiqua', 23), fg="#7163ba", bg='#f8f2f2').grid(row=0, column=0,padx=50) #for left margin

        Label(a, text="Select Plan", font=('Book Antiqua', 23), fg="#7163ba", bg='#f8f2f2').grid(row=0,column=1,)
        Label(a, text="Payment Method", font=('Book Antiqua', 23), fg="#7163ba", bg='#f8f2f2').grid(row=1, column=1,)

        Label(a, text=":", font=('Book Antiqua', 23), fg="#7163ba", bg='#f8f2f2').grid(row=0, column=2)
        Label(a, text=":", font=('Book Antiqua', 23), fg="#7163ba", bg='#f8f2f2').grid(row=1, column=2)

        amount_choosen = ttk.Combobox(a, width=27, font=('Book Antiqua', 20), state="readonly",textvariable=plan_ammount)
        amount_choosen['values'] = ("₱200 for 7 days", "₱600 for 30 days")
        amount_choosen.grid(row=0, column=3, padx=10)

        paymethod_choosen = ttk.Combobox(a, width=27, font=('Book Antiqua', 20), state="readonly",textvariable=paymethod)
        paymethod_choosen['values'] = ("Credit/Debit Card", "GCash")
        paymethod_choosen.grid(row=1, column=3, padx=10)

        paymethod_function(0)
        paymethod_choosen.bind("<<ComboboxSelected>>", paymethod_function)

        font = ("Book Antiqua", 18)
        window.option_add("*TCombobox*Listbox.font", font)

    def profile_submit():
        navigation_profile_button.config(image=clicked_Back_picture)
        for widgets in Change_Frame.winfo_children():
            widgets.destroy()

        Label(Change_Frame, image=logo, borderwidth=0).place(x=380, y=10)
        Label(Change_Frame, text="Profile", font=('Book Antiqua', 20,), fg="#7163ba", bg='#f8f2f2').place(x=10, y=15)
        Label(Change_Frame, text="Payment Option", font=('Book Antiqua', 21, "bold"), fg="#7163ba", bg='#f8f2f2').place(x=10, y=50)


        def profile_confirm():

            paymentIntentResult = createPaymentIntent(100 * 100)
            paymentMethodResult = createPaymentMethod(cardNumber.get(),int(expMonth.get()),int(expYear.get()),
                                                      cvc.get(), full_name, "test@gmail.com", "0", "0", "0", "0", "0", "0")

            attachPaymentResult = PaymentIntent(paymentIntentResult, paymentMethodResult)

            if attachPaymentResult == 'succeeded':
                if plan_ammount.get() == "₱200 for 7 days":
                    success_text = "Your subscription date has been extended by seven days."
                else:
                    success_text = "Your subscription date has been extended by 30 days."

                messagebox.showinfo("Payment Succeed",success_text )
                Profile_Frame()

            else:
                messagebox.showerror("Payment Failed", attachPaymentResult)

        packFrame = Frame(Change_Frame, width=1040, height=400, bg="#f8f2f2")
        packFrame.place(x=0, y=165)

        a = Frame(packFrame, bg='#f8f2f2')
        a.pack()

        Label(a, text="", font=('Book Antiqua', 23), fg="#7163ba", bg='#f8f2f2').grid(row=0, column=0)  # for left margin

        Label(a, text="Payment For", font=('Book Antiqua', 20,"bold"), fg="#7163ba", bg='#f8f2f2').grid(row=0, column=1,columnspan=3)

        Label(a, text="Description", font=('Book Antiqua', 18), fg="#7163ba", bg='#f8f2f2').grid(row=1, column=1, )
        Label(a, text="Selcct Plan", font=('Book Antiqua', 18), fg="#7163ba", bg='#f8f2f2').grid(row=2, column=1, )
        Label(a, text="Payment Method", font=('Book Antiqua', 18), fg="#7163ba", bg='#f8f2f2').grid(row=3, column=1, )

        Label(a, text=":", font=('Book Antiqua', 18), fg="#7163ba", bg='#f8f2f2').grid(row=1, column=2)
        Label(a, text=":", font=('Book Antiqua', 18), fg="#7163ba", bg='#f8f2f2').grid(row=2, column=2)
        Label(a, text=":", font=('Book Antiqua', 18), fg="#7163ba", bg='#f8f2f2').grid(row=3, column=2)

        Label(a, text="Yoga With LeAnne", font=('Book Antiqua', 18), fg="#7163ba", bg='#f8f2f2').grid(row=1, column=3)
        Label(a, text=plan_ammount.get(), font=('Book Antiqua', 18), fg="#7163ba", bg='#f8f2f2').grid(row=2, column=3, )
        Label(a, text=paymethod.get(), font=('Book Antiqua', 18), fg="#7163ba", bg='#f8f2f2').grid(row=3, column=3,)

        b = Frame(packFrame, bg='#f8f2f2')
        b.pack()
        Label(b, text="", font=('Book Antiqua', 23), fg="#7163ba", bg='#f8f2f2').grid(row=0, column=0)  # for left margin
        Label(b, text="Billing Details", font=('Book Antiqua', 18, "bold"), fg="#7163ba", bg='#f8f2f2').grid(row=0,column=1)

        c = Frame(packFrame, bg='#f8f2f2')
        c.pack()
        Label(c, text="", font=('Book Antiqua', 18), fg="#7163ba", bg='#f8f2f2').grid(row=0, column=0)

        Label(c, text="Name", font=('Book Antiqua', 18), fg="#7163ba", bg='#f8f2f2').grid(row=0, column=1)
        Label(c, text="Email", font=('Book Antiqua', 18), fg="#7163ba", bg='#f8f2f2').grid(row=1, column=1, )
        Label(c, text="Card Number", font=('Book Antiqua', 18), fg="#7163ba", bg='#f8f2f2').grid(row=2, column=1, )
        Label(c, text="Expiration Month", font=('Book Antiqua', 18), fg="#7163ba", bg='#f8f2f2').grid(row=3, column=1, )
        Label(c, text="Expiration Year", font=('Book Antiqua', 18), fg="#7163ba", bg='#f8f2f2').grid(row=4, column=1, )
        Label(c, text="CVC", font=('Book Antiqua', 18), fg="#7163ba", bg='#f8f2f2').grid(row=5, column=1, )

        Label(c, text=":", font=('Book Antiqua', 18), fg="#7163ba", bg='#f8f2f2').grid(row=0, column=2)
        Label(c, text=":", font=('Book Antiqua', 18), fg="#7163ba", bg='#f8f2f2').grid(row=1, column=2)
        Label(c, text=":", font=('Book Antiqua', 18), fg="#7163ba", bg='#f8f2f2').grid(row=2, column=2)
        Label(c, text=":", font=('Book Antiqua', 18), fg="#7163ba", bg='#f8f2f2').grid(row=3, column=2)
        Label(c, text=":", font=('Book Antiqua', 18), fg="#7163ba", bg='#f8f2f2').grid(row=4, column=2)
        Label(c, text=":", font=('Book Antiqua', 18), fg="#7163ba", bg='#f8f2f2').grid(row=5, column=2)

        Label(c, text=full_name, font=('Book Antiqua', 18), fg="#7163ba", bg='#f8f2f2').grid(row=0, column=3)
        Label(c, text=present_account[1], font=('Book Antiqua', 18), fg="#7163ba", bg='#f8f2f2').grid(row=1, column=3, )
        Label(c, text=cardNumber.get(), font=('Book Antiqua', 18), fg="#7163ba", bg='#f8f2f2').grid(row=2,column=3, )
        Label(c, text=expMonth.get(), font=('Book Antiqua', 18), fg="#7163ba", bg='#f8f2f2').grid(row=3, column=3)
        Label(c, text=expYear.get(), font=('Book Antiqua', 18), fg="#7163ba", bg='#f8f2f2').grid(row=4, column=3, )
        Label(c, text=cvc.get(), font=('Book Antiqua', 18), fg="#7163ba", bg='#f8f2f2').grid(row=5, column=3, )


        d = Frame(packFrame, bg='#f8f2f2')
        d.pack()
        Button(d, text="Back", font=('Book Antiqua', 18), fg="#f8f2f2", bg="#7163BA", cursor="hand2",command=profile_payment_option).grid(row=0, column=1,ipadx=10,padx=150,sticky=W)
        Button(d, text="Confirm", font=('Book Antiqua', 18), fg="#f8f2f2", bg="#7163BA", cursor="hand2",command=profile_confirm).grid(row=0,column=2,padx=200,sticky=E)

    def Home_Frame():
        Change_Frame.tkraise()
        pygame.mixer.Channel(1).stop()
        navigation_home_button.config(command=Home_Frame, image=clicked_Homeframe_picture)
        navigation_setting_button.config(command=Setting_Frame, image=navigation_setting_image)
        navigation_profile_button.config(command=Profile_Frame, image=navigation_profile_image)

        for widgets in Change_Frame.winfo_children():
            widgets.destroy()

        def get_certificate():
            full_name = f"{present_account[3]} {present_account[4]} {present_account[5]}"
            yoga_cert.create_cert(full_name)

        strength_details = present_account[8].split('-')

        strength_easy_accuracy = get_accuracy.details(strength_details,0)
        strength_medium_accuracy = get_accuracy.details(strength_details,1)
        strength_hard_accuracy = get_accuracy.details(strength_details,2)

        balance_easy_accuracy = get_accuracy.details(strength_details,3)
        balance_medium_accuracy = get_accuracy.details(strength_details,4)
        balance_hard_accuracy = get_accuracy.details(strength_details,5)

        flexibility_easy_accuracy = get_accuracy.details(strength_details,6)
        flexibility_medium_accuracy = get_accuracy.details(strength_details,7)
        flexibility_hard_accuracy = get_accuracy.details(strength_details,8)

        record_accuracy = True

        # Photo Label
        Label(Change_Frame, text="Home", font=('Book Antiqua', 45,), fg="#7163ba", bg='#f8f2f2').place(x=10, y=15)
        Label(Change_Frame, image=strengthContainer, borderwidth=0).place(x=5, y=200)
        Label(Change_Frame, image=balanceContainer, borderwidth=0).place(x=265, y=200)
        Label(Change_Frame, image=flexContainer, borderwidth=0).place(x=525, y=200)
        Label(Change_Frame, image=reportContainer, borderwidth=0).place(x=785, y=180)
        Label(Change_Frame, image=logo, borderwidth=0).place(x=380, y=10)

        # Session Level Label

        tkinter_design.home_button(Change_Frame, "Easy", strength_easy_accuracy[1], retry_frame_container,
                                   strength_easylist, strength_easy_accuracy, record_accuracy, 40, 300, 200, 320, 40,
                                   350)
        sm = tkinter_design.home_button(Change_Frame, "Medium", strength_medium_accuracy[1], retry_frame_container,
                                        strength_mediumlist, strength_medium_accuracy, record_accuracy, 40, 378, 200,
                                        398, 40, 428)
        sh = tkinter_design.home_button(Change_Frame, "Hard", strength_hard_accuracy[1], retry_frame_container,
                                        strength_hardlist, strength_hard_accuracy, record_accuracy, 40, 456, 200, 476,
                                        40, 506)

        tkinter_design.home_button(Change_Frame, "Easy", balance_easy_accuracy[1], retry_frame_container,
                                   balance_easylist, balance_easy_accuracy, record_accuracy, 300, 300, 460, 320, 300,
                                   350)
        bm = tkinter_design.home_button(Change_Frame, "Medium", balance_medium_accuracy[1], retry_frame_container,
                                        balance_mediumlist, balance_medium_accuracy, record_accuracy, 300, 378, 460,
                                        390, 300, 428)
        bh = tkinter_design.home_button(Change_Frame, "Hard", balance_hard_accuracy[1], retry_frame_container,
                                        balance_hardlist, balance_hard_accuracy, record_accuracy, 300, 456, 460, 476,
                                        300, 506)

        tkinter_design.home_button(Change_Frame, "Easy", flexibility_easy_accuracy[1], retry_frame_container,
                                   flexibility_easylist, flexibility_easy_accuracy, record_accuracy, 560, 300, 720, 320,
                                   560, 350)
        fm = tkinter_design.home_button(Change_Frame, "Medium", flexibility_medium_accuracy[1], retry_frame_container,
                                        flexibility_mediumlist, flexibility_medium_accuracy, record_accuracy, 560, 378,
                                        720, 390, 560, 428)
        fh = tkinter_design.home_button(Change_Frame, "Hard", flexibility_hard_accuracy[1], retry_frame_container,
                                        flexibility_hardlist, flexibility_hard_accuracy, record_accuracy, 560, 456, 720,
                                        476, 560, 506)

        # Disable buttons
        tkinter_design.home_disable_button(sm, sh, strength_easy_accuracy[1], strength_medium_accuracy[1],
                                           bm, bh, balance_easy_accuracy[1], balance_medium_accuracy[1],
                                           fm, fh, flexibility_easy_accuracy[1], flexibility_medium_accuracy[1])

        strength_all_progress = int(
            (strength_easy_accuracy[1] + strength_medium_accuracy[1] + strength_hard_accuracy[1]) / 3)
        balance_all_progress = int(
            (balance_easy_accuracy[1] + balance_medium_accuracy[1] + balance_hard_accuracy[1]) / 3)
        flexibility_all_progress = int(
            (flexibility_easy_accuracy[1] + flexibility_medium_accuracy[1] + flexibility_hard_accuracy[1]) / 3)

        tkinter_design.home_progress_label(Change_Frame, strength_all_progress, 80, 545, 200, 550, 40, 574)
        tkinter_design.home_progress_label(Change_Frame, balance_all_progress, 340, 545, 460, 550, 300, 574)
        tkinter_design.home_progress_label(Change_Frame, flexibility_all_progress, 600, 545, 720, 550, 560, 574)

        # Overall Progress
        overall_progress = int((strength_all_progress + balance_all_progress + flexibility_all_progress) / 3)

        Label(Change_Frame, text=f'{overall_progress}%', font=('Book Antiqua', 23, "bold"), bg="white").place(x=900,y=290)
        ttk.Progressbar(Change_Frame, orient='horizontal', mode='determinate', length=200,
                        value=overall_progress).place(x=824, y=330)

        certicate_btn = Button(Change_Frame, text="Get Certificate", font=('Book Antiqua', 15),fg="#f8f2f2", bg="#7163BA", cursor="hand2",command=get_certificate)
        certicate_btn.place(x=850,y=363)

        if overall_progress < 84:
            certicate_btn.config(state=DISABLED,disabledforeground="#C0C0C0",cursor="arrow")
            ToolTip(certicate_btn, msg="You are an idiot",fg='red', font=('Book Antiqua', 11))

        # overall tries
        user_tries = present_account[7].split("/")
        user_tries_overall = int(user_tries[0]) + int(user_tries[1]) + int(user_tries[2])
        user_tries_text= f"Str-{user_tries[0]}    Bal-{user_tries[1]}    Flx-{user_tries[2]}"

        Label(Change_Frame, text=user_tries_overall, font=('Book Antiqua', 25,"bold"), bg="white").place(x=915, y=535)
        Label(Change_Frame, text=user_tries_text, font=('Book Antiqua', 15,), bg="white").place(x=835, y=580)

        window.mainloop()

    def Setting_Frame():
        Change_Frame.tkraise()
        pygame.mixer.Channel(1).stop()
        navigation_home_button.config(command=Home_Frame, image=navigation_home_image)
        navigation_setting_button.config(command=Setting_Frame, image=clicked_Settingframe_picture)
        navigation_profile_button.config(command=Profile_Frame, image=navigation_profile_image)

        for widgets in Change_Frame.winfo_children():
            widgets.destroy()

        # Label
        Label(Change_Frame, text="Settings", font=('Book Antiqua', 45,), fg="#7163ba", bg='#f8f2f2').place(x=10, y=15)
        Label(Change_Frame, image=logo, borderwidth=0).place(x=380, y=10)
        Label(Change_Frame, text="Detection", font=('Book Antiqua', 25,), fg="#7163ba", bg='#f8f2f2').place(x=200,
                                                                                                            y=360)
        Label(Change_Frame, text="Music", font=('Book Antiqua', 25,), fg="#7163ba", bg='#f8f2f2').place(x=580, y=360)

        # Button
        Button(Change_Frame, image=detection_setting_image, borderwidth=0, cursor="hand2",
               command=setting_detection).place(x=200, y=200)
        Button(Change_Frame, image=music_setting_image, borderwidth=0, cursor="hand2", command=setting_music).place(
            x=550, y=200)
        window.mainloop()

    def setting_detection():
        navigation_setting_button.config(image=clicked_Back_picture)
        for widgets in Change_Frame.winfo_children():
            widgets.destroy()

        Label(Change_Frame, text="Setting", font=('Book Antiqua', 20,), fg="#7163ba", bg='#f8f2f2').place(x=10, y=15)
        Label(Change_Frame, text="Detection", font=('Book Antiqua', 30,), fg="#7163ba", bg='#f8f2f2').place(x=10, y=50)

        lmain = Label(Change_Frame, borderwidth=0, image=camera_label, width=840, height=680, )
        lmain.place(x=200, y=10)

        def change_detector_color(complex):
            global detector
            global color
            if complex == 0:
                color = [0, 255, 0]
                lite_btn.config(image=active_radiobutton)
                full_btn.config(image=inactive_radiobutton)
                heavy_btn.config(image=inactive_radiobutton)
            elif complex == 1:
                color = [255, 0, 0]
                lite_btn.config(image=inactive_radiobutton)
                full_btn.config(image=active_radiobutton)
                heavy_btn.config(image=inactive_radiobutton)
            elif complex == 2:
                color = [0, 0, 255]
                lite_btn.config(image=inactive_radiobutton)
                full_btn.config(image=inactive_radiobutton)
                heavy_btn.config(image=active_radiobutton)

            detector = pm.poseDetector(complex=complex)

            with open('setting.txt', 'r+') as file:
                file_data = file.read()
                details = file_data.split('\n')
                setting_name = details[0]
                setting_name_except_LastChar = setting_name[:-1]

                option_update = str(detector.complex)

                file_data = file_data.replace(setting_name, setting_name_except_LastChar + option_update)
                file.seek(0)
                file.truncate(0)
                file.write(file_data)

        def closeCamera_setting(navigation):
            global close_camera
            close_camera = True
            navigation_setting_button.config(command=Setting_Frame)  # para mabilis ulit ang paglipat
            navigation_home_button.config(command=Home_Frame)

            # if int(lastsave_detection) != detector.complex:
            #    with open('setting.txt', 'r+') as file:
            #        print("save")
            #        file_data = file.read()
            #        details = file_data.split('\n')
            #        setting_name = details[0]
            #        setting_name_except_LastChar = setting_name[:-1]
            #
            #        option_update = str(detector.complex)
            #
            #        file_data = file_data.replace(setting_name, setting_name_except_LastChar + option_update)
            #        file.seek(0)
            #        file.truncate(0)
            #        file.write(file_data)

            if navigation == 1:
                window.after(500, Home_Frame)
            elif navigation == 2:
                window.after(500, Setting_Frame)  # need ng delay para mapatay ang cam light
            elif navigation == 3:
                window.after(500, Profile_Frame)

        def change_function_navigation_buttons():
            global cap
            cap = cv2.VideoCapture(0)
            user_camera_button.destroy()
            navigation_home_button.config(command=lambda: closeCamera_setting(1))
            navigation_setting_button.config(command=lambda: closeCamera_setting(2))
            # navigation_profile_button.config(command=lambda: closeCamera_setting(3))
            user_cam()

        def user_cam():
            global close_camera
            global color

            _, frame = cap.read()
            frame = cv2.flip(frame, 1)
            frame = cv2.resize(frame, (840, 680))

            frame = detector.findPose(frame, False)
            lmlist = detector.findPosition(frame, False)

            if len(lmlist) != 0:
                detector.findAllAngle(frame, 16, 14, 12, 24, 26, 28, 32, 15, 13, 11, 23, 25, 29, 31, color[0],
                                      color[1], color[2])

            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

            img = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)
            lmain.imgtk = imgtk
            lmain.configure(image=imgtk)

            if close_camera == True:
                cap.release()
            else:
                lmain.after(10, user_cam)

        lite_btn = Button(Change_Frame, image=inactive_radiobutton, borderwidth=0, cursor="hand2",
                          command=lambda: change_detector_color(0))
        lite_btn.place(x=30, y=130)
        full_btn = Button(Change_Frame, image=inactive_radiobutton, borderwidth=0, cursor="hand2",
                          command=lambda: change_detector_color(1))
        full_btn.place(x=30, y=280)
        heavy_btn = Button(Change_Frame, image=inactive_radiobutton, borderwidth=0, cursor="hand2",
                           command=lambda: change_detector_color(2))
        heavy_btn.place(x=30, y=430)

        Label(Change_Frame, text="Low", font=('Book Antiqua', 20,), fg="#7163ba", bg='#f8f2f2').place(x=30, y=180)
        Label(Change_Frame, text="Medium", font=('Book Antiqua', 20,), fg="#7163ba", bg='#f8f2f2').place(x=5, y=330)
        Label(Change_Frame, text="High", font=('Book Antiqua', 20,), fg="#7163ba", bg='#f8f2f2').place(x=30, y=480)
        # command = change_function_navigation_buttons
        user_camera_button = Button(Change_Frame, image=camera_icon, borderwidth=0, highlightthickness=0, cursor="hand2",
                                    command=change_function_navigation_buttons)
        user_camera_button.place(x=330, y=80)

        # to select the last save camera detection
        with open('setting.txt', 'r+') as file:
            file_data = file.read()
            details = file_data.split('\n')
            setting_name = details[0]
            lastsave_detection = setting_name[-1]

        # to call last save detection and button
        change_detector_color(int(lastsave_detection))

        global close_camera

        close_camera = False

        window.mainloop()

    def setting_music():
        navigation_setting_button.config(image=clicked_Back_picture)
        for widgets in Change_Frame.winfo_children():
            widgets.destroy()
        # Label
        Label(Change_Frame, text="Setting", font=('Book Antiqua', 20,), fg="#7163ba", bg='#f8f2f2').place(x=10, y=15)
        Label(Change_Frame, text="Music", font=('Book Antiqua', 30,), fg="#7163ba", bg='#f8f2f2').place(x=10, y=50)

        def play_song():
            Change_Frame.tkraise()
            item = song_box.curselection()
            item = item[0]
            global playing_music
            playing_music = item
            pygame.mixer.Channel(1).play(pygame.mixer.Sound(song_path[item]), loops=-1)

        def add_song():
            Change_Frame.tkraise()
            global song_path
            global song_name
            song = filedialog.askopenfilenames(title="Choose a Song", filetypes=(("mp3 Files", "*.mp3"),))

            for song in song:
                navigation_home_button.config(command=lambda: change_config("home"))
                navigation_setting_button.config(command=lambda: change_config("setting"))
                name = song.split("/")
                name = name[-1]
                name = name.split(".")
                # print(f'{name[0]},{song}')
                song_box.insert(END, name[0])
                song_name.append(name[0])
                song_path.append(song)
                # print(song_path)
                # print(song_name)

        def select_song():
            Change_Frame.tkraise()
            global song_select
            song = song_box.curselection()
            index = song[0]

            if index != song_select:
                navigation_home_button.config(command=lambda: change_config("home"))
                navigation_setting_button.config(command=lambda: change_config("setting"))

                # to select song
                song_name = (song_box.get(index))
                song_box.delete(index)
                song_box.insert(index, f'{song_name}    (SELECTED)')
                song_box.selection_set(index, last=None)

                # to deselect song
                deselect_song = (song_box.get(song_select))
                deselect_song = deselect_song.split("    ")
                song_box.delete(song_select)
                song_box.insert(song_select, deselect_song[0])

                # to change song_select
                song_select = index

        def remove_song():
            def yes_remove_song():
                navigation_home_button.config(command=lambda: change_config("home"))
                navigation_setting_button.config(command=lambda: change_config("setting"))

                song_box.delete(item)
                song_path.pop(item)
                song_name.pop(item)

                pygame.mixer.Channel(1).stop()
                Change_Frame.tkraise()

                # to minus the select song
                global song_select
                if song_select > item:
                    song_select -= 1

            global song_path
            global song_name
            global playing_music

            item = song_box.curselection()
            item = item[0]

            for widgets in option_music_frame.winfo_children():
                widgets.destroy()

            option_music_frame.tkraise()
            Label(option_music_frame, image=option_image, borderwidth=0).place(x=0, y=0)

            if item <= 3:
                Label(option_music_frame, bg='#f8f2f2').pack(pady=5)
                text = "This is a default song. Cannot remove."
                Label(option_music_frame, text=text, font=('Book Antiqua', 16,), bg='#f8f2f2').pack(pady=11, padx=19)
                Button(option_music_frame, text="Okay", font=('Book Antiqua', 14),
                       command=lambda: Change_Frame.tkraise()).pack(pady=13)

            elif item == song_select:
                Label(option_music_frame, bg='#f8f2f2').pack(pady=5)
                text = "This is the selected song. Cannot remove."
                Label(option_music_frame, text=text, font=('Book Antiqua', 15,)).pack(pady=11, padx=12)
                Button(option_music_frame, text="Okay", font=('Book Antiqua', 14),
                       command=lambda: Change_Frame.tkraise()).pack(pady=13)
            else:
                Label(option_music_frame, bg='#f8f2f2').grid(row=0, column=0, pady=5)
                Label(option_music_frame, text="Are you sure you want to delete it?", font=('Book Antiqua', 16,)).grid(
                    pady=10, padx=34, columnspan=3, row=1, column=0)
                Button(option_music_frame, text="Yes", font=('Book Antiqua', 14), command=yes_remove_song).grid(row=2,
                                                                                                                column=0,
                                                                                                                pady=14,
                                                                                                                ipadx=13,
                                                                                                                padx=50)
                Button(option_music_frame, text="Cancel", font=('Book Antiqua', 14),
                       command=lambda: Change_Frame.tkraise()).grid(row=2, column=1, pady=14)

        def rename_song():
            def change_raise():
                song_rename_string = song_rename.get()
                name = song_box.get(index)

                if song_rename_string == "":
                    text = "Field is required"
                    notif_label.config(text=text)
                    return
                if song_rename_string == name:
                    text = "Same song name, try again"
                    notif_label.config(text=text)
                    return

                Change_Frame.tkraise()
                navigation_home_button.config(command=lambda: change_config("home"))
                navigation_setting_button.config(command=lambda: change_config("setting"))

                song_box.delete(index)
                song_box.insert(index, song_rename_string)
                song_box.selection_set(index, last=None)

                global song_name
                song_name.pop(index)
                song_name.insert(index, song_rename_string)

            def limit_characters(*args):
                value = song_rename.get()
                if len(value) > 15: song_rename.set(value[:15])

            index = song_box.curselection()
            index = index[0]

            for widgets in option_music_frame.winfo_children():
                widgets.destroy()

            option_music_frame.tkraise()
            Label(option_music_frame, image=option_image, borderwidth=0).place(x=0, y=0)

            if index <= 3:
                Label(option_music_frame, bg='#f8f2f2').pack(pady=5)
                text = "This is a default song. Cannot rename."
                Label(option_music_frame, text=text, font=('Book Antiqua', 16,)).pack(pady=11, padx=19)
                Button(option_music_frame, text="Okay", font=('Book Antiqua', 14), command=Change_Frame.tkraise).pack(
                    pady=13)
            elif index == song_select:
                Label(option_music_frame, bg='#f8f2f2').pack(pady=5)
                text = "This is the selected song. Cannot rename."
                Label(option_music_frame, text=text, font=('Book Antiqua', 15,)).pack(pady=11, padx=12)
                Button(option_music_frame, text="Okay", font=('Book Antiqua', 14), command=Change_Frame.tkraise).pack(
                    pady=13)
            else:
                song_rename = StringVar()
                song_rename.trace('w', limit_characters)

                Label(option_music_frame, text="Rename Song", font=('Book Antiqua', 18, "bold"), bg='#f8f2f2').pack(
                    pady=5)
                Entry(option_music_frame, textvariable=song_rename, width=30, font=('Book Antiqua', 15,)).pack(padx=20)

                notif_label = Label(option_music_frame, text="", font=('Book Antiqua', 13,), fg="red", bg='#f8f2f2',
                                    justify=CENTER)
                notif_label.pack()
                Button(option_music_frame, text="Rename", font=('Book Antiqua', 12,), command=change_raise).pack(
                    padx=62, pady=8, side=LEFT)
                Button(option_music_frame, text="Cancel", font=('Book Antiqua', 12,),
                       command=Change_Frame.tkraise).pack(padx=62, side=RIGHT, ipadx=8)

        def volume(x):
            Change_Frame.tkraise()
            global volume_level
            vlabel['text'] = x
            volume_level = int(x)

            # to change volume meter image
            if int(volume_level) >= 70:
                volume_level_label.config(image=high_song_image)
            elif int(volume_level) >= 40:
                volume_level_label.config(image=mid_song_image)
            elif int(volume_level) >= 1:
                volume_level_label.config(image=low_song_image)
            elif int(volume_level) == 0:
                volume_level_label.config(image=mute_song_image)

            volume_level = volume_level * 0.01
            pygame.mixer.Channel(1).set_volume(volume_level)

        def change_config(change_frame):
            def save_changes(option):
                if option == "yes":
                    with open('setting.txt', 'r+') as file:
                        file_data = file.read()
                        details = file_data.split('\n')

                        # save selected value of music
                        select_song_name = details[1]
                        setting_name_except_LastChar = select_song_name[:-1]
                        select_song_update = str(song_select)
                        file_data = file_data.replace(select_song_name,
                                                      setting_name_except_LastChar + select_song_update)
                        # save selected volume level
                        volume_in_text = details[2]
                        volume_details = volume_in_text.split('_')
                        volume_name = volume_details[0]
                        file_data = file_data.replace(volume_in_text, volume_name + "_" + str(volume_level))

                        # save selected music path name
                        print(song_path[song_select])
                        select_song_path = details[3]
                        select_song_path_update = song_path[song_select]
                        file_data = file_data.replace(select_song_path, select_song_path_update)

                        # global use for user_selected_music
                        global user_selected_music
                        user_selected_music = song_path[song_select]

                        file.seek(0)
                        file.truncate(0)
                        file.write(file_data)

                    with open('user_music.txt', 'w') as file:
                        for a, b in zip(song_name, song_path):
                            file.write(f'{a},{b}\n')
                else:
                    pass

                if change_frame == "home":
                    Home_Frame()
                elif change_frame == "setting":
                    Setting_Frame()

            navigation_home_button.config(command=Home_Frame)  # to set back to normal
            for widgets in option_music_frame.winfo_children():
                widgets.destroy()

            option_music_frame.tkraise()
            Label(option_music_frame, image=option_image, borderwidth=0).place(x=0, y=0)

            Label(option_music_frame, bg='#f8f2f2').grid(row=0, pady=5)
            Label(option_music_frame, text="Do you want to save changes?", font=('Book Antiqua', 19,)).grid(pady=10,
                                                                                                            padx=28,
                                                                                                            row=1,
                                                                                                            column=0,
                                                                                                            columnspan=2)
            Button(option_music_frame, text="Yes", font=('Book Antiqua', 12,),
                   command=lambda: save_changes("yes")).grid(row=2, column=0, ipadx=10)
            Button(option_music_frame, text="No", font=('Book Antiqua', 12,), command=lambda: save_changes("no")).grid(
                pady=14, row=2, column=1, ipadx=10)

        add_song_button = Button(Change_Frame, image=add_song_image, borderwidth=0, highlightthickness=0, cursor="hand2",
                                 command=add_song)
        add_song_button.place(x=900, y=50)
        remove_song_button = Button(Change_Frame, image=remove_song_image, borderwidth=0, highlightthickness=0,cursor="hand2",
                                    command=remove_song)
        remove_song_button.place(x=100, y=290)
        rename_song_button = Button(Change_Frame, image=rename_song_image, borderwidth=0, highlightthickness=0,cursor="hand2",
                                    command=rename_song)
        rename_song_button.place(x=900, y=270)
        select_song_button = Button(Change_Frame, image=select_song_image, borderwidth=0, highlightthickness=0,cursor="hand2",
                                    command=select_song)
        select_song_button.place(x=900, y=320)
        play_song_button = Button(Change_Frame, image=play_song_image, borderwidth=0, highlightthickness=0,cursor="hand2",
                                  command=play_song)
        play_song_button.place(x=430, y=400)

        Song_box_Frame = Frame(Change_Frame, bg="#7163ba")
        Song_box_Frame.place(x=200, y=50)
        song_box = Listbox(Song_box_Frame, bg="#7163ba", fg='white', height=10, width=45, font=('Book Antiqua', 20,), cursor="hand2",
                           selectbackground='violet', activestyle="none")
        song_box.pack(side=LEFT, fill=BOTH)
        scrollbar = Scrollbar(Song_box_Frame)
        scrollbar.pack(side=RIGHT, fill=BOTH)

        song_box.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=song_box.yview)

        with open('setting.txt', 'r+') as file:  # to get the selected song in text
            file_data = file.read()
            details = file_data.split('\n')

            # to get theme number
            global song_select
            setting_name = details[1]
            song_select = setting_name[-1]
            song_select = int(song_select)

            # to get volume data line
            for_volume = details[2]
            volume_details = for_volume.split('_')
            # to get volume number
            volume_number = volume_details[1]
            volume_number = float(volume_number)

        volume_level_label = Label(Change_Frame, image=high_song_image, borderwidth=0, highlightthickness=0)
        volume_level_label.place(x=90, y=500)
        volume_slider = Scale(Change_Frame, from_=0, to=100, orient=HORIZONTAL, bg="#7163ba", command=volume, cursor="hand2",
                              showvalue=False, activebackground="violet", length=550, sliderlength=100)
        volume_slider.set(volume_number * 100)
        volume_slider.place(x=220, y=550)
        vlabel = Label(Change_Frame, text=str(volume_number * 100), fg="#7163ba", font=('Book Antiqua', 45))
        vlabel.place(x=800, y=510)

        global song_name
        global song_path

        song_name = []
        song_path = []

        with open('user_music.txt', 'r+') as file:  # to get the name songs in text
            file_data = file.read()
            song_file = file_data.split('\n')

        song_file = song_file[:-1]  # to remove the last text
        for i in song_file:  # to split song names and their directory paths
            i = i.split(',')
            song_name.append(i[0])
            song_path.append(i[1])

        for idx, song_listbox in enumerate(song_name):  # to display selected song and other songs in the listbox
            if idx == song_select:
                song_box.insert(END, f'{song_listbox}    (SELECTED)')
                song_box.selection_set(idx, last=None)
            else:
                song_box.insert(END, song_listbox)

        Change_Frame.tkraise()

        window.mainloop()

    def leave_yoga():
        for widgets in option_music_frame.winfo_children():
            widgets.destroy()
        Change_Frame.tkraise()
        option_music_frame.tkraise()

        Label(option_music_frame, image=option_image, borderwidth=0).place(x=0, y=0)

        Label(option_music_frame, text="Are you sure you want to leave?", font=('Book Antiqua', 19,)).place(x=15, y=40)
        Button(option_music_frame, text="Yes", font=('Book Antiqua', 12,), width=5,command=Page2).place(x=80, y=100)
        Button(option_music_frame, text="Cancel", font=('Book Antiqua', 12,),
               command=lambda: Change_Frame.tkraise()).place(x=250, y=100)

    Change_Frame = tkinter_design.frame_widgets(Page_frame, 620, 1050, '#f8f2f2', 230, 70) #
    option_music_frame = tkinter_design.frame_widgets(Page_frame, 150, 400, '#bb9dbd', 500, 200)
    retry_Frame = tkinter_design.frame_widgets(Page_frame, 550, 900, 'red', 270, 100)

    Navigation_Frame = tkinter_design.frame_widgets(Page_frame, 550, 150, '#7163ba', 70, 100)

    navigation_profile_button = tkinter_design.navigation_buttons(Navigation_Frame, navigation_profile_image,
                                                                  Profile_Frame, 0, 0)
    navigation_setting_button = tkinter_design.navigation_buttons(Navigation_Frame, navigation_setting_image,
                                                                  Setting_Frame, 0, 150)
    navigation_home_button = tkinter_design.navigation_buttons(Navigation_Frame, navigation_home_image, Home_Frame, 0,
                                                               250)
    navigation_exit_button = tkinter_design.navigation_buttons(Navigation_Frame, navigation_exit_image, leave_yoga, 0,
                                                               450)

    expiration_date = datetime.datetime.strptime(present_account[6], "%Y-%m-%d").date()

    if date_today <= expiration_date:
        Home_Frame()

    else:
        disable_home_lbl = Label(Navigation_Frame, image=disable_home_image, borderwidth=0)
        disable_home_lbl.place(x=0, y=250)
        ToolTip(disable_home_lbl, msg="Pay to play", anchor=CENTER, fg='red', font=('Book Antiqua', 11))
        Profile_Frame()
    # Profile_Frame()


def Page2():
    for widgets in Page_frame.winfo_children():
        widgets.destroy()

    Background_Frame = Frame(Page_frame)
    Background_Frame.place(x=0, y=0)
    Label(Background_Frame, image=bG_image2, borderwidth=0).pack()

    global users_mysql
    #mycursor.execute('SELECT * FROM yoga_accounts')
    #users_mysql = mycursor.fetchall()

    def log_in():
        if emailAddress_entry.get() == "" or password_entry.get() == "":
            warning_notif.config(text="All field are required")
            return

        #for user in users_mysql:
            #if emailAddress_entry.get() == user[1]:
                #if password_entry.get() == user[2]:

                    #global present_account
                    #present_account = user

                    #global full_name
                    #full_name = f"{present_account[3]} {present_account[4]} {present_account[5]}"
                    #Page1()

                    #break

                #else:
                    #warning_notif.config(text="Incorrect password")
                    #break
        else:
            warning_notif.config(text="Email address does not exist")

    def show_pass():
        entry_pass.config(show="")
        eye_button.config(command=hide_pass,image=hide_pw)

    def hide_pass():
        entry_pass.config(show="*")
        eye_button.config(command=show_pass,image=show_pw)


    Label(Page_frame, image=logo2, borderwidth=0).pack(pady=60)

    a = Frame(Page_frame,bg="#f8f2f2")
    a.pack()

    Label(a, text="Email Address", font=('Book Antiqua', 25), fg='#7163BA', bg="#f8f2f2").grid(row=0)
    Entry(a, textvariable=emailAddress_entry, font=('Book Antiqua', 15), justify=CENTER, width=40).grid(row=1)
    Label(a, text="Password", font=('Book Antiqua', 25), fg='#7163BA', bg="#f8f2f2").grid(row=2)
    entry_pass = Entry(a, textvariable=password_entry, font=('Book Antiqua', 15), justify=CENTER, width=40,show="*")
    entry_pass.grid(row=3)

    eye_button = Button(a,image=show_pw,borderwidth=0,cursor="hand2",command=show_pass)
    eye_button.grid(row=3,column=1,padx=3,ipadx=3)

    warning_notif = Label(Page_frame, text="", font=('Book Antiqua', 15,"italic"), fg='red', bg="#f8f2f2")
    warning_notif.pack(pady=10)

    Button(Page_frame, text="LOGIN", font=('Book Antiqua', 15), fg="#f8f2f2", bg="#7163BA", cursor="hand2", command=log_in).pack(
        ipadx=10, pady=10)

    def clicker(event):
        Page3()
    register_bind = Label(Page_frame, text="Don't have an Account? Sign-up here.", font=('Book Antiqua', 14, "italic"), fg="#7163BA", bg="#f8f2f2",cursor="hand2")
    register_bind.bind("<Button-1>", clicker)
    register_bind.pack(ipadx=10, pady=10)

    # back end

def Page3(): # register
    for widgets in Page_frame.winfo_children():
        widgets.destroy()

    Background_Frame = Frame(Page_frame)
    Background_Frame.place(x=0, y=0)
    Label(Background_Frame, image=bG_image2, borderwidth=0).pack()

    def register_email():
        for widgets in Page_frame.winfo_children():
            widgets.destroy()

        Background_Frame = Frame(Page_frame)
        Background_Frame.place(x=0, y=0)
        Label(Background_Frame, image=bG_image2, borderwidth=0).pack()

        def valid_reg_email():
            if register_firstname.get() == "" or register_emailaddress.get() == "" or register_lastname.get() == "":
                warning_label.config(text="* must fill all required entries")
                return

            pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            if bool(re.match(pat, register_emailaddress.get())) == False: # for gmail format vaildation
                warning_label.config(text="* invalid email format")
                return

            for i in users_mysql:
                if i[1] ==register_emailaddress.get():
                    warning_label.config(text="* email address has already been used")
                    return

            global verification_number
            verification_number = gmail_verification.check(register_emailaddress.get())

            register_code()

        Label(Page_frame, image=logo2, borderwidth=0).pack(pady=30)

        a = Frame(Page_frame,bg="#f8f2f2")
        a.pack(pady=10)
        Label(a, text = "First Name:",font=('Book Antiqua', 25), fg='#7163BA',bg="#f8f2f2").grid(row=0,column=0,pady=10,sticky=E)
        Label(a, text="Middle Name:",font=('Book Antiqua', 25), fg='#7163BA',bg="#f8f2f2").grid(row=1, column=0,pady=10,sticky=E)
        Label(a, text="Last Name:",font=('Book Antiqua', 25), fg='#7163BA',bg="#f8f2f2").grid(row=2, column=0,pady=10,sticky=E)
        Label(a, text="Email Address:", font=('Book Antiqua', 25), fg='#7163BA', bg="#f8f2f2").grid(row=3, column=0, pady=10,sticky=E)


        Entry(a, width=40, font=('Book Antiqua', 18),justify=CENTER,textvariable=register_firstname).grid(row=0, column=1,padx=10)
        Entry(a, width=40, font=('Book Antiqua', 18),justify=CENTER,textvariable=register_midname).grid(row=1, column=1,padx=10)
        Entry(a, width=40, font=('Book Antiqua', 18),justify=CENTER,textvariable=register_lastname).grid(row=2, column=1,padx=10)
        Entry(a, width=40, font=('Book Antiqua', 18),justify=CENTER,textvariable=register_emailaddress).grid(row=3, column=1,padx=10)

        Label(a, text="*", font=('Book Antiqua', 25), fg='red', bg="#f8f2f2").grid(row=0, column=2)
        Label(a, text="*", font=('Book Antiqua', 25), fg='red', bg="#f8f2f2").grid(row=2, column=2)
        Label(a, text="*", font=('Book Antiqua', 25), fg='red', bg="#f8f2f2").grid(row=3, column=2)

        warning_label = Label(Page_frame, text = "",font=('Book Antiqua', 18,"italic"), fg="red")
        warning_label.pack()

        e = Frame(Page_frame,bg="#f8f2f2")
        e.pack(pady=20)

        Button(e, text="Cancel", font=('Book Antiqua', 20), fg="#f8f2f2", bg="#7163BA",cursor="hand2", command=Page2).grid(row=1, column=0,padx=100)
        Button(e, text="Next", font=('Book Antiqua', 20), fg="#f8f2f2", bg="#7163BA", cursor="hand2",command=valid_reg_email).grid(row=1, column=1,padx=100,ipadx=10)

    def register_code():
        for widgets in Page_frame.winfo_children():
            widgets.destroy()

        Background_Frame = Frame(Page_frame)
        Background_Frame.place(x=0, y=0)
        Label(Background_Frame, image=bG_image2, borderwidth=0).pack()

        Label(Page_frame, image=logo2, borderwidth=0).pack(pady=30)

        def verify_gmail_number():
            if str(verification_number) != verication_number_entry.get():
                warning_label.config(text="* verification number is incorrect")
                return

            register_password()

        def resend_gmail_number():
            global verification_number
            verification_number = gmail_verification.check(register_emailaddress.get())
            print(verification_number)

        print(verification_number)

        a = Frame(Page_frame,bg="#f8f2f2")
        a.pack(pady=10)

        Label(a, text="Verification Code:", font=('Book Antiqua', 25), fg='#7163BA', bg="#f8f2f2").grid(row=0, column=0,pady=10, sticky=E)
        Entry(a, width=15, textvariable=verication_number_entry, font=('Book Antiqua', 18),justify=CENTER).grid(row=0, column=1,padx=10)

        Button(Page_frame, text="Resend Code", font=('Book Antiqua', 15),cursor="hand2", command=resend_gmail_number).pack(pady=10)

        warning_label = Label(Page_frame, text="", font=('Book Antiqua', 18, "italic"),fg="red",bg="#f8f2f2")
        warning_label.pack()

        e = Frame(Page_frame,bg="#f8f2f2")
        e.pack(pady=20)

        Button(e, text="Back", font=('Book Antiqua', 20), fg="#f8f2f2", bg="#7163BA", cursor="hand2",command=register_email).grid(row=1,column=0,padx=100,ipadx=10)
        Button(e, text="Verify", font=('Book Antiqua', 20), fg="#f8f2f2", bg="#7163BA",cursor="hand2", command=verify_gmail_number).grid(row=1,column=1,padx=100)

    def register_password():
        for widgets in Page_frame.winfo_children():
            widgets.destroy()

        Background_Frame = Frame(Page_frame)
        Background_Frame.place(x=0, y=0)
        Label(Background_Frame, image=bG_image2, borderwidth=0).pack()

        def valid_reg_pass():
            if register_createpass.get() == "" or register_confirmpass.get() == "":
                warning_label.config(text="* all fields are required")
                return
            if register_createpass.get() != register_confirmpass.get():
                warning_label.config(text="* password is not matching")
                return

            register_success()

        def show_pass():
            entry_pass.config(show="")
            eye_button.config(command=hide_pass, image=hide_pw)

        def hide_pass():
            entry_pass.config(show="*")
            eye_button.config(command=show_pass, image=show_pw)

        Label(Page_frame, image=logo2, borderwidth=0).pack(pady=30)

        a = Frame(Page_frame,bg="#f8f2f2")
        a.pack(pady=10)
        Label(a, text = "Create Password:",font=('Book Antiqua', 25), fg='#7163BA',bg="#f8f2f2").grid(row=0,column=0,pady=10,sticky=E)
        Label(a, text="Confirm Password:",font=('Book Antiqua', 25), fg='#7163BA',bg="#f8f2f2").grid(row=1, column=0,pady=10,sticky=E)

        entry_pass = Entry(a, width=40, textvariable=register_createpass,font=('Book Antiqua', 18),justify=CENTER, show="*")
        entry_pass.grid(row=0, column=1,padx=10)
        Entry(a, width=40, textvariable=register_confirmpass, font=('Book Antiqua', 18),justify=CENTER, show="*").grid(row=1, column=1,padx=10)

        eye_button = Button(a, image=show_pw, borderwidth=0, cursor="hand2",command=show_pass)
        eye_button.grid(row=0, column=2, padx=3, ipadx=3)

        warning_label = Label(Page_frame, text = "",font=('Book Antiqua', 18,"italic"), fg="red",bg="#f8f2f2")
        warning_label.pack()

        e = Frame(Page_frame,bg="#f8f2f2")
        e.pack(pady=20)

        Button(e, text="Back", font=('Book Antiqua', 20), fg="#f8f2f2", bg="#7163BA", cursor="hand2",command=register_code).grid(row=1, column=0,padx=100,ipadx=20)
        Button(e, text="Confirm", font=('Book Antiqua', 20), fg="#f8f2f2", bg="#7163BA", cursor="hand2",command=valid_reg_pass).grid(row=1, column=1,padx=100)

    def register_success():
        for widgets in Page_frame.winfo_children():
            widgets.destroy()

        Background_Frame = Frame(Page_frame)
        Background_Frame.place(x=0, y=0)
        Label(Background_Frame, image=bG_image2, borderwidth=0).pack()

        Label(Page_frame, image=logo2, borderwidth=0).pack(pady=30)

        Label(Page_frame, text="You have successfully created an account!", font=('Book Antiqua', 35), fg='#7163BA', bg="#f8f2f2").pack(pady=30)
        Button(Page_frame, text="Get Started", font=('Book Antiqua', 20), fg="#f8f2f2", bg="#7163BA", cursor="hand2",command=Page2).pack()


        # for 3 days trial perido
        trial_date = str(date_today)
        trial_date = trial_date.split("-")
        date1 = date(int(trial_date[0]), int(trial_date[1]), int(trial_date[2]))
        date2 = date1 + timedelta(days=3)

        #user_transaction
        num = date_today.month
        split_trans = str(date_today).split("-")
        split_trans[1] = calendar.month_name[num]
        monthname = '-'.join([str(elem) for elem in split_trans])
        monthname = f'{monthname},3-Days Free Trial,₱0'


        #sql = "INSERT INTO yoga_accounts ( email, password, firstname, midname, lastname, expiration, user_try, user_accuracy, user_transaction) " \
              #"VALUES ( %s, %s, %s, %s, %s, %s, %s ,%s, %s)"
        #val = ( register_emailaddress.get(), register_createpass.get(), register_firstname.get(), register_midname.get(),register_lastname.get(),
               #str(date2),"0/0/0", "0/0/0/0/0/0/0/0/0/0-0/0/0/0/0/0/0/0/0/0-0/0/0/0/0/0/0/0/0/0-0/0/0/0/0/0/0/0/0/0-0/0/0/0/0/0/0/0/0/0-0/0/0/0/0/0/0/0/0/0-0/0/0/0/0/0/0/0/0/0-0/0/0/0/0/0/0/0/0/0-0/0/0/0/0/0/0/0/0/0",
               #monthname)

        #mycursor.execute(sql, val)
        #mydb.commit()

        #to clear register entry text
        register_firstname.set("")
        register_midname.set("")
        register_lastname.set("")
        register_emailaddress.set("")
        register_createpass.set("")
        register_confirmpass.set("")
        verication_number_entry.set("")

    register_email()


present_account = []

#Credit Card
cardNumber = StringVar()
expMonth = StringVar()
expYear = StringVar()
cvc = StringVar()

#transaction
plan_ammount = StringVar()
plan_ammount.set("₱200 for 7 days")
paymethod = StringVar()
paymethod.set("Credit/Debit Card")


#profile entry
profile_current_pass = StringVar()
profile_confirm_pass = StringVar()
profile_new_pass = StringVar()

#login entry
emailAddress_entry = StringVar()
password_entry = StringVar()

# registration data
verication_number_entry = StringVar()

register_firstname = StringVar()
register_midname = StringVar()
register_lastname = StringVar()
register_emailaddress = StringVar()

register_createpass = StringVar()
register_confirmpass = StringVar()


# Create a frame
Page_frame = Frame(window)
Page_frame.pack(side="top", expand=True, fill="both")


logo = PhotoImage(file="images/newLogo.png")
logo2 = PhotoImage(file="images/yoga logo.png")
bG_image = PhotoImage(file="images/Bg.png")
bG_image2 = PhotoImage(file="images/BGforsignup.png")

# Photos
navigation_profile_image = PhotoImage(file="images/PROFILE.png")
navigation_home_image = PhotoImage(file="images/HOME2.png")
navigation_setting_image = PhotoImage(file="images/SETTINGS2.png")
navigation_exit_image = PhotoImage(file="images/EXIT2.png")
clicked_Profileframe_picture = PhotoImage(file="images/ProfileHover.png")
clicked_Homeframe_picture = PhotoImage(file="images/home.png")
clicked_Settingframe_picture = PhotoImage(file="images/settings.png")
clicked_Back_picture = PhotoImage(file="images/BACK.png")
disable_home_image = PhotoImage(file="images/HOME3.png")

# Log in
show_pw = PhotoImage(file="images/show_pw.png")
hide_pw = PhotoImage(file="images/hide_pw.png")

# Profile
profile_line = PhotoImage(file="images/profile_line.png")
change_picture = PhotoImage(file="images/change picture.png")
change_pass = PhotoImage(file="images/change pass.png")
view_profile = PhotoImage(file="images/viewProfile.png")
subscription_plan = PhotoImage(file="images/subscription plan.png")

# Home
strengthContainer = PhotoImage(file="images/containerStrength.png")
balanceContainer = PhotoImage(file="images/containerBalance.png")
flexContainer = PhotoImage(file="images/containerFlex.png")
reportContainer = PhotoImage(file="images/reportContainer.png")
bg = PhotoImage(file="images/BGforEndSession.png")

# Setting
music_setting_image = PhotoImage(file="images/newMusic.png")
detection_setting_image = PhotoImage(file="images/newDetection.png")
option_image = PhotoImage(file="images/optionframe.png")

# Setting_detection
camera_label = PhotoImage(file="images/camera_label.png")
camera_icon = PhotoImage(file="images/cam_icon.png")
active_radiobutton = PhotoImage(file="images/radiobutton_active.png")
inactive_radiobutton = PhotoImage(file="images/radiobutton_inactive.png")

# Setting Music
add_song_image = PhotoImage(file="images/addSong.png")
remove_song_image = PhotoImage(file="images/removeSong.png")
rename_song_image = PhotoImage(file="images/renameSong.png")
select_song_image = PhotoImage(file="images/selectSong.png")
play_song_image = PhotoImage(file="images/playSong.png")
mute_song_image = PhotoImage(file="images/newMUTEvolume.png")
low_song_image = PhotoImage(file="images/newLOWvolume.png")
mid_song_image = PhotoImage(file="images/newMIDvloume.png")
high_song_image = PhotoImage(file="images/newHIGHvolume.png")

# Data
strength_easylist = get_data.strength_easylist()
strength_mediumlist = get_data.strength_mediumlist()
strength_hardlist = get_data.strength_hardlist()
balance_easylist = get_data.balance_easylist()
balance_mediumlist = get_data.balance_mediumlist()
balance_hardlist = get_data.balance_hardlist()
flexibility_easylist = get_data.flexibility_easylist()
flexibility_mediumlist = get_data.flexibility_mediumlist()
flexibility_hardlist = get_data.flexibility_hardlist()

Page2()
window.mainloop()