from PyQt5 import Qt, QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QApplication, QPushButton
from PyQt5.QtCore import QSize, QTimer    
from PyQt5.QtGui import QIcon

import tensorflow as tf
import cv2
import numpy as np

from utils import label_map_util
from utils import visualization_utils as vis_util
from threading import Thread
from collections import deque
from datetime import datetime


import qdarkstyle
import time
import sys
import cv2
import imutils
import csv
import os


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 544)
        MainWindow.setMaximumSize(QtCore.QSize(650, 544))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(100, 0, 530, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.url = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.url.setFont(font)
        self.url.setObjectName("url")
        self.horizontalLayout.addWidget(self.url)
        self.username = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.username.setFont(font)
        self.username.setObjectName("username")
        self.horizontalLayout.addWidget(self.username)
        self.password = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.password.setFont(font)
        self.password.setObjectName("password")
        self.horizontalLayout.addWidget(self.password)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 80, 31, 391))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_1.setObjectName("label_1")
        self.verticalLayout.addWidget(self.label_1)
        self.url1 = QtWidgets.QLineEdit(self.centralwidget)
        self.url1.setGeometry(QtCore.QRect(40, 90, 181, 21))
        self.url1.setObjectName("url1")
        #self.url1.setFrame(False)
        self.usr1 = QtWidgets.QLineEdit(self.centralwidget)
        self.usr1.setGeometry(QtCore.QRect(260, 90, 131, 21))
        self.usr1.setObjectName("usr1")
        self.url2 = QtWidgets.QLineEdit(self.centralwidget)
        self.url2.setGeometry(QtCore.QRect(40, 140, 181, 21))
        self.url2.setObjectName("url2")
        self.url3 = QtWidgets.QLineEdit(self.centralwidget)
        self.url3.setGeometry(QtCore.QRect(40, 190, 181, 21))
        self.url3.setObjectName("url3")
        self.url4 = QtWidgets.QLineEdit(self.centralwidget)
        self.url4.setGeometry(QtCore.QRect(40, 240, 181, 21))
        self.url4.setObjectName("url4")
        self.url5 = QtWidgets.QLineEdit(self.centralwidget)
        self.url5.setGeometry(QtCore.QRect(40, 290, 181, 21))
        self.url5.setObjectName("url5")
        self.url6 = QtWidgets.QLineEdit(self.centralwidget)
        self.url6.setGeometry(QtCore.QRect(40, 340, 181, 21))
        self.url6.setObjectName("url6")
        self.url7 = QtWidgets.QLineEdit(self.centralwidget)
        self.url7.setGeometry(QtCore.QRect(40, 390, 181, 21))
        self.url7.setObjectName("url7")
        self.url8 = QtWidgets.QLineEdit(self.centralwidget)
        self.url8.setGeometry(QtCore.QRect(40, 440, 181, 21))
        self.url8.setObjectName("url8")
        self.usr2 = QtWidgets.QLineEdit(self.centralwidget)
        self.usr2.setGeometry(QtCore.QRect(260, 140, 131, 21))
        self.usr2.setObjectName("usr2")
        self.usr3 = QtWidgets.QLineEdit(self.centralwidget)
        self.usr3.setGeometry(QtCore.QRect(260, 190, 131, 21))
        self.usr3.setObjectName("usr3")
        self.usr4 = QtWidgets.QLineEdit(self.centralwidget)
        self.usr4.setGeometry(QtCore.QRect(260, 240, 131, 21))
        self.usr4.setObjectName("usr4")
        self.usr8 = QtWidgets.QLineEdit(self.centralwidget)
        self.usr8.setGeometry(QtCore.QRect(260, 440, 131, 21))
        self.usr8.setObjectName("usr8")
        self.usr7 = QtWidgets.QLineEdit(self.centralwidget)
        self.usr7.setGeometry(QtCore.QRect(260, 390, 131, 21))
        self.usr7.setObjectName("usr7")
        self.usr6 = QtWidgets.QLineEdit(self.centralwidget)
        self.usr6.setGeometry(QtCore.QRect(260, 340, 131, 21))
        self.usr6.setObjectName("usr6")
        self.usr5 = QtWidgets.QLineEdit(self.centralwidget)
        self.usr5.setGeometry(QtCore.QRect(260, 290, 131, 21))
        self.usr5.setObjectName("usr5")
        self.psw1 = QtWidgets.QLineEdit(self.centralwidget)
        self.psw1.setGeometry(QtCore.QRect(430, 90, 131, 21))
        self.psw1.setObjectName("psw1")
        self.psw2 = QtWidgets.QLineEdit(self.centralwidget)
        self.psw2.setGeometry(QtCore.QRect(430, 140, 131, 21))
        self.psw2.setObjectName("psw2")
        self.psw3 = QtWidgets.QLineEdit(self.centralwidget)
        self.psw3.setGeometry(QtCore.QRect(430, 190, 131, 21))
        self.psw3.setObjectName("psw3")
        self.psw4 = QtWidgets.QLineEdit(self.centralwidget)
        self.psw4.setGeometry(QtCore.QRect(430, 240, 131, 21))
        self.psw4.setObjectName("psw4")
        self.psw5 = QtWidgets.QLineEdit(self.centralwidget)
        self.psw5.setGeometry(QtCore.QRect(430, 290, 131, 21))
        self.psw5.setObjectName("psw5")
        self.psw6 = QtWidgets.QLineEdit(self.centralwidget)
        self.psw6.setGeometry(QtCore.QRect(430, 340, 131, 21))
        self.psw6.setObjectName("psw6")
        self.psw7 = QtWidgets.QLineEdit(self.centralwidget)
        self.psw7.setGeometry(QtCore.QRect(430, 390, 131, 21))
        self.psw7.setObjectName("psw7")
        self.psw8 = QtWidgets.QLineEdit(self.centralwidget)
        self.psw8.setGeometry(QtCore.QRect(430, 440, 131, 21))
        self.psw8.setObjectName("psw8")
        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(180, 480, 113, 32))
        self.save.setObjectName("save")
        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.setGeometry(QtCore.QRect(380, 480, 113, 32))
        self.cancel.setObjectName("cancel")
        self.del1 = QtWidgets.QPushButton(self.centralwidget)
        self.del1.setGeometry(QtCore.QRect(565, 90, 16, 16))
        self.del1.setMaximumSize(QtCore.QSize(16, 16))
        self.del1.setToolTip("")
        self.del1.setStyleSheet("background: transparent; border: none;")
        self.del1.setText("")
        icon = QtGui.QIcon.fromTheme(scriptDir + os.path.sep + 'deleteIcon.png')
        self.del1.setIcon(icon)
        self.del1.setObjectName("del1")
        #self.del1.setFrame(False)
        self.del2 = QtWidgets.QPushButton(self.centralwidget)
        self.del2.setGeometry(QtCore.QRect(565, 140, 16, 16))
        self.del2.setMaximumSize(QtCore.QSize(16, 16))
        self.del2.setToolTip("")
        self.del2.setStyleSheet("background: transparent; border: none;")
        self.del2.setText("")
        icon = QtGui.QIcon.fromTheme(scriptDir + os.path.sep + 'deleteIcon.png')
        self.del2.setIcon(icon)
        self.del2.setObjectName("del2")
        self.del3 = QtWidgets.QPushButton(self.centralwidget)
        self.del3.setGeometry(QtCore.QRect(565, 190, 16, 16))
        self.del3.setMaximumSize(QtCore.QSize(16, 16))
        self.del3.setToolTip("")
        self.del3.setStyleSheet("background: transparent; border: none;")
        self.del3.setText("")
        icon = QtGui.QIcon.fromTheme(scriptDir + os.path.sep + 'deleteIcon.png')
        self.del3.setIcon(icon)
        self.del3.setObjectName("del3")
        self.del4 = QtWidgets.QPushButton(self.centralwidget)
        self.del4.setGeometry(QtCore.QRect(565, 240, 16, 16))
        self.del4.setMaximumSize(QtCore.QSize(16, 16))
        self.del4.setToolTip("")
        self.del4.setStyleSheet("background: transparent; border: none;")
        self.del4.setText("")
        icon = QtGui.QIcon.fromTheme(scriptDir + os.path.sep + 'deleteIcon.png')
        self.del4.setIcon(icon)
        self.del4.setObjectName("del4")
        self.del5 = QtWidgets.QPushButton(self.centralwidget)
        self.del5.setGeometry(QtCore.QRect(565, 290, 16, 16))
        self.del5.setMaximumSize(QtCore.QSize(16, 16))
        self.del5.setToolTip("")
        self.del5.setStyleSheet("background: transparent; border: none;")
        self.del5.setText("")
        icon = QtGui.QIcon.fromTheme(scriptDir + os.path.sep + 'deleteIcon.png')
        self.del5.setIcon(icon)
        self.del5.setObjectName("del5")
        self.del6 = QtWidgets.QPushButton(self.centralwidget)
        self.del6.setGeometry(QtCore.QRect(565, 340, 16, 16))
        self.del6.setMaximumSize(QtCore.QSize(16, 16))
        self.del6.setToolTip("")
        self.del6.setStyleSheet("background: transparent; border: none;")
        self.del6.setText("")
        icon = QtGui.QIcon.fromTheme(scriptDir + os.path.sep + 'deleteIcon.png')
        self.del6.setIcon(icon)
        self.del6.setObjectName("del6")
        self.del7 = QtWidgets.QPushButton(self.centralwidget)
        self.del7.setGeometry(QtCore.QRect(565, 390, 16, 16))
        self.del7.setMaximumSize(QtCore.QSize(16, 16))
        self.del7.setToolTip("")
        self.del7.setStyleSheet("background: transparent; border: none;")
        self.del7.setText("")
        icon = QtGui.QIcon.fromTheme(scriptDir + os.path.sep + 'deleteIcon.png')
        self.del7.setIcon(icon)
        self.del7.setObjectName("del7")
        self.del8 = QtWidgets.QPushButton(self.centralwidget)
        self.del8.setGeometry(QtCore.QRect(565, 440, 16, 16))
        self.del8.setMaximumSize(QtCore.QSize(16, 16))
        self.del8.setToolTip("")
        self.del8.setStyleSheet("background: transparent; border: none;")
        self.del8.setText("")
        icon = QtGui.QIcon.fromTheme(scriptDir + os.path.sep + 'deleteIcon.png')
        self.del8.setIcon(icon)
        self.del8.setObjectName("del8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.del1.clicked.connect(self.psw1.clear)
        self.del1.clicked.connect(self.usr1.clear)
        self.del1.clicked.connect(self.url1.clear)
        self.del2.clicked.connect(self.psw2.clear)
        self.del2.clicked.connect(self.usr2.clear)
        self.del2.clicked.connect(self.url2.clear)
        self.del3.clicked.connect(self.psw3.clear)
        self.del3.clicked.connect(self.usr3.clear)
        self.del3.clicked.connect(self.url3.clear)
        self.del4.clicked.connect(self.psw4.clear)
        self.del4.clicked.connect(self.usr4.clear)
        self.del4.clicked.connect(self.url4.clear)
        self.del5.clicked.connect(self.psw5.clear)
        self.del5.clicked.connect(self.usr5.clear)
        self.del5.clicked.connect(self.url5.clear)
        self.del6.clicked.connect(self.psw6.clear)
        self.del6.clicked.connect(self.usr6.clear)
        self.del6.clicked.connect(self.url6.clear)
        self.del7.clicked.connect(self.psw7.clear)
        self.del7.clicked.connect(self.usr7.clear)
        self.del7.clicked.connect(self.url7.clear)
        self.del8.clicked.connect(self.psw8.clear)
        self.del8.clicked.connect(self.usr8.clear)
        self.del8.clicked.connect(self.url8.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
        self.cancel.clicked.connect(MainWindow.close)

        self.cameraInfo = [[self.url1,self.usr1,self.psw1],
                        [self.url2,self.usr2,self.psw2],
                        [self.url3,self.usr3,self.psw3],
                        [self.url4,self.usr4,self.psw4],
                        [self.url5,self.usr5,self.psw5],
                        [self.url6,self.usr6,self.psw6],
                        [self.url7,self.usr7,self.psw7],
                        [self.url8,self.usr8,self.psw8]
                        ]

        self.init_fields()



        self.save.clicked.connect(self.write_to_csv)
        self.save.clicked.connect(self.read_from_csv)
        self.save.clicked.connect(MainWindow.close)

        
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ADD/Remove Cameras"))
        self.url.setText(_translate("MainWindow", "URL"))
        self.username.setText(_translate("MainWindow", "UserName"))
        self.password.setText(_translate("MainWindow", "Password"))
        self.label_8.setText(_translate("MainWindow", "1."))
        self.label_7.setText(_translate("MainWindow", "2."))
        self.label_6.setText(_translate("MainWindow", "3."))
        self.label_5.setText(_translate("MainWindow", "4."))
        self.label_4.setText(_translate("MainWindow", "5."))
        self.label_3.setText(_translate("MainWindow", "6."))
        self.label_2.setText(_translate("MainWindow", "7."))
        self.label_1.setText(_translate("MainWindow", "8."))
        self.save.setText(_translate("MainWindow", "Save"))
        self.cancel.setText(_translate("MainWindow", "Cancel"))

    def button_assignment(self):
        a = self.psw1.text()
        print(a)

    def write_to_csv(self):
        '''
        input : List[List[str]]

        '''
        # name of csv file  
        filename = "Cameras_CONFIG.csv"
        fields = ['URL','USERNAME','PASSWORD']
        row = len(self.cameraInfo)
        col = len(self.cameraInfo[0])
        # writing to csv file  
        with open(filename, 'w+') as csvfile:  
            # creating a csv writer object  
            csvwriter = csv.writer(csvfile)  
            # writing the fields  
            csvwriter.writerow(fields)  
            for i in range(row):
                if self.cameraInfo[i][0].text() != "":
                    add_row = []
                    for j in range(col):
                        add_row.append(self.cameraInfo[i][j].text())

                    csvwriter.writerow(add_row)

    def read_from_csv(self):
        '''
        Read Cameras Info to store in A Dictionary to be sent to Hassan

        '''
        filename = "cameras_config.csv"
        firstLine = True
        dic = {}
        with open(filename,'r+') as csv_file:
            csv_reader = csv.reader(csv_file)
            count = 1
            for row in csv_reader:
                if firstLine:
                    firstLine = False
                else:
                    dic[count] = row
                    count += 1

        for i in range(len(dic)):
            #username = dic[i+1][1]
            #password = dic[i+1][2]
            if len(dic[i+1][0]) < 4:
                globals()['camera' + str(i)] = int(dic[i+1][0])
            else:
                globals()['camera' + str(i)] = str(dic[i+1][0])
            print(type(dic[i+1][0]))
        print(dic)
        print(camera0)
        print(camera1)
        add_cameras(len(dic), camera0, camera1, camera2, camera3, camera4, camera5, camera6, camera7, camera8)
        #print(dic)
        #return dic

    def init_fields(self):
        '''
        '''
        filename = "cameras_config.csv"
        firstLine = True
        with open(filename, 'r+') as csv_file:
            csv_reader = csv.reader(csv_file)
            j = 0
            for row in csv_reader:
                if firstLine:
                    firstLine = False
                else:
                    for i in range(len(row)):
                        self.cameraInfo[j][i].setText(row[i])

                    j += 1


class Ui_SecondWindow(object):
    
    def setupUi(self, SecondWindow):
        SecondWindow.setObjectName("SecondWindow")
        SecondWindow.resize(400, 300)
        self.centralWidget = QtWidgets.QWidget(SecondWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 130, 191, 23))
        self.pushButton.setObjectName("pushButton")
        SecondWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(SecondWindow)
        QtCore.QMetaObject.connectSlotsByName(SecondWindow)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("SecondWindow", "SecondWindow"))
        self.pushButton.setText(_translate("SecondWindow", "Congratz !"))

