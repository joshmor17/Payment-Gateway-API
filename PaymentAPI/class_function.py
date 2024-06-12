from tkinter import *
import tkinter as tk
from tkinter import ttk
import numpy as np
from tktooltip import ToolTip
import smtplib
import ssl
from email.message import EmailMessage
import random
import re
import cv2
import os
from tkinter import filedialog

class get_accuracy:
    def details(self,present_account,index):
        accuracy_details = present_account[index].split('/')

        yogaaccuracy = []
        yogapercent = []
        for i in accuracy_details:
            yogapercent.append(f"{i}%")
            yogaaccuracy.append(int(i))

        a = np.array(yogaaccuracy)
        b = np.sum(a)
        yogaprogress = int(b / 10)
        index = index

        return yogapercent,yogaprogress, index


class get_data:
    def strength_easylist(self):

        yoganame = ['Tree Pose (Left)', 'Tree Pose (Right)', 'Warrior Pose (Left)', 'Warrior Pose (Right)',
                    'Goddess Pose', 'Trikonasana (Left)', 'Trikonasana (Right)', 'Mountain Pose', 'Half Bending',
                    'Butterfly Pose']

        kaliwabar_list = [[171, 151, 225, 165, 185, 205],  # Tree pose (left)
                          [164, 144, 219, 159, 179, 199],  # Tree pose (Right)
                          [109, 89, 215, 155, 175, 195],  # Warrior pose (left)
                          [96, 76, 214, 154, 174, 194],  # Warrior pose (Right)
                          [111, 91, 285, 225, 245, 265],  # Goddess
                          [85, 65, 201, 151, 171, 191],  # Trikonasana (left)
                          [138, 118, 217, 157, 177, 197],  # Trikonasana (right)
                          [20, 0, 204, 174, 181, 197],  # Mountain Pose
                          [330, 290, 206, 146, 166, 186],  # Half Bending
                          [25, 0, 201, 151, 171, 191]]  # Butterfly Pose

        kananbar_list = [[211, 191, 202, 142, 162, 182],  # Tree pose (left)
                         [215, 195, 202, 142, 162, 182],  # Tree pose(Right)
                         [278, 258, 203, 143, 163, 183],  # Warrior pose (left)
                         [264, 244, 200, 140, 160, 180],  # Warrior pose (Right)
                         [264, 244, 130, 70, 90, 110],  # Goddess pose
                         [252, 232, 196, 136, 156, 176],  # Trikonasana (left)
                         [308, 288, 188, 128, 148, 168],  # Trikonasana (right)
                         [346, 326, 191, 161, 168, 184],  # Mountain Pose
                         [340, 300, 198, 138, 158, 178],  # Half Bending
                         [30, 0, 219, 159, 179, 199]]  # Butterfly pose

        paakaliwabar_list = [[230, 210, 115, 55, 75, 95],  # Tree pose (left)
                             [193, 173, 206, 146, 166, 186],  # Tree pose(Right)
                             [232, 212, 167, 107, 127, 147],  # Warrior pose (left)
                             [214, 194, 219, 159, 179, 199],  # Warrior pose (Right)
                             [262, 242, 138, 78, 98, 118],  # Goddess pose
                             [295, 275, 204, 144, 164, 184],  # Trikonasana (left)
                             [163, 143, 203, 143, 163, 183],  # Trikonasana (right)
                             [196, 176, 193, 163, 170, 186],  # Mountain Pose
                             [114, 74, 217, 167, 187, 207],  # Half Bending
                             [289, 269, 41, 0, 2, 22]]  # Butterfly pose

        paakananbar_list = [[188, 168, 218, 158, 178, 198],  # Tree pose (left)
                            [150, 130, 290, 230, 250, 270],  # Tree pose(Right)
                            [166, 146, 206, 146, 166, 186],  # Warrior pose (left)
                            [138, 118, 258, 198, 218, 238],  # Warrior pose (Right)
                            [114, 94, 288, 228, 248, 268],  # Goddess pose
                            [221, 201, 212, 152, 172, 192],  # Trikonasana (left)
                            [83, 63, 216, 156, 176, 196],  # Trikonasana (right)
                            [185, 165, 196, 166, 173, 189],  # Mountain Pose
                            [123, 83, 212, 152, 172, 192],  # Half Bending
                            [91, 71, 360, 317, 337, 357]]  # Butterfly pose

        kaliwafoot_list = [[266, 206, 216, 256],  # Tree pose (left)
                           [210, 150, 160, 200],  # Tree pose (right)
                           [269, 209, 219, 259],  # Warrior pose (left)
                           [206, 146, 156, 196],  # Warrior pose (right)
                           [287, 227, 237, 277],  # Goddess pose
                           [240, 180, 190, 230],  # Trikonasana (left)
                           [209, 149, 159, 199],  # Trikonasana (right)
                           [236, 176, 186, 226],  # Mountain pose
                           [149, 89, 99, 139],  # Half Bending
                           [205, 145, 155, 195]]  # Butterfly pose

        kananfoot_list = [[218, 158, 168, 208],  # Tree pose (left)
                          [173, 113, 123, 163],  # Tree pose (right)
                          [231, 171, 181, 221],  # Warrior pose (left)
                          [148, 88, 98, 138],  # Warrior pose (right)
                          [146, 86, 96, 136],  # Goddess pose
                          [228, 168, 178, 218],  # Trikonasana (left)
                          [183, 123, 133, 173],  # Trikonasana (right)
                          [185, 125, 135, 175],  # Mountain pose
                          [151, 91, 101, 141],  # Half Bending
                          [219, 159, 169, 209]]  # Butterfly pose

        rightchest_list = [[250, 190, 200, 240],  # Tree pose (left)
                           [213, 153, 163, 203],  # Tree pose(Right)
                           [262, 202, 212, 252],  # Warrior pose (left)
                           [234, 174, 184, 224],  # Warrior pose (Right)
                           [282, 222, 232, 272],  # Goddess pose
                           [315, 255, 265, 305],  # Trikonasana (left)
                           [183, 123, 133, 173],  # Trikonasana (right)
                           [216, 156, 166, 206],  # Mountain Pose
                           [124, 64, 74, 114],  # Half Bending
                           [309, 249, 259, 299]]  # Butterfly

        yogatime = 5
        preparationtime = 5
        loop = 0
        cooldown = 10

        pictures = ["pictures1/p1.jpg", "pictures1/p2.jpg", "pictures1/p3.jpg", "pictures1/p4.jpg", "pictures1/p5.jpg",
                    "pictures1/p6.jpg", "pictures1/p7.jpg", "pictures1/p8.jpg", "pictures1/p9.jpg", "pictures1/p10.jpg"]

        return yoganame ,kaliwabar_list, kananbar_list, paakaliwabar_list, paakananbar_list, kaliwafoot_list, kananfoot_list, rightchest_list,\
               yogatime, preparationtime, loop, cooldown, pictures


    def strength_mediumlist(self):
        yoganame = ['Kwek=Kwek', 'Tree Pose (Right)', 'Warrior Pose (Left)', 'Warrior Pose (Right)',
                    'Goddess Pose', 'Trikonasana (Left)', 'Trikonasana (Right)', 'Mountain Pose', 'Half Bending',
                    'Butterfly Pose']

        kaliwabar_list = [[169, 149, 217, 157, 177, 197],
                          [169, 149, 216, 156, 176, 196],
                          [107, 87, 214, 154, 174, 194],
                          [107, 87, 209, 149, 169, 189],
                          [105, 85, 292, 232, 252, 272],
                          [117, 97, 215, 155, 175, 195],
                          [116, 96, 219, 159, 179, 199],
                          [28, 8, 215, 155, 175, 195],
                          [204, 184, 204, 144, 164, 184],
                          [42, 22, 143, 83, 103, 123]]

        kananbar_list = [[204, 184, 206, 146, 166, 186], [203, 183, 206, 146, 166, 186], [282, 262, 204, 144, 164, 184],
                         [274, 254, 200, 140, 160, 180], [267, 247, 120, 60, 80, 100], [266, 246, 191, 131, 151, 171],
                         [257, 237, 199, 139, 159, 179], [355, 335, 193, 133, 153, 173], [206, 186, 201, 141, 161, 181],
                         [333, 313, 288, 228, 248, 268]]
        paakaliwabar_list = [[250, 230, 58, -2, 18, 38], [187, 167, 208, 148, 168, 188], [244, 224, 165, 105, 125, 145],
                             [222, 202, 208, 148, 168, 188], [269, 249, 131, 71, 91, 111],
                             [313, 293, 219, 159, 179, 199], [145, 125, 206, 146, 166, 186],
                             [201, 181, 206, 146, 166, 186], [100, 80, 210, 150, 170, 190], [293, 273, 48, -12, 8, 28]]
        paakananbar_list = [[193, 173, 207, 147, 167, 187], [134, 114, 358, 298, 318, 338],
                            [160, 140, 209, 149, 169, 189], [139, 119, 243, 183, 203, 223],
                            [106, 86, 294, 234, 254, 274], [235, 215, 211, 151, 171, 191], [56, 36, 210, 150, 170, 190],
                            [182, 162, 206, 146, 166, 186], [99, 79, 211, 151, 171, 191], [86, 66, 373, 313, 333, 353]]
        kaliwafoot_list = [[281, 221, 231, 271], [211, 151, 161, 201], [270, 210, 220, 260], [192, 132, 142, 182],
                           [285, 225, 235, 275], [239, 179, 189, 229], [197, 137, 147, 187], [220, 160, 170, 210],
                           [140, 80, 90, 130], [208, 148, 158, 198]]
        kananfoot_list = [[203, 143, 153, 193], [155, 95, 105, 145], [209, 149, 159, 199], [159, 99, 109, 149],
                          [140, 80, 90, 130], [233, 173, 183, 223], [172, 112, 122, 162], [198, 138, 148, 188],
                          [143, 83, 93, 133], [199, 139, 149, 189]]
        rightchest_list = [[270, 210, 220, 260], [207, 147, 157, 197], [264, 204, 214, 254], [242, 182, 192, 232],
                           [289, 229, 239, 279], [333, 273, 283, 323], [165, 105, 115, 155], [221, 161, 171, 211],
                           [120, 60, 70, 110], [313, 253, 263, 303]]

        yogatime = 6
        preparationtime = 5
        loop = 3
        cooldown = 10

        pictures = ["pictures1/p11.jpg", "pictures1/p12.jpg", "pictures1/p13.jpg", "pictures1/p14.jpg", "pictures1/p15.jpg",
                    "pictures1/p16.jpg", "pictures1/p7.jpg", "pictures1/p18.jpg", "pictures1/p19.jpg", "pictures1/p20.jpg"]

        return yoganame, kaliwabar_list, kananbar_list, paakaliwabar_list, paakananbar_list, kaliwafoot_list, kananfoot_list, rightchest_list, \
               yogatime, preparationtime, loop, cooldown, pictures

    def strength_hardlist(self):
        yoganame = ['Kwek=Kwek', 'Tree Pose (Right)', 'Warrior Pose (Left)', 'Warrior Pose (Right)',
                    'Goddess Pose', 'Trikonasana (Left)', 'Trikonasana (Right)', 'Mountain Pose', 'Half Bending',
                    'Butterfly Pose']

        kaliwabar_list = [[36, 16, 239, 179, 199, 219],
                          [204, 184, 225, 165, 185, 205],
                          [109, 89, 217, 157, 177, 197],
                          [95, 75, 213, 153, 173, 193],
                          [107, 87, 300, 240, 260, 280],
                          [121, 101, 227, 167, 187, 207],
                          [333, 313, 64, 4, 24, 44],
                          [25, 5, 217, 157, 177, 197],
                          [259, 239, 198, 138, 158, 178],
                          [50, 30, 132, 72, 92, 112]]
        kananbar_list = [[179, 159, 197, 137, 157, 177],
                         [338, 318, 189, 129, 149, 169],
                         [286, 266, 204, 144, 164, 184],
                         [273, 253, 197, 137, 157, 177],
                         [262, 242, 115, 55, 75, 95],
                         [272, 252, 193, 133, 153, 173],
                         [250, 230, 206, 146, 166, 186],
                         [356, 336, 199, 139, 159, 179],
                         [269, 249, 196, 136, 156, 176],
                         [324, 304, 287, 227, 247, 267]]
        paakaliwabar_list = [[264, 244, 57, -3, 17, 37],
                             [169, 149, 209, 149, 169, 189],
                             [259, 239, 128, 68, 88, 108],
                             [232, 212, 218, 158, 178, 198],
                             [273, 253, 119, 59, 79, 99],
                             [343, 323, 195, 135, 155, 175],
                             [139, 119, 206, 146, 166, 186],
                             [201, 181, 210, 150, 170, 190],
                             [76, 56, 209, 149, 169, 189],
                             [300, 280, 50, -10, 10, 30]]
        paakananbar_list = [[211, 191, 209, 149, 169, 189],
                            [113, 93, 361, 301, 321, 341],
                            [144, 124, 208, 148, 168, 188],
                            [111, 91, 289, 229, 249, 269],
                            [104, 84, 302, 242, 262, 282],
                            [245, 225, 216, 156, 176, 196],
                            [37, 17, 226, 166, 186, 206],
                            [184, 164, 206, 146, 166, 186],
                            [84, 64, 208, 148, 168, 188],
                            [74, 54, 368, 308, 328, 348]]
        kaliwafoot_list = [[279, 219, 229, 269],
                           [221, 161, 171, 211],
                           [292, 232, 242, 282],
                           [179, 119, 129, 169],
                           [238, 178, 188, 228],
                           [256, 196, 206, 246],
                           [214, 154, 164, 204],
                           [225, 165, 175, 215],
                           [140, 80, 90, 130],
                           [255, 195, 205, 245]]
        kananfoot_list = [[226, 166, 176, 216],
                          [159, 99, 109, 149],
                          [244, 184, 194, 234],
                          [139, 79, 89, 129],
                          [188, 128, 138, 178],
                          [205, 145, 155, 195],
                          [161, 101, 111, 151],
                          [202, 142, 152, 192],
                          [145, 85, 95, 135],
                          [200, 140, 150, 190]]
        rightchest_list = [[284, 224, 234, 274],
                           [189, 129, 139, 179],
                           [279, 219, 229, 269],
                           [252, 192, 202, 242],
                           [293, 233, 243, 283],
                           [363, 303, 313, 353],
                           [159, 99, 109, 149],
                           [221, 161, 171, 211],
                           [96, 36, 46, 86],
                           [320, 260, 270, 310]]

        yogatime = 30
        preparationtime = 10
        loop = 3
        cooldown = 10

        pictures = ["pictures1/p21.jpg", "pictures1/p22.jpg", "pictures1/p23.jpg", "pictures1/p24.jpg", "pictures1/p25.jpg",
                    "pictures1/p26.jpg", "pictures1/p27.jpg", "pictures1/p28.jpg", "pictures1/p29.jpg", "pictures1/p30.jpg"]

        return yoganame, kaliwabar_list, kananbar_list, paakaliwabar_list, paakananbar_list, kaliwafoot_list, kananfoot_list, rightchest_list, \
               yogatime, preparationtime, loop, cooldown, pictures

    def balance_easylist(self):
        yoganame = ["Treepose Left", "Treepose Right", "Warrior II Left", "Warrior II Right", "Five Pointed Star"
                    ,"Warrior I Left", "Warrior I Right", "Crescent Low Lunge (L)", "Crescent Low Lunge (R)", "Chairpose"]

        kaliwabar_list = [[167, 147, 220, 160, 180, 200], [171, 151, 219, 159, 179, 199], [118, 98, 206, 146, 166, 186],
                          [102, 82, 211, 151, 171, 191], [103, 83, 210, 150, 170, 190], [173, 153, 219, 159, 179, 199],
                          [205, 185, 201, 141, 161, 181], [177, 157, 223, 163, 183, 203],
                          [208, 188, 192, 132, 152, 172], [206, 186, 201, 141, 161, 181]]
        kananbar_list = [[206, 186, 201, 141, 161, 181], [212, 192, 197, 137, 157, 177], [279, 259, 207, 147, 167, 187],
                         [267, 247, 208, 148, 168, 188], [275, 255, 203, 143, 163, 183], [164, 144, 227, 167, 187, 207],
                         [200, 180, 197, 137, 157, 177], [170, 150, 232, 172, 192, 212], [204, 184, 188, 128, 148, 168],
                         [206, 186, 197, 137, 157, 177]]
        paakaliwabar_list = [[229, 209, 130, 70, 90, 110], [190, 170, 204, 144, 164, 184],
                             [244, 224, 164, 104, 124, 144], [219, 199, 207, 147, 167, 187],
                             [208, 188, 212, 152, 172, 192], [161, 141, 204, 144, 164, 184],
                             [157, 137, 253, 193, 213, 233], [177, 157, 123, 63, 83, 103],
                             [102, 82, 306, 246, 266, 286], [127, 107, 269, 209, 229, 249]]
        paakananbar_list = [[191, 171, 214, 154, 174, 194], [152, 132, 281, 221, 241, 261],
                            [166, 146, 211, 151, 171, 191], [142, 122, 256, 196, 216, 236],
                            [168, 148, 208, 148, 168, 188], [219, 199, 166, 106, 126, 146],
                            [213, 193, 214, 154, 174, 194], [274, 254, 112, 52, 72, 92], [194, 174, 297, 237, 257, 277],
                            [129, 109, 267, 207, 227, 247]]
        kaliwafoot_list = [[247, 187, 197, 237], [213, 153, 163, 203], [273, 213, 223, 263], [200, 140, 150, 190],
                           [232, 172, 182, 222], [309, 249, 259, 299], [131, 71, 81, 121], [242, 182, 192, 232],
                           [133, 73, 83, 123], [134, 74, 84, 124]]
        kananfoot_list = [[212, 152, 162, 202], [181, 121, 131, 171], [236, 176, 186, 226], [140, 80, 90, 130],
                          [190, 130, 140, 180], [283, 223, 233, 273], [105, 45, 55, 95], [281, 221, 231, 271],
                          [176, 116, 126, 166], [132, 72, 82, 122]]
        rightchest_list = [[249, 189, 199, 239], [210, 150, 160, 200], [264, 204, 214, 254], [239, 179, 189, 229],
                           [228, 168, 178, 218], [181, 121, 131, 171], [177, 117, 127, 167], [197, 137, 147, 187],
                           [122, 62, 72, 112], [147, 87, 97, 137]]

        yogatime = 10
        preparationtime = 5
        loop = 1
        cooldown = 10

        pictures = ["pictures1/b1.jpg", "pictures1/b2.jpg", "pictures1/b3.jpg", "pictures1/b4.jpg",
                    "pictures1/b5.jpg",
                    "pictures1/b6.jpg", "pictures1/b7.jpg", "pictures1/b8.jpg", "pictures1/b9.jpg",
                    "pictures1/b10.jpg"]

        return yoganame, kaliwabar_list, kananbar_list, paakaliwabar_list, paakananbar_list, kaliwafoot_list, kananfoot_list, rightchest_list, \
            yogatime, preparationtime, loop, cooldown, pictures


    def balance_mediumlist(self):
        yoganame = ["Treepose Left", "Treepose Right", "Warrior II Left", "Warrior II Right", "Five Pointed Star"
            , "Warrior I Left", "Warrior I Right", "Crescent Low Lunge (L)", "Crescent Low Lunge (R)", "Chairpose"]

        kaliwabar_list = [[167, 147, 218, 158, 178, 198], [173, 153, 219, 159, 179, 199], [113, 93, 205, 145, 165, 185],
                          [103, 83, 210, 150, 170, 190], [106, 86, 208, 148, 168, 188], [168, 148, 225, 165, 185, 205],
                          [204, 184, 195, 135, 155, 175], [72, 52, 218, 158, 178, 198], [136, 116, 217, 157, 177, 197],
                          [204, 184, 198, 138, 158, 178]]
        kananbar_list = [[208, 188, 203, 143, 163, 183], [212, 192, 201, 141, 161, 181], [280, 260, 208, 148, 168, 188],
                         [263, 243, 210, 150, 170, 190], [270, 250, 206, 146, 166, 186], [165, 145, 229, 169, 189, 209],
                         [201, 181, 193, 133, 153, 173], [245, 225, 208, 148, 168, 188], [302, 282, 198, 138, 158, 178],
                         [205, 185, 194, 134, 154, 174]]
        paakaliwabar_list = [[250, 230, 58, -2, 18, 38], [190, 170, 206, 146, 166, 186], [241, 221, 166, 106, 126, 146],
                             [216, 196, 207, 147, 167, 187], [207, 187, 212, 152, 172, 192],
                             [164, 144, 207, 147, 167, 187], [154, 134, 246, 186, 206, 226],
                             [252, 232, 122, 62, 82, 102], [60, 40, 283, 223, 243, 263], [122, 102, 276, 216, 236, 256]]
        paakananbar_list = [[195, 175, 207, 147, 167, 187], [136, 116, 359, 299, 319, 339],
                            [165, 145, 210, 150, 170, 190], [133, 113, 258, 198, 218, 238],
                            [168, 148, 207, 147, 167, 187], [219, 199, 167, 107, 127, 147],
                            [208, 188, 212, 152, 172, 192], [317, 297, 137, 77, 97, 117], [106, 86, 309, 249, 269, 289],
                            [124, 104, 272, 212, 232, 252]]
        kaliwafoot_list = [[282, 222, 232, 272], [218, 158, 168, 208], [272, 212, 222, 262], [202, 142, 152, 192],
                           [233, 173, 183, 223], [296, 236, 246, 286], [146, 86, 96, 136], [247, 187, 197, 237],
                           [151, 91, 101, 141], [130, 70, 80, 120]]
        kananfoot_list = [[198, 138, 148, 188], [128, 68, 78, 118], [217, 157, 167, 207], [148, 88, 98, 138],
                          [196, 136, 146, 186], [287, 227, 237, 277], [118, 58, 68, 108], [257, 197, 207, 247],
                          [179, 119, 129, 169], [129, 69, 79, 119]]
        rightchest_list = [[270, 210, 220, 260], [210, 150, 160, 200], [261, 201, 211, 251], [236, 176, 186, 226],
                           [227, 167, 177, 217], [184, 124, 134, 174], [174, 114, 124, 164], [272, 212, 222, 262],
                           [80, 20, 30, 70], [142, 82, 92, 132]]

        yogatime = 10
        preparationtime = 5
        loop = 1
        cooldown = 10

        pictures = ["pictures1/b11.jpg", "pictures1/b12.jpg", "pictures1/b13.jpg", "pictures1/b14.jpg",
                    "pictures1/b15.jpg",
                    "pictures1/b16.jpg", "pictures1/b17.jpg", "pictures1/b18.jpg", "pictures1/b19.jpg",
                    "pictures1/b20.jpg"]

        return yoganame, kaliwabar_list, kananbar_list, paakaliwabar_list, paakananbar_list, kaliwafoot_list, kananfoot_list, rightchest_list, \
            yogatime, preparationtime, loop, cooldown, pictures

    def balance_hardlist(self):
        yoganame = ["Treepose Left", "Treepose Right", "Warrior II Left", "Warrior II Right", "Five Pointed Star"
            , "Warrior I Left", "Warrior I Right", "Crescent Low Lunge (L)", "Crescent Low Lunge (R)", "Downward Facing Dog"]

        kaliwabar_list = [[49, 29, 214, 154, 174, 194], [201, 181, 224, 164, 184, 204], [117, 97, 206, 146, 166, 186],
                          [102, 82, 209, 149, 169, 189], [108, 88, 210, 150, 170, 190], [185, 165, 224, 164, 184, 204],
                          [204, 184, 193, 133, 153, 173], [207, 187, 234, 174, 194, 214],
                          [172, 152, 185, 125, 145, 165], [187, 167, 228, 168, 188, 208]]
        kananbar_list = [[186, 166, 189, 129, 149, 169], [339, 319, 197, 137, 157, 177], [275, 255, 205, 145, 165, 185],
                         [256, 236, 210, 150, 170, 190], [269, 249, 204, 144, 164, 184], [176, 156, 231, 171, 191, 211],
                         [196, 176, 194, 134, 154, 174], [202, 182, 238, 178, 198, 218], [179, 159, 176, 116, 136, 156],
                         [192, 172, 226, 166, 186, 206]]
        paakaliwabar_list = [[267, 247, 60, 0, 20, 40], [178, 158, 204, 144, 164, 184], [266, 246, 146, 86, 106, 126],
                             [231, 211, 206, 146, 166, 186], [204, 184, 212, 152, 172, 192],
                             [155, 135, 195, 135, 155, 175], [130, 110, 262, 202, 222, 242],
                             [140, 120, 151, 91, 111, 131], [104, 84, 319, 259, 279, 299],
                             [307, 287, 194, 134, 154, 174]]
        paakananbar_list = [[208, 188, 211, 151, 171, 191], [115, 95, 363, 303, 323, 343],
                            [143, 123, 210, 150, 170, 190], [103, 83, 275, 215, 235, 255],
                            [172, 152, 208, 148, 168, 188], [250, 230, 150, 90, 110, 130],
                            [222, 202, 216, 156, 176, 196], [269, 249, 106, 46, 66, 86], [243, 223, 264, 204, 224, 244],
                            [307, 287, 195, 135, 155, 175]]
        kaliwafoot_list = [[280, 220, 230, 270], [226, 166, 176, 216], [271, 211, 221, 261], [199, 139, 149, 189],
                           [226, 166, 176, 216], [321, 261, 271, 311], [139, 79, 89, 129], [228, 168, 178, 218],
                           [137, 77, 87, 127], [297, 237, 247, 287]]
        kananfoot_list = [[193, 133, 143, 183], [142, 82, 92, 132], [225, 165, 175, 215], [154, 94, 104, 144],
                          [205, 145, 155, 195], [279, 219, 229, 269], [102, 42, 52, 92], [291, 231, 241, 281],
                          [192, 132, 142, 182], [294, 234, 244, 284]]
        rightchest_list = [[287, 227, 237, 277], [198, 138, 148, 188], [286, 226, 236, 276], [251, 191, 201, 241],
                           [224, 164, 174, 214], [175, 115, 125, 165], [150, 90, 100, 140], [160, 100, 110, 150],
                           [124, 64, 74, 114], [327, 267, 277, 317]]

        yogatime = 10
        preparationtime = 5
        loop = 1
        cooldown = 10

        pictures = ["pictures1/b21.jpg", "pictures1/b22.jpg", "pictures1/b23.jpg", "pictures1/b24.jpg",
                    "pictures1/b25.jpg",
                    "pictures1/b26.jpg", "pictures1/b27.jpg", "pictures1/b28.jpg", "pictures1/b29.jpg",
                    "pictures1/b30.jpg"]

        return yoganame, kaliwabar_list, kananbar_list, paakaliwabar_list, paakananbar_list, kaliwafoot_list, kananfoot_list, rightchest_list, \
            yogatime, preparationtime, loop, cooldown, pictures

    def flexibility_easylist(self):
        yoganame = ["Trikonasana (L)", "Trikonasana (R)", "Goddess", "Half Forward Bend", "Mountain Pose"
            , "Warrior II Left", "Warrior II Right", "Seated Side Bend (L)", "Seated Side Bend (R)", "Butterfly"]

        kaliwabar_list = [[77, 57, 218, 158, 178, 198], [135, 115, 216, 156, 176, 196], [107, 87, 295, 235, 255, 275],
                          [317, 297, 200, 140, 160, 180], [25, 5, 220, 160, 180, 200], [114, 94, 205, 145, 165, 185],
                          [101, 81, 211, 151, 171, 191], [68, 48, 249, 189, 209, 229], [206, 186, 220, 160, 180, 200],
                          [17, -3, 201, 141, 161, 181]]
        kananbar_list = [[249, 229, 197, 137, 157, 177], [308, 288, 188, 128, 148, 168], [261, 241, 127, 67, 87, 107],
                         [325, 305, 189, 129, 149, 169], [355, 335, 195, 135, 155, 175], [277, 257, 205, 145, 165, 185],
                         [264, 244, 207, 147, 167, 187], [191, 171, 182, 122, 142, 162], [310, 290, 173, 113, 133, 153],
                         [369, 349, 225, 165, 185, 205]]
        paakaliwabar_list = [[288, 268, 212, 152, 172, 192], [161, 141, 205, 145, 165, 185],
                             [259, 239, 138, 78, 98, 118], [98, 78, 210, 150, 170, 190], [200, 180, 211, 151, 171, 191],
                             [241, 221, 175, 115, 135, 155], [213, 193, 209, 149, 169, 189], [313, 293, 41, -19, 1, 21],
                             [250, 230, 46, -14, 6, 26], [293, 273, 43, -17, 3, 23]]
        paakananbar_list = [[219, 199, 212, 152, 172, 192], [89, 69, 209, 149, 169, 189], [115, 95, 284, 224, 244, 264],
                            [100, 80, 210, 150, 170, 190], [184, 164, 207, 147, 167, 187],
                            [164, 144, 209, 149, 169, 189], [133, 113, 253, 193, 213, 233],
                            [143, 123, 366, 306, 326, 346], [87, 67, 361, 301, 321, 341], [90, 70, 375, 315, 335, 355]]
        kaliwafoot_list = [[214, 154, 164, 204], [217, 157, 167, 207], [277, 217, 227, 267], [145, 85, 95, 135],
                           [223, 163, 173, 213], [265, 205, 215, 255], [189, 129, 139, 179], [206, 146, 156, 196],
                           [230, 170, 180, 220], [207, 147, 157, 197]]
        kananfoot_list = [[228, 168, 178, 218], [183, 123, 133, 173], [144, 84, 94, 134], [151, 91, 101, 141],
                          [193, 133, 143, 183], [247, 187, 197, 237], [152, 92, 102, 142], [201, 141, 151, 191],
                          [203, 143, 153, 193], [224, 164, 174, 214]]
        rightchest_list = [[308, 248, 258, 298], [181, 121, 131, 171], [279, 219, 229, 269], [118, 58, 68, 108],
                           [220, 160, 170, 210], [261, 201, 211, 251], [233, 173, 183, 223], [333, 273, 283, 323],
                           [270, 210, 220, 260], [313, 253, 263, 303]]

        yogatime = 10
        preparationtime = 5
        loop = 0
        cooldown = 10

        pictures = ["pictures1/f1.jpg", "pictures1/f2.jpg", "pictures1/f3.jpg", "pictures1/f4.jpg",
                    "pictures1/f5.jpg",
                    "pictures1/f6.jpg", "pictures1/f7.jpg", "pictures1/f8.jpg", "pictures1/f9.jpg",
                    "pictures1/f10.jpg"]

        return yoganame, kaliwabar_list, kananbar_list, paakaliwabar_list, paakananbar_list, kaliwafoot_list, kananfoot_list, rightchest_list, \
            yogatime, preparationtime, loop, cooldown, pictures

    def flexibility_mediumlist(self):
        yoganame = ["Trikonasana (L)", "Trikonasana (R)", "Goddess", "Half Forward Bend", "Mountain Pose"
            , "Warrior II Left", "Warrior II Right", "Seated Side Bend Stretch (L)", "Seated Side Bend Stretch (R)", "Butterfly"]

        kaliwabar_list = [[126, 106, 216, 156, 176, 196], [120, 100, 217, 157, 177, 197], [108, 88, 287, 227, 247, 267],
                          [202, 182, 205, 145, 165, 185], [25, 5, 216, 156, 176, 196], [111, 91, 207, 147, 167, 187],
                          [103, 83, 210, 150, 170, 190], [84, 64, 241, 181, 201, 221], [205, 185, 233, 173, 193, 213],
                          [46, 26, 132, 72, 92, 112]]
        kananbar_list = [[262, 242, 196, 136, 156, 176], [256, 236, 202, 142, 162, 182], [259, 239, 129, 69, 89, 109],
                         [201, 181, 204, 144, 164, 184], [354, 334, 201, 141, 161, 181], [275, 255, 206, 146, 166, 186],
                         [261, 241, 211, 151, 171, 191], [166, 146, 189, 129, 149, 169], [288, 268, 191, 131, 151, 171],
                         [329, 309, 296, 236, 256, 276]]
        paakaliwabar_list = [[324, 304, 214, 154, 174, 194], [142, 122, 209, 149, 169, 189],
                             [267, 247, 130, 70, 90, 110], [105, 85, 207, 147, 167, 187],
                             [200, 180, 210, 150, 170, 190], [246, 226, 156, 96, 116, 136],
                             [219, 199, 211, 151, 171, 191], [304, 284, 214, 154, 174, 194], [247, 227, 45, -15, 5, 25],
                             [289, 269, 48, -12, 8, 28]]
        paakananbar_list = [[243, 223, 215, 155, 175, 195], [58, 38, 209, 149, 169, 189], [105, 85, 296, 236, 256, 276],
                            [104, 84, 207, 147, 167, 187], [183, 163, 206, 146, 166, 186],
                            [152, 132, 211, 151, 171, 191], [124, 104, 259, 199, 219, 239],
                            [131, 111, 368, 308, 328, 348], [57, 37, 222, 162, 182, 202], [86, 66, 374, 314, 334, 354]]
        kaliwafoot_list = [[242, 182, 192, 232], [214, 154, 164, 204], [278, 218, 228, 268], [140, 80, 90, 130],
                           [224, 164, 174, 214], [278, 218, 228, 268], [206, 146, 156, 196], [266, 206, 216, 256],
                           [209, 149, 159, 199], [207, 147, 157, 197]]
        kananfoot_list = [[218, 158, 168, 208], [171, 111, 121, 161], [140, 80, 90, 130], [144, 84, 94, 134],
                          [199, 139, 149, 189], [224, 164, 174, 214], [152, 92, 102, 142], [209, 149, 159, 199],
                          [130, 70, 80, 120], [212, 152, 162, 202]]
        rightchest_list = [[344, 284, 294, 334], [162, 102, 112, 152], [287, 227, 237, 277], [125, 65, 75, 115],
                           [220, 160, 170, 210], [266, 206, 216, 256], [239, 179, 189, 229], [324, 264, 274, 314],
                           [267, 207, 217, 257], [309, 249, 259, 299]]

        yogatime = 5
        preparationtime = 5
        loop = 1
        cooldown = 10

        pictures = ["pictures1/f11.jpg", "pictures1/f12.jpg", "pictures1/f13.jpg", "pictures1/f14.jpg",
                    "pictures1/f5.jpg",
                    "pictures1/f16.jpg", "pictures1/f17.jpg", "pictures1/f18.jpg", "pictures1/f19.jpg",
                    "pictures1/f20.jpg"]

        return yoganame, kaliwabar_list, kananbar_list, paakaliwabar_list, paakananbar_list, kaliwafoot_list, kananfoot_list, rightchest_list, \
            yogatime, preparationtime, loop, cooldown, pictures

    def flexibility_hardlist(self):
        yoganame = ["Trikonasana (L)", "Trikonasana (R)", "Goddess", "Half Forward Bend", "Mountain Pose"
            , "Warrior II Left", "Warrior II Right", "Extended Side Bend (L)", "Extended Side Bend (R)",
                    "Butterfly"]

        kaliwabar_list = [[124, 104, 231, 171, 191, 211], [116, 96, 219, 159, 179, 199], [116, 96, 279, 219, 239, 259],
                          [258, 238, 199, 139, 159, 179], [24, 4, 217, 157, 177, 197], [112, 92, 208, 148, 168, 188],
                          [103, 83, 211, 151, 171, 191], [81, 61, 94, 34, 54, 74], [199, 179, 213, 153, 173, 193],
                          [53, 33, 109, 49, 69, 89]]
        kananbar_list = [[276, 256, 195, 135, 155, 175], [246, 226, 195, 135, 155, 175], [256, 236, 137, 77, 97, 117],
                         [259, 239, 201, 141, 161, 181], [355, 335, 198, 138, 158, 178], [274, 254, 206, 146, 166, 186],
                         [258, 238, 209, 149, 169, 189], [183, 163, 197, 137, 157, 177], [298, 278, 209, 149, 169, 189],
                         [316, 296, 310, 250, 270, 290]]
        paakaliwabar_list = [[345, 325, 194, 134, 154, 174], [133, 113, 208, 148, 168, 188],
                             [264, 244, 126, 66, 86, 106], [70, 50, 210, 150, 170, 190], [198, 178, 211, 151, 171, 191],
                             [264, 244, 139, 79, 99, 119], [233, 213, 206, 146, 166, 186], [340, 320, 138, 78, 98, 118],
                             [183, 163, 208, 148, 168, 188], [305, 285, 50, -10, 10, 30]]
        paakananbar_list = [[257, 237, 215, 155, 175, 195], [33, 13, 222, 162, 182, 202], [116, 96, 291, 231, 251, 271],
                            [73, 53, 210, 150, 170, 190], [184, 164, 210, 150, 170, 190],
                            [143, 123, 209, 149, 169, 189], [102, 82, 282, 222, 242, 262],
                            [196, 176, 208, 148, 168, 188], [47, 27, 280, 220, 240, 260], [73, 53, 372, 312, 332, 352]]
        kaliwafoot_list = [[257, 197, 207, 247], [227, 167, 177, 217], [236, 176, 186, 226], [142, 82, 92, 132],
                           [225, 165, 175, 215], [279, 219, 229, 269], [207, 147, 157, 197], [263, 203, 213, 253],
                           [187, 127, 137, 177], [201, 141, 151, 191]]
        kananfoot_list = [[220, 160, 170, 210], [167, 107, 117, 157], [186, 126, 136, 176], [146, 86, 96, 136],
                          [192, 132, 142, 182], [226, 166, 176, 216], [152, 92, 102, 142], [209, 149, 159, 199],
                          [158, 98, 108, 148], [201, 141, 151, 191]]
        rightchest_list = [[365, 305, 315, 355], [153, 93, 103, 143], [284, 224, 234, 274], [90, 30, 40, 80],
                           [218, 158, 168, 208], [284, 224, 234, 274], [253, 193, 203, 243], [360, 300, 310, 350],
                           [203, 143, 153, 193], [325, 265, 275, 315]]

        yogatime = 10
        preparationtime = 5
        loop = 0
        cooldown = 10

        pictures = ["pictures1/f21.jpg", "pictures1/f22.jpg", "pictures1/f23.jpg", "pictures1/f24.jpg",
                    "pictures1/f25.jpg",
                    "pictures1/f26.jpg", "pictures1/f27.jpg", "pictures1/f28.jpg", "pictures1/f29.jpg",
                    "pictures1/f30.jpg"]

        return yoganame, kaliwabar_list, kananbar_list, paakaliwabar_list, paakananbar_list, kaliwafoot_list, kananfoot_list, rightchest_list, \
            yogatime, preparationtime, loop, cooldown, pictures

    def totesting(self):

        yoganame = ["Testing","Treepose Right", "Warrior-I Left", "Warrior-I Right", "WarriorII-Left"
                    ,"Warrior-II Right", "Warrior-III Left", "Warrior-III Right", "Half-Bending", "GodPose"]

        yogapercent = ["10%", "70%", "70%", "70%", "70%", "70%", "50%", "10%", "2%", "5%"]

        yogaprogress = 18

        kaliwabar_list = [[0, 151, 225, 165, 185, 205],  # Tree pose (left)
                          [1, 144, 219, 159, 179, 199],  # Tree pose (Right)
                          [2, 89, 215, 155, 175, 195],  # Warrior pose (left)
                          [3, 76, 214, 154, 174, 194],  # Warrior pose (Right)
                          [4, 91, 285, 225, 245, 265],  # Goddess
                          [5, 65, 201, 151, 171, 191],  # Trikonasana (left)
                          [6, 118, 217, 157, 177, 197],  # Trikonasana (right)
                          [7, 0, 204, 174, 181, 197],  # Mountain Pose
                          [8, 290, 206, 146, 166, 186],  # Half Bending
                          [9, 0, 201, 151, 171, 191]]  # Butterfly Pose

        kananbar_list = [[211, 191, 202, 142, 162, 182],  # Tree pose (left)
                         [215, 195, 202, 142, 162, 182],  # Tree pose(Right)
                         [278, 258, 203, 143, 163, 183],  # Warrior pose (left)
                         [264, 244, 200, 140, 160, 180],  # Warrior pose (Right)
                         [264, 244, 130, 70, 90, 110],  # Goddess pose
                         [252, 232, 196, 136, 156, 176],  # Trikonasana (left)
                         [308, 288, 188, 128, 148, 168],  # Trikonasana (right)
                         [346, 326, 191, 161, 168, 184],  # Mountain Pose
                         [340, 300, 198, 138, 158, 178],  # Half Bending
                         [30, 0, 219, 159, 179, 199]]  # Butterfly pose

        paakaliwabar_list = [[230, 210, 115, 55, 75, 95],  # Tree pose (left)
                             [193, 173, 206, 146, 166, 186],  # Tree pose(Right)
                             [232, 212, 167, 107, 127, 147],  # Warrior pose (left)
                             [214, 194, 219, 159, 179, 199],  # Warrior pose (Right)
                             [262, 242, 138, 78, 98, 118],  # Goddess pose
                             [295, 275, 204, 144, 164, 184],  # Trikonasana (left)
                             [163, 143, 203, 143, 163, 183],  # Trikonasana (right)
                             [196, 176, 193, 163, 170, 186],  # Mountain Pose
                             [114, 74, 217, 167, 187, 207],  # Half Bending
                             [289, 269, 41, 0, 2, 22]]  # Butterfly pose

        paakananbar_list = [[188, 168, 218, 158, 178, 198],  # Tree pose (left)
                            [150, 130, 290, 230, 250, 270],  # Tree pose(Right)
                            [166, 146, 206, 146, 166, 186],  # Warrior pose (left)
                            [138, 118, 258, 198, 218, 238],  # Warrior pose (Right)
                            [114, 94, 288, 228, 248, 268],  # Goddess pose
                            [221, 201, 212, 152, 172, 192],  # Trikonasana (left)
                            [83, 63, 216, 156, 176, 196],  # Trikonasana (right)
                            [185, 165, 196, 166, 173, 189],  # Mountain Pose
                            [123, 83, 212, 152, 172, 192],  # Half Bending
                            [91, 71, 360, 317, 337, 357]]  # Butterfly pose

        kaliwafoot_list = [[266, 206, 216, 256],  # Tree pose (left)
                           [210, 150, 160, 200],  # Tree pose (right)
                           [269, 209, 219, 259],  # Warrior pose (left)
                           [206, 146, 156, 196],  # Warrior pose (right)
                           [287, 227, 237, 277],  # Goddess pose
                           [240, 180, 190, 230],  # Trikonasana (left)
                           [209, 149, 159, 199],  # Trikonasana (right)
                           [236, 176, 186, 226],  # Mountain pose
                           [149, 89, 99, 139],  # Half Bending
                           [205, 145, 155, 195]]  # Butterfly pose

        kananfoot_list = [[218, 158, 168, 208],  # Tree pose (left)
                          [173, 113, 123, 163],  # Tree pose (right)
                          [231, 171, 181, 221],  # Warrior pose (left)
                          [148, 88, 98, 138],  # Warrior pose (right)
                          [146, 86, 96, 136],  # Goddess pose
                          [228, 168, 178, 218],  # Trikonasana (left)
                          [183, 123, 133, 173],  # Trikonasana (right)
                          [185, 125, 135, 175],  # Mountain pose
                          [151, 91, 101, 141],  # Half Bending
                          [219, 159, 169, 209]]  # Butterfly pose

        rightchest_list = [[250, 190, 200, 240],  # Tree pose (left)
                           [213, 153, 163, 203],  # Tree pose(Right)
                           [262, 202, 212, 252],  # Warrior pose (left)
                           [234, 174, 184, 224],  # Warrior pose (Right)
                           [282, 222, 232, 272],  # Goddess pose
                           [315, 255, 265, 305],  # Trikonasana (left)
                           [183, 123, 133, 173],  # Trikonasana (right)
                           [216, 156, 166, 206],  # Mountain Pose
                           [124, 64, 74, 114],  # Half Bending
                           [309, 249, 259, 299]]  # Butterfly pose

        return yoganame,yogapercent,yogaprogress, kaliwabar_list, kananbar_list, paakaliwabar_list, paakananbar_list, kaliwafoot_list, kananfoot_list, rightchest_list

