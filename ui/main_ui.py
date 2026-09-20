import sys
import os
import json
from PyQt6 import QtCore, QtGui, QtWidgets



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        with open(r"C:\Users\maria\todolist\static\style.css", "r") as style_file:
            style_str=style_file.read()
            MainWindow.setStyleSheet(style_str)

            
        MainWindow.resize(1000,700) #arxikes diastaseis kai basic properties vasikoy parathiroy
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("To Do List")

        window_icon = QtGui.QIcon('./static/icons/list.svg') #main window icon
        MainWindow.setWindowIcon(window_icon)

        #central widget
        self.centralWidget = QtWidgets.QWidget(parent=MainWindow)
        MainWindow.setCentralWidget(self.centralWidget)

        #main layout toy central widget
        self.main_verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.main_verticalLayout.setContentsMargins(80,50,80,50)
        self.main_verticalLayout.setSpacing(20)

        # title frame
        self.title_frame = QtWidgets.QFrame(parent=self.centralWidget)
        self.title_frame.setMaximumSize(QtCore.QSize(16777215,60))
        self.title_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.title_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.title_frame.setObjectName("title_frame")

        #title section
        self.title_frame_horizontalLayout = QtWidgets.QHBoxLayout(self.title_frame)
        self.title_frame_horizontalLayout.setContentsMargins(10,10,10,10)

        #icon in the title
        self.icon_label=QtWidgets.QLabel(parent=self.title_frame)
        self.icon_label.setMinimumSize(QtCore.QSize(40,40))
        self.icon_label.setMaximumSize(QtCore.QSize(40,40))
        self.icon_label.setPixmap(QtGui.QPixmap("./static/icons.list.min.svg"))
        self.icon_label.setScaledContents(True)
        self.icon_label.setObjectName("icon_label")


        self,self.title_frame_horizontalLayout.addWidget(self.icon_label)

        self.title_label= QtWidgets.QLabel(parent=self.title_frame)
        self.title_label.setText("To Do list")
        self.title_label.setMinimumSize(QtCore.QSize(150,40))
        self.title_label.setObjectName("title_label")

        self.title_frame_horizontalLayout.addWidget(self.title_label)

        #frame gia task list
        self.task_frame=QtWidgets.QFrame(parent=self.centralWidget)
        self.task_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.task_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.task_frame.setObjectName("task_frame")

        self.task_verticalLayout=QtWidgets.QVBoxLayout(self.task_frame)
        self.task_verticalLayout.setContentsMargins(10,15,10,15)

        self.task_listView=QtWidgets.QListView(parent=self.task_frame)
        self.task_listView.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.task_listView.setDragDropMode(QtWidgets.QAbstractItemView.DragDropMode.DragOnly)
        self.task_listView.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.NoSelection)
        self.task_listView.setMovement(QtWidgets.QListView.Movement.Free)
        self.task_listView.setObjectName("task_listView")

        self.task_verticalLayout.addWidget(self.task_listView)

        #frame for new tasks
        self.add_task_frame=QtWidgets.QFrame(parent=self.centralWidget)
        self.add_task_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.add_task_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.add_task_frame.setObjectName("add_task_frame")

        self.add_HorizontalLayout=QtWidgets.QHBoxLayout(self.add_task_frame)
        self.add_HorizontalLayout.setContentsMargins(30,0,0,0)
        self.add_HorizontalLayout.setSpacing(0)

        #text gia neo task
        self.newTask=QtWidgets.QLineEdit(parent=self.add_task_frame)
        self.newTask.setObjectName("new_task")

        self.add_HorizontalLayout.addWidget(self.newTask)

        self.add_btn=QtWidgets.QPushButton(parent=self.add_task_frame)
        self.add_btn.setText("Add")
        font=QtGui.QFont()
        font.setBold(True)
        self.add_btn.setFont(font)
        self.add_btn.setIcon(QtGui.QIcon("./static/icons/add_black.svg"))
        self.add_btn.setIconSize(QtCore.QSize(30,30))
        self.add_btn.setObjectName("add_btn")

        self.add_HorizontalLayout.addWidget(self.add_btn)

        #add task frames
        self.main_verticalLayout.addWidget(self.title_frame)
        self.main_verticalLayout.addWidget(self.title_frame)
        self.main_verticalLayout.addWidget(self.title_frame)
        self.main_verticalLayout.addWidget(self.title_frame)