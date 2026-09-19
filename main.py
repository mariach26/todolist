import json
import os
import sys

from PyQt6.QtCore import QSize, pyqtSignal, Qt
from PyQt6.QtGui import QStandardItemModel, QStandardItem, QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget

from ui.task_ui import Ui_TaskForm
from ui.main_ui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.list_view=self.ui.task_listView
        self.add_btn=self.ui.add_btn
        self.task_input=self.ui.new_task

        self.list_model=QStandardItemModel
        self.init_ui()



        self.task_file_path=os.path.join(os.getcwd(), "static/tasks.json")
        self.task_list=self.get_tasks() #retrieve tasks
        self.show_tasks(self.task_list)


    def init_ui(self):
        self.list_view.setModel(self.list_model)
        self.list_view.setSpacing(5)
        self.list_view.setFocusPolicy(Qt.Policy.NoFocus)

        #icon gia add button
        self.add_btn.setIcon(QIcon("./static/icons/add_min.svg"))
        self.add_btn.clicked.connect(self.add_new_task)

    def add_new_task(self):
        #neo task apo xrhsth
        new_task=self.task_input.text().strip()
        if new_task:
            self.task_list.append([new_task,False])
            self.show_tasks(self.task_list)
            self.task_input.clear()

    def remove_item(self,position):
        #afairesh 
        self.list_model.removeRow(position)
        self.task_list.pop(position)
        self.get_all_tasks()
        self.show_tasks(self.task_list)


    def get_tasks(self):
        #fortwsh tasks apo json
        with open(self.task_file_path,"r") as f:
            tasks_data_str= f.read()
            if tasks_data_str:
                tasks=json.loads(tasks_data_str)
                return tasks["tasks"]
            else:
                return list()
            
    def show_tasks(self):
        #custon widgets gia kathe task
        self.list_model.clear()
        if self.task_list:
            for i, task in enumerate(self.task_list):
                item=QStandardItem()
                self.list_model.appendRow(item)
                widget=Ui_TaskForm(task[0], task[1], i)
                widget.closeClicked.connect(self.remove_item)
                item.setSizeHint(widget.sizeHint())
                self.list_view.setIndexWidget(self.list_model.indexFromItem(item), widget)

    def get_all_tasks(self):
        self.task_list=[]

        for row in range(self.list_model.rowCount()):
            item=self.list_model.item(row,0)
            widget=self.list_view.indexWidget(item.index())
            if isinstance(widget,Ui_TaskForm):
                self.task_list.append([widget.get_checkbox_text(), widget.get_checkbox_state()])

    def closeEvent(self,event):
        self.get_all_tasks()
        with open(self.task_file_path, "w") as f:
            pass


if  __name__=="__main__":
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec())