class tkinter_design:
    def frame_widgets(self,frame,h,w,bg,x,y):
        frame_name = Frame(frame, height=h, width=w, bg=bg)
        frame_name.place(x=x, y=y)

        return frame_name

    def navigation_buttons(self,frame,img,command,x,y):
        button_name = Button(frame, image=img, borderwidth=0,highlightthickness=0, cursor="hand2", command=command)
        button_name.place(x=x, y=y)

        return button_name

    def home_button(self,frame,text, display, function, data,data2,data3,bx,by,lx,ly,px,py):
        button = Button(frame, text=text, font=('Book Antiqua', 15,),width=7,command=lambda: function(data,data2,data3),cursor= "hand2")
        button.place(x=bx, y=by)
        Label(frame, text=f'{display}%', font=('Book Antiqua', 10), bg="white").place(x=lx, y=ly)
        ttk.Progressbar(frame,orient='horizontal',mode='determinate',length=200, value=display).place(x=px, y=py)

        return button

    def home_progress_label(self, frame, display, bx,by,lx,ly,px,py):
        Label(frame, text="PROGRESS  ", font=('Book Antiqua', 15, "bold"), bg="white").place(x=bx, y=by)
        Label(frame, text=f'{display}%', font=('Book Antiqua', 10), bg="white").place(x=lx, y=ly)
        ttk.Progressbar(frame, orient='horizontal', mode='determinate', length=200, value=display).place(x=px, y=py)

    def home_disable_button(self,sm,sh,strength_easy_accuracy,strength_medium_accuracy,
                            bm,bh,balance_easy_accuracy,balance_medium_accuracy,
                            fm,fh,flexibility_easy_accuracy,flexibility_medium_accuracy):
        if strength_easy_accuracy < 69:
            sm['state'] = DISABLED
            sm.config(cursor="arrow")
            ToolTip(sm, msg="Strength Easy must be at least 70% to unlock it", anchor=CENTER,fg='red',font=('Book Antiqua', 11))
        if strength_easy_accuracy < 89 or strength_medium_accuracy < 69:
            sh['state'] = DISABLED
            sh.config(cursor="arrow")
            ToolTip(sh,msg="Must have at least 90% Strength Easy and \n70% Strength Medium to unlock it", fg='red', font=('Book Antiqua', 11))
        if balance_easy_accuracy < 69:
            bm['state'] = DISABLED
            bm.config(cursor="arrow")
            ToolTip(bm, msg="Balance Easy must be at least 70% to unlock it", anchor=CENTER,fg='red',font=('Book Antiqua', 11))
        if balance_easy_accuracy < 89 or balance_medium_accuracy < 69:
            bh['state'] = DISABLED
            bh.config(cursor="arrow")
            ToolTip(bh,msg="Must have at least 90% Balance Easy and \n70% Balance Medium to unlock it", fg='red', font=('Book Antiqua', 11))
        if flexibility_easy_accuracy < 69:
            fm['state'] = DISABLED
            fm.config(cursor="arrow")
            ToolTip(fm, msg="Flexibility Easy must be at least 70% to unlock it", anchor=CENTER,fg='red',font=('Book Antiqua', 11))
        if flexibility_easy_accuracy < 89 or flexibility_medium_accuracy < 69:
            fh['state'] = DISABLED
            fh.config(cursor="arrow")
            ToolTip(fh,msg="Must have at least 90% Flexibility Easy and \n70% Flexibility Medium to unlock it", fg='red', font=('Book Antiqua', 11))

    def end_frame_text(self,frame,progress):
        if progress >= 90:
            text = "Well Done"
        elif progress >= 70:
            text = "Good Job"
        elif progress >= 40:
            text = "Nice"
        elif progress >=1:
            text = "Keep Trying"
        else:
            text = "No Data"
        Label(frame, text=text, font=('Book Antiqua', 40), bg="#f8f2f2").grid(row=0, column=0)


    def practice_session_label(self, frame, display,fs, r,c,px,sticky):
        Label(frame, text=display, bg="#f8f2f2", font=('Book Antiqua', fs)).grid(row=r, column=c, padx=px, sticky=sticky)

    def practice_session_entry(self, frame, display, textvariable, fs, r,c_add,condition):
        if condition == 1:
            Label(frame, text=display, bg="#f8f2f2", font=('Book Antiqua', fs)).grid(row=r, column=0+c_add, padx=10, sticky=E)
            Entry(frame, textvariable=textvariable,width=5, font=('Book Antiqua', fs,),justify=CENTER).grid(row=r, column=1+c_add, padx=3)
            Label(frame, text="secs", bg="#f8f2f2", font=('Book Antiqua', fs)).grid(row=r, column=2+c_add, sticky=W)
        elif condition==2:
            Label(frame, text=display, bg="#f8f2f2", font=('Book Antiqua', fs)).grid(row=r, column=0+c_add, padx=10, sticky=E)
            Entry(frame, textvariable=textvariable,width=5, font=('Book Antiqua', fs,),justify=CENTER).grid(row=r, column=1+c_add, padx=3)

    def practice_checkbutton(self,frame,text,text2,var,fs,command,r,pady):
        Checkbutton(frame, text=text,variable=var, font=('Book Antiqua', fs), bg="#f8f2f2",command=command).grid(row=r, column=0, sticky=W)
        Label(frame, text=text2, font=('Book Antiqua', fs), bg="#f8f2f2").grid(row=r, column=1, padx=10,pady=pady)

    def practice_checkbutton2(self, frame, text, text2,var,fs,command,r):
        Label(frame, text="", font=('Book Antiqua', fs), bg="#f8f2f2").grid(row=r - 5, column=2, padx=30)
        Checkbutton(frame, text=text, variable=var,font=('Book Antiqua', fs), bg="#f8f2f2",command=command).grid(row=r-5, column=3, sticky=W)
        Label(frame, text=text2, font=('Book Antiqua', fs), bg="#f8f2f2").grid(row=r-5, column=4, padx=10)

    # def transaction_trace(self,submit_btn,cardNumber,expMonth,expYear,cvc):
    #     def check(*args):
    #         if (cardNumber.get() and expMonth.get() and expYear.get() and cvc.get()) == "":
    #             submit_btn.config(state=DISABLED, disabledforeground="#C0C0C0", cursor="arrow")
    #             ToolTip(submit_btn, msg="All field are required", fg="red", font=('Book Antiqua', 11))
    #         else:
    #             submit_btn.config(state=NORMAL, cursor="hand2")
    #
    #     check(0)
    #     cardNumber.trace('w', check)
    #     expMonth.trace("w", check)
    #     expYear.trace("w", check)
    #     cvc.trace("w", check)

    def credit_debit_design(self,b,cardNumber,expMonth,expYear,cvc):
        Label(b, text="", font=('Book Antiqua', 23), fg="#7163ba", bg='#f8f2f2').grid(row=0, column=0,
                                                                                      padx=60)  # for left margin
        Label(b, text="Credit/Debit Card", font=('Book Antiqua', 30, "bold"), fg="#7163ba", bg='#f8f2f2').grid(row=0,
                                                                                                               column=1,
                                                                                                               pady=5,
                                                                                                               columnspan=3)

        Label(b, textvariable=cardNumber, text="Card Number", font=('Book Antiqua', 23), fg="#7163ba",
              bg='#f8f2f2').grid(row=1, column=1)
        Label(b, textvariable=expMonth, text="Expiration Month", font=('Book Antiqua', 23), fg="#7163ba",
              bg='#f8f2f2').grid(row=2, column=1)
        Label(b, textvariable=expYear, text="Expiration Year", font=('Book Antiqua', 23), fg="#7163ba",
              bg='#f8f2f2').grid(row=3, column=1)
        Label(b, textvariable=cvc, text="CVC", font=('Book Antiqua', 23), fg="#7163ba", bg='#f8f2f2').grid(row=4,
                                                                                                           column=1)

        Label(b, text=":", font=('Book Antiqua', 23), fg="#7163ba", bg='#f8f2f2').grid(row=1, column=2)
        Label(b, text=":", font=('Book Antiqua', 23), fg="#7163ba", bg='#f8f2f2').grid(row=2, column=2)
        Label(b, text=":", font=('Book Antiqua', 23), fg="#7163ba", bg='#f8f2f2').grid(row=3, column=2)
        Label(b, text=":", font=('Book Antiqua', 23), fg="#7163ba", bg='#f8f2f2').grid(row=4, column=2)

        Entry(b, font=('Book Antiqua', 18), justify=CENTER, width=20).grid(row=1, column=3, padx=10)
        Entry(b, font=('Book Antiqua', 18), justify=CENTER, width=8).grid(row=2, column=3, padx=10, sticky=W)
        Entry(b, font=('Book Antiqua', 18), justify=CENTER, width=8).grid(row=3, column=3, padx=10, sticky=W)
        Entry(b, font=('Book Antiqua', 18), justify=CENTER, width=8).grid(row=4, column=3, padx=10, sticky=W)

        Button(b, text="Submit", font=('Book Antiqua', 20), fg="#f8f2f2", bg="#7163BA", cursor="hand2", ).grid(row=5,
                                                                                                               column=1,
                                                                                                               columnspan=3,
                                                                                                               pady=10)