class CameraWidget(QtWidgets.QWidget):
    """Independent camera feed
    Uses threading to grab IP camera frames in the background

    @param width - Width of the video frame
    @param height - Height of the video frame
    @param stream_link - IP/RTSP/Webcam link
    @param cam_number - IP/RTSP/Webcam link
    @param aspect_ratio - Whether to maintain frame aspect ratio or force into fraame
    """

    def __init__(self, width, height, stream_link=0, cam_number=0, aspect_ratio=False, parent=None, deque_size=1):
        super(CameraWidget, self).__init__(parent)

        # Initialize deque used to store frames read from the stream
        self.deque = deque(maxlen=deque_size)

        # Slight offset is needed since PyQt layouts have a built in padding
        # So add offset to counter the padding 
        self.offset = 16
        self.screen_width = width - self.offset
        self.screen_height = height - self.offset
        self.maintain_aspect_ratio = aspect_ratio

        self.camera_stream_link = stream_link

        self.camera_number = cam_number

        # Flag to check if camera is valid/working
        self.online = False
        self.capture = None
        self.video_frame = QtWidgets.QLabel()

        self.load_network_stream()

        # Start background frame grabbing
        self.get_frame_thread = Thread(target=self.get_frame, args=())
        self.get_frame_thread.daemon = True
        self.get_frame_thread.start()

        # Periodically set video frame to display
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.set_frame)
        self.timer.start(.5)
        self.PATH_TO_FROZEN_GRAPH_GUN = '/Users/abdelrahmanhegazy/Desktop/SSD_MODEL/newmodel/frozen_inference_graph.pb'
        self.PATH_TO_LABEL_MAP_GUN = '/Users/abdelrahmanhegazy/Desktop/SSD_MODEL/newmodel/label_map.pbtxt'
        self.NUM_CLASSES_GUN= 1
        self.gun_graph = tf.Graph()
        with self.gun_graph.as_default():
          od_graph_def_guns = tf.compat.v1.GraphDef()
          with tf.io.gfile.GFile(self.PATH_TO_FROZEN_GRAPH_GUN, 'rb') as fid1:
              serialized_graph1 = fid1.read()
              od_graph_def_guns.ParseFromString(serialized_graph1)
              tf.import_graph_def(od_graph_def_guns, name='')

          self.gun_session = tf.compat.v1.Session(graph=self.gun_graph)

        self.label_map_gun = label_map_util.load_labelmap(self.PATH_TO_LABEL_MAP_GUN)
        self.categories_gun = label_map_util.convert_label_map_to_categories(self.label_map_gun, max_num_classes=self.NUM_CLASSES_GUN, use_display_name=True)
        self.category_index_gun = label_map_util.create_category_index(self.categories_gun)

        # Extract image tensor
        self.gun_image_tensor = self.gun_graph.get_tensor_by_name('image_tensor:0')
        # Extract detection boxes
        self.gun_boxes = self.gun_graph.get_tensor_by_name('detection_boxes:0')
        # Extract detection scores
        self.gun_scores = self.gun_graph.get_tensor_by_name('detection_scores:0')
        # Extract detection classes
        self.gun_classes = self.gun_graph.get_tensor_by_name('detection_classes:0')
        # Extract number of detections
        self.gun_num_detections = self.gun_graph.get_tensor_by_name(
                          'num_detections:0')

        #self.PATH_TO_FROZEN_GRAPH_FIGHT = '/Users/abdelrahmanhegazy/Desktop/fight-model/frozen_inference_graph.pb'
        #self.PATH_TO_LABEL_MAP_FIGHT = '/Users/abdelrahmanhegazy/Desktop/fight-model/ava_label_map_v2.1 copy.pbtxt'
        # path to the frozen graph:
        self.PATH_TO_FROZEN_GRAPH_OBJECT_DETECTION = '/Users/abdelrahmanhegazy/Desktop/ssd_mobilenet_v2_coco_2018_03_29/frozen_inference_graph.pb'
        # path to the label map
        self.PATH_TO_LABEL_MAP_OBJECT_DETECTION = '/Users/abdelrahmanhegazy/Desktop/SSD_MODEL/mscoco_label_map.pbtxt'

        self.NUM_CLASSES_OBJECTS= 90
        self.object_graph = tf.Graph()
        with self.object_graph.as_default():
            od_graph_def_object_detection = tf.compat.v1.GraphDef()
            with tf.io.gfile.GFile(self.PATH_TO_FROZEN_GRAPH_OBJECT_DETECTION, 'rb') as fid2:
                serialized_graph2 = fid2.read()
                od_graph_def_object_detection.ParseFromString(serialized_graph2)
                tf.import_graph_def(od_graph_def_object_detection, name='')

            self.object_session = tf.compat.v1.Session(graph=self.object_graph)

        self.label_map_object_detection = label_map_util.load_labelmap(self.PATH_TO_LABEL_MAP_OBJECT_DETECTION)
        self.categories_object_detection = label_map_util.convert_label_map_to_categories(self.label_map_object_detection, max_num_classes=self.NUM_CLASSES_OBJECTS, use_display_name=True)
        self.category_index_object_detection = label_map_util.create_category_index(self.categories_object_detection)

        # Extract image tensor
        self.object_image_tensor = self.object_graph.get_tensor_by_name('image_tensor:0')
        # Extract detection boxes
        self.object_boxes = self.object_graph.get_tensor_by_name('detection_boxes:0')
        # Extract detection scores
        self.object_scores = self.object_graph.get_tensor_by_name('detection_scores:0')
        # Extract detection classes
        self.object_classes = self.object_graph.get_tensor_by_name('detection_classes:0')
        # Extract number of detections
        self.object_num_detections = self.object_graph.get_tensor_by_name(
                          'num_detections:0')

        print("model initialized")

        print('Started camera: {}'.format(self.camera_stream_link))
        #camera_stream_link += 1

    def load_network_stream(self):
        """Verifies stream link and open new stream if valid"""

        def load_network_stream_thread():
            if self.verify_network_stream(self.camera_stream_link):
                self.capture = cv2.VideoCapture(self.camera_stream_link)
                self.online = True
        self.load_stream_thread = Thread(target=load_network_stream_thread, args=())
        self.load_stream_thread.daemon = True
        self.load_stream_thread.start()

    def verify_network_stream(self, link):
        """Attempts to receive a frame from given link"""

        cap = cv2.VideoCapture(link)
        if not cap.isOpened():
            return False
        cap.release()
        return True

    def get_frame(self):
        """Reads frame, resizes, and converts image to pixmap"""

        while True:
            try:
                if self.capture.isOpened() and self.online:
                    # Read next frame from stream and insert into deque
                    status, frame = self.capture.read()
                    if status:
                        self.deque.append(frame)
                    else:
                        self.capture.release()
                        self.online = False
                else:
                    # Attempt to reconnect
                    print('attempting to reconnect', self.camera_stream_link)
                    self.load_network_stream()
                    self.spin(2)
                self.spin(.001)
            except AttributeError:
                pass

    def spin(self, seconds):
        """Pause for set amount of seconds, replaces time.sleep so program doesnt stall"""

        time_end = time.time() + seconds
        while time.time() < time_end:
            QtWidgets.QApplication.processEvents()

    def set_frame(self):
        """Sets pixmap image to video frame"""

        if not self.online:
            self.spin(1)
            return

        if self.deque and self.online:
            # Grab latest frame
            frame = self.deque[-1]
            #detectedframe = video.model(frame)
            image_np_expanded = np.expand_dims(frame, axis=0)
            (boxes, scores, classes, num_detections) = self.gun_session.run(
                [self.gun_boxes, self.gun_scores, self.gun_classes, self.gun_num_detections],
                feed_dict={self.gun_image_tensor: image_np_expanded})
            vis_util.visualize_boxes_and_labels_on_image_array(
                frame,
                np.squeeze(boxes),
                np.squeeze(classes).astype(np.int32),
                np.squeeze(scores),
                self.category_index_gun,
                use_normalized_coordinates=True,
                line_thickness=3,
           )
           

            '''
            image_np_expanded = np.expand_dims(frame, axis=0)

            (boxes, scores, classes, num_detections) = self.fight_session.run(
                [self.fight_boxes, self.fight_scores, self.fight_classes, self.fight_num_detections],
                feed_dict={self.fight_image_tensor: image_np_expanded})
            # Visualization of the results of a detection.
            vis_util.visualize_boxes_and_labels_on_image_array(
                frame,
                np.squeeze(boxes),
                np.squeeze(classes).astype(np.int32),
                np.squeeze(scores),
                self.category_index_fight,
                use_normalized_coordinates=True,
                line_thickness=6,
               )
            #detectedframe = video.run_model(frame)
            '''
            #image_np_expanded = np.expand_dims(frame, axis=0)
            (boxes1, scores1, classes1, num_detections1) = self.object_session.run(
                [self.object_boxes, self.object_scores, self.object_classes, self.object_num_detections],
                feed_dict={self.object_image_tensor: image_np_expanded})
            # Visualization of the results of a detection.
            vis_util.visualize_boxes_and_labels_on_image_array(
                frame,
                np.squeeze(boxes1),
                np.squeeze(classes1).astype(np.int32),
                np.squeeze(scores1),
                self.category_index_object_detection,
                use_normalized_coordinates=True,
                line_thickness=3,
               )

            # Keep frame aspect ratio
            if self.maintain_aspect_ratio:
                self.frame = imutils.resize(frame, width=self.screen_width)
            # Force resize
            else:
                self.frame = cv2.resize(frame, (self.screen_width, self.screen_height))

            # Add timestamp to cameras
            cv2.rectangle(self.frame, (self.screen_width-190,0), (self.screen_width,50), color=(0,0,0), thickness=-1)
            cv2.putText(self.frame, datetime.now().strftime('%H:%M:%S'), (self.screen_width-180,37), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255,255,255), lineType=cv2.LINE_AA)


            # Add name to cameras
            cv2.rectangle(self.frame, (0,0), (130,50), color=(0,0,0), thickness=-1)
            cv2.putText(self.frame, 'Cam{}'.format(self.camera_number) , (10,37), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255,255,255), lineType=cv2.LINE_AA)


            # Convert to pixmap and set to video frame
            #detectedframe = model(self.frame)
            self.img = QtGui.QImage(self.frame, self.frame.shape[1], self.frame.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
            self.pix = QtGui.QPixmap.fromImage(self.img)
            self.video_frame.setPixmap(self.pix)

    def get_video_frame(self):
        return self.video_frame



def exit_application():
    """Exit program event handler"""

    sys.exit(1)

def add_cameras(cam, camera0, camera1, camera2, camera3, camera4, camera5, camera6, camera7, camera8):

    for i in reversed(range(ml.count())): 
        widgetToRemove = ml.itemAt(i).widget()
        # remove it from the layout list
        ml.removeWidget(widgetToRemove)
        # remove it from the gui
        widgetToRemove.setParent(None)

    camNum = cam

    # Create camera widgets

    if camNum < 2:
        screenSize = 1
    elif camNum < 5:
        screenSize = 2
    elif camNum < 10:
        screenSize = 3
    
    print('Creating Camera Widgets...')
    zero = CameraWidget(screen_width//screenSize, screen_height//screenSize, camera0, 1)
    one = CameraWidget(screen_width//screenSize, screen_height//screenSize, camera1, 2)
    #two = CameraWidget(screen_width//screenSize, screen_height//screenSize, camera2, 3)
    #three = CameraWidget(screen_width//screenSize, screen_height//screenSize, camera3, 4)
    #four = CameraWidget(screen_width//screenSize, screen_height//screenSize, camera4, 5)
    #five = CameraWidget(screen_width//screenSize, screen_height//screenSize, camera5, 6)
    #six = CameraWidget(screen_width//screenSize, screen_height//screenSize, camera6, 7)
    #seven = CameraWidget(screen_width//screenSize, screen_height//screenSize, camera7, 8)
    #eight = CameraWidget(screen_width//screenSize, screen_height//screenSize, camera8, 9)


    #camNUM = self.camNUM
    #elf.camNUM = camNUM

    print('Adding widgets to layout...')
    if camNum == 0:
        print('NO Camera...')
    elif camNum == 1:
        ml.addWidget(zero.get_video_frame(),0,0,1,1)
        #ml.addWidget(one.get_video_frame(),0,1,1,1)
        #ml.addWidget(two.get_video_frame(),0,2,1,1)
        #ml.addWidget(three.get_video_frame(),1,0,1,1)
        #ml.addWidget(four.get_video_frame(),1,1,1,1)
        #ml.addWidget(five.get_video_frame(),1,2,1,1)
        #ml.addWidget(six.get_video_frame(),2,0,1,1)
        #ml.addWidget(seven.get_video_frame(),2,1,1,1)
        #ml.addWidget(eight.get_video_frame(),3,2,1,1)
    elif camNum == 2:
        ml.addWidget(zero.get_video_frame(),0,0,1,1)
        ml.addWidget(one.get_video_frame(),0,1,1,1)
        #ml.addWidget(two.get_video_frame(),0,2,1,1)
        #ml.addWidget(three.get_video_frame(),1,0,1,1)
        #ml.addWidget(four.get_video_frame(),1,1,1,1)
        #ml.addWidget(five.get_video_frame(),1,2,1,1)
        #ml.addWidget(six.get_video_frame(),2,0,1,1)
        #ml.addWidget(seven.get_video_frame(),2,1,1,1)
        #ml.addWidget(eight.get_video_frame(),3,2,1,1)
    elif camNum == 3:
        ml.addWidget(zero.get_video_frame(),0,0,1,1)
        ml.addWidget(one.get_video_frame(),0,1,1,1)
        ml.addWidget(two.get_video_frame(),1,0,1,1)
        #ml.addWidget(three.get_video_frame(),1,0,1,1)
        #ml.addWidget(four.get_video_frame(),1,1,1,1)
        #ml.addWidget(five.get_video_frame(),1,2,1,1)
        #ml.addWidget(six.get_video_frame(),2,0,1,1)
        #ml.addWidget(seven.get_video_frame(),2,1,1,1)
        #ml.addWidget(eight.get_video_frame(),3,2,1,1)
    elif camNum == 4:
        ml.addWidget(zero.get_video_frame(),0,0,1,1)
        ml.addWidget(one.get_video_frame(),0,1,1,1)
        ml.addWidget(two.get_video_frame(),1,0,1,1)
        ml.addWidget(three.get_video_frame(),1,1,1,1)
        #ml.addWidget(four.get_video_frame(),1,1,1,1)
        #ml.addWidget(five.get_video_frame(),1,2,1,1)
        #ml.addWidget(six.get_video_frame(),2,0,1,1)
        #ml.addWidget(seven.get_video_frame(),2,1,1,1)
        #ml.addWidget(eight.get_video_frame(),3,2,1,1)
    elif camNum == 5:
        ml.addWidget(zero.get_video_frame(),0,0,1,1)
        ml.addWidget(one.get_video_frame(),0,1,1,1)
        ml.addWidget(two.get_video_frame(),0,2,1,1)
        ml.addWidget(three.get_video_frame(),1,0,1,1)
        ml.addWidget(four.get_video_frame(),1,1,1,1)
        #ml.addWidget(five.get_video_frame(),1,2,1,1)
        #ml.addWidget(six.get_video_frame(),2,0,1,1)
        #ml.addWidget(seven.get_video_frame(),2,1,1,1)
        #ml.addWidget(eight.get_video_frame(),3,2,1,1)
    elif camNum == 6:
        ml.addWidget(zero.get_video_frame(),1,0,1,1)
        ml.addWidget(one.get_video_frame(),1,1,1,1)
        ml.addWidget(two.get_video_frame(),1,2,1,1)
        ml.addWidget(three.get_video_frame(),2,0,1,1)
        ml.addWidget(four.get_video_frame(),2,1,1,1)
        ml.addWidget(five.get_video_frame(),2,2,1,1)
        #ml.addWidget(six.get_video_frame(),2,0,1,1)
        #ml.addWidget(seven.get_video_frame(),2,1,1,1)
        #ml.addWidget(eight.get_video_frame(),3,2,1,1)
    elif camNum == 7:
        ml.addWidget(zero.get_video_frame(),1,0,1,1)
        ml.addWidget(one.get_video_frame(),1,1,1,1)
        ml.addWidget(two.get_video_frame(),1,2,1,1)
        ml.addWidget(three.get_video_frame(),2,0,1,1)
        ml.addWidget(four.get_video_frame(),2,1,1,1)
        ml.addWidget(five.get_video_frame(),2,2,1,1)
        ml.addWidget(six.get_video_frame(),3,0,1,1)
        #ml.addWidget(seven.get_video_frame(),2,1,1,1)
        #ml.addWidget(eight.get_video_frame(),3,2,1,1)
    elif camNum == 8:
        ml.addWidget(zero.get_video_frame(),1,0,1,1)
        ml.addWidget(one.get_video_frame(),1,1,1,1)
        ml.addWidget(two.get_video_frame(),1,2,1,1)
        ml.addWidget(three.get_video_frame(),2,0,1,1)
        ml.addWidget(four.get_video_frame(),2,1,1,1)
        ml.addWidget(five.get_video_frame(),2,2,1,1)
        ml.addWidget(six.get_video_frame(),3,0,1,1)
        ml.addWidget(seven.get_video_frame(),3,1,1,1)
        #ml.addWidget(eight.get_video_frame(),3,2,1,1)
    elif camNum == 9:
        ml.addWidget(zero.get_video_frame(),1,0,1,1)
        ml.addWidget(one.get_video_frame(),1,1,1,1)
        ml.addWidget(two.get_video_frame(),1,2,1,1)
        ml.addWidget(three.get_video_frame(),2,0,1,1)
        ml.addWidget(four.get_video_frame(),2,1,1,1)
        ml.addWidget(five.get_video_frame(),2,2,1,1)
        ml.addWidget(six.get_video_frame(),3,0,1,1)
        ml.addWidget(seven.get_video_frame(),3,1,1,1)
        ml.addWidget(eight.get_video_frame(),3,2,1,1)
    
    mw.show()

class Controller:
    
    def __init__(self):
        pass
    
    def Show_FirstWindow(self):

        print('After 99 hours of trying out everything')
        add_cameras(camNum, camera0, camera1, camera2, camera3, camera4, camera5, camera6, camera7, camera8)
    
    def Show_SecondWindow(self):
        
        self.SecondWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.SecondWindow)
        #self.ui.pushButton.clicked.connect(self.Print)

        self.SecondWindow.show()

    def Print(self):
        print('After 99 hours of trying out everything')
        self.SecondWindow.close()
        self.Show_FirstWindow()


if __name__ == '__main__':

    # Create main application window
    app = QtWidgets.QApplication([])
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    #app.setStyle(Qt.QStyleFactory.create("Cleanlooks"))
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyside2'))
    mw = QtWidgets.QMainWindow()
    mw.setWindowTitle('Camera GUI')
    mw.setWindowFlags(QtCore.Qt.FramelessWindowHint)

    cw = QtWidgets.QWidget()
    ml = QtWidgets.QGridLayout()
    cw.setLayout(ml)
    mw.setCentralWidget(cw)
    mw.showMaximized()

    scriptDir = os.path.dirname(os.path.realpath(__file__))
    controller = Controller()
    secondWidget = Ui_MainWindow()
    # Dynamically determine screen width/height
    screen_width = QtWidgets.QApplication.desktop().screenGeometry().width()
    screen_height = QtWidgets.QApplication.desktop().screenGeometry().height()

    # Number of cameras
    camNum = 4

    # Screen width & height
    #screenSize = 1

    # Create Camera Widgets 
    username = ''
    password = ''

    # Stream links
    #camera0 = 'rtsp://192.168.1.4:8080/h264_ulaw.sdp'.format(username, password)
    camera0 = 0
    camera1 = 0
    camera2 = 0
    camera3 = 0
    camera4 = 0
    camera5 = 0
    camera6 = 0
    camera7 = 0
    camera8 = 0

    #Controller.Show_SecondWindow()




    # Add widgets to layout

    #add_cameras(camNum, camera0, camera1, camera2, camera3, camera4, camera5, camera6, camera7, camera8)

    #camNum += 1

    '''
    print('Adding widgets to layout...')
    ml.addWidget(zero.get_video_frame(),0,0,1,1)
    ml.addWidget(one.get_video_frame(),0,1,1,1)
    ml.addWidget(two.get_video_frame(),0,2,1,1)
    ml.addWidget(three.get_video_frame(),1,0,1,1)
    ml.addWidget(four.get_video_frame(),1,1,1,1)
    #ml.addWidget(five.get_video_frame(),1,2,1,1)
    #ml.addWidget(six.get_video_frame(),2,0,1,2)
    #ml.addWidget(seven.get_video_frame(),2,1,-2,1)
    #ml.addWidget(eight.get_video_frame(),2,2,1,1)
    '''

    print('Verifying camera credentials...')

    '''
    menubar = mw.menuBar()
    fileMenu = menubar.addMenu('Cameras')
    addAct = QAction('Add', mw)
    removeAct = QAction('Remove', mw)
    editAct = QAction('Edit', mw)
    fileMenu.addAction(addAct)
    fileMenu.addAction(removeAct)
    fileMenu.addAction(editAct)
    ''' 

    def addCall():
        print('Open')
        controller.Show_SecondWindow()
        

    def openCall():
        print('Add')
        #camera0 = 'rtsp://192.168.1.4:8080/h264_ulaw.sdp'.format(username, password)
        #camera0 = 0
        #ml.removeWidget(zero)
        #add_cameras(camNum)
        #camNum = 2
        #for i in reversed(range(ml.count())): 
        #    ml.itemAt(i).widget().setParent(None)
        '''
        for i in reversed(range(ml.count())): 
            widgetToRemove = ml.itemAt(i).widget()
            # remove it from the layout list
            ml.removeWidget(widgetToRemove)
            # remove it from the gui
            widgetToRemove.setParent(None)
        '''
        #camera0 = 'rtsp://192.168.1.4:8080/h264_ulaw.sdp'.format(username, password)
        #camera0 = 0
        #camNum = 2
        secondWidget.read_from_csv()
        #add_cameras(camNum, camera0, camera1, camera2, camera3, camera4, camera5, camera6, camera7, camera8)

    # Create new action
    addAction = QAction(QIcon('new.png'), '&ADD/Edit', mw)        
    addAction.setShortcut('Ctrl+A')
    addAction.setStatusTip('ADD/Edit')
    addAction.triggered.connect(addCall)

    # Create new action
    openAction = QAction(QIcon('open.png'), '&Refresh', mw)        
    openAction.setShortcut('Ctrl+R')
    openAction.setStatusTip('Refresh')
    openAction.triggered.connect(openCall)

    # Create menu bar and add action
    menuBar = mw.menuBar()
    cameraMenu = menuBar.addMenu('&Camera')
    cameraMenu.addAction(addAction)
    cameraMenu.addAction(openAction)

    #mw.update()

    #mw.show()

    #mw.update()

    #add_cameras(camNum)

    QtWidgets.QShortcut(QtGui.QKeySequence('Ctrl+Q'), mw, exit_application)

    if(sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtWidgets.QApplication.instance().exec_()

    #sys.exit(app.exec_())