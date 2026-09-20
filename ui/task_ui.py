import sys
from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_TaskForm(QtWidgets. QWidget):
    #task gia na deixnei pote exei patithei to close button
    closeClicked=QtCore.pyqtSignal(int)

    #CSS style gia checked kai unchecked
    checked_style="text-decoration: line-through"
    unchecked_style="text-decoration: none"

    def __init__(self, text, state, position, *args, **kwargs):
        super().__init__()

        self.position=position

        self.init_ui()
        self.task_check_box.setText(text)
        self.task_check_box.setChecked(state)

        if state:
            self.task_check_box.setStyleSheet(self.checked_style)



        #otan allazei h katastash toy task, ananewse to style toy
        self.task_check_box.stateChanged.connect(self.update_style)

        #otan patietai to remove btn, to task prepei na kleisei
        self.remove_btn.clicked.connect(self.emitCloseSignal)



    def init_ui(self):
        self.setGeometry( 0,0,1000,100)

        #css apo arxeio
        with open("./static/style_task.css", "r") as style_file:
            style_str = style_file.read()
            self.setStyleSheet(style_str)
            
        self.gridLayout=QtWidgets.QGridLayout(self)
        self.gridLayout.setContentsMargins(0,0,0,0)
        self.gridLayout.setSpacing(0)


        #dhmioyrgia main task widget
        self.task_widget=QtWidgets.QWidget(parent=self)
        self.horizontalLayout=QtWidgets.QHBoxLayout(self.task_widget)

        #checkbox gia na chekarontai ta oloklhrwmena task
        self.task_check_box=QtWidgets.QCheckBox(self.task_widget)
        self.horizontalLayout.addWidget(self.task_check_box)

        #koympi gia afairesh toy oloklhrwmenoy task
        self.remove_btn=QtWidgets.QPushButton(self.task_widget)
        self.remove_btn.setIcon(QtGui.QIcon("./static/icons/close.svg"))
        self.remove_btn.setIconSize(QtCore.QSize(20,20))
        self.horizontalLayout.addWidget(self.remove_btn)

        #prosthiki task widget sto grid layout
        self.gridLayout.addWidget(self.task_widget, 0,0,1,1)

#update to visual style analoga me to an einai completed h oxi
    def update_style(self,state):
        self.task_check_box.setStyleSheet(self.checked_style if state else self.unchecked_style)

    def emitCloseSignal(self):
        self.closeClicked.emit(self.position)

    def get_checkbox_state(self):
        return self.task_check_box.isChecked()

    def get_checkbox_text(self):
        return self.task_check_box.text()