class yoga_function:
    def yoganame_pady(self,k):
        if k == 1:pady = 82
        elif k == 2:pady = 33
        elif k == 3:pady = 17
        elif k == 4:pady = 9
        else:pady = 0

        return pady

    def int_only(self,limit,empty,command):

        s1 = StringVar()
        s1.set(empty)
        s1.trace('w', lambda *args: command(s1, limit, empty, *args))

        return s1

    def set_time_formula(self,yogatime,user_want_pose,lp,preptime,cdtime):
        if user_want_pose>0:x=1
        else: x=0

        second = int((((yogatime * user_want_pose) + (preptime * user_want_pose)) * (lp+1)) + ((cdtime * lp) * x))

        if second >=3600:
            minutes = int(second/60)
            hrs, mins = divmod(minutes, 60)
            if hrs == 1: hrs_text = "1 hr"
            else: hrs_text = f'{hrs} hrs'

            if mins == 0: mins_text = ""
            elif mins == 1: mins_text = "and 1 min"
            else: mins_text = f'and {mins} mins'

            convert = f'{hrs_text} {mins_text}'

        elif second >=60:
            mins, secs = divmod(second, 60)
            if mins == 1: mins_text = "1 min"
            else: mins_text = f'{mins} mins'

            if secs == 0: secs_text = ""
            elif secs == 1: secs_text = "and 1 sec"
            else: secs_text = f'and {secs} secs'

            convert = f'{mins_text} {secs_text}'

        else:
            convert = f'{second} secs'

        return convert

    def open_setting(self):
        with open('setting.txt', 'r+') as file:
            file_data = file.read()
            details = file_data.split('\n')

            # for level of camera detection
            detection = details[0]
            detection_number = detection[-1]
            # for music theme
            theme = details[1]
            #for volume
            volume = details[2]
            song_playing = details[3]

        return int(detection_number), theme, volume, song_playing

class gmail_verification:
    def check(self,email_receiver):
        verification_number = random.randint(1000, 9999)

        email_sender = 'lefthope8@gmail.com'
        email_password = 'hqpyempaatyktlej'

        pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        if re.match(pat,email_receiver):
            # Set the subject and body of the email
            subject = 'Check your verification number!'
            body = f"""[Yoga with LeAnne] Verification Code: {verification_number}. Do not share this code with others."""

            em = EmailMessage()
            em['From'] = email_sender
            em['To'] = email_receiver
            em['Subject'] = subject
            em.set_content(body)

            # Add SSL (layer of security)
            context = ssl.create_default_context()

            # Log in and send the email
            try:
                with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                    smtp.login(email_sender, email_password)
                    smtp.sendmail(email_sender, email_receiver, em.as_string())

                return verification_number
            except:
                print("It seems that there is a problem in sending verification codes. Check your internet conncection")

        else:
            print("Invalid Email")

class yoga_cert:
    def create_cert(self,user_name):
        yoga_cert_path = os.path.abspath("images/yoga_certt.png")
        path = yoga_cert_path

        # path = r'C:\Users\arris\PycharmProjects\yoga\images\yoga_certt.png'

        # Reading an image in default mode
        image = cv2.imread(path)

        font = cv2.FONT_HERSHEY_COMPLEX
        org = (345, 400)
        fontScale = 1
        color = (0, 0, 0)
        thickness = 2
        yoga_user_name = user_name
        image = cv2.putText(image, yoga_user_name, org, font, fontScale, color, thickness, cv2.LINE_AA)
        # cv2.imshow("NAmme", image)
        # cv2.waitKey(0)

        directory = filedialog.askdirectory(title="Select a directory in which to save the certificate.")

        os.chdir(directory)
        filename = 'YogawithLeanne Certifcate.jpg'
        cv2.imwrite(filename, image)

