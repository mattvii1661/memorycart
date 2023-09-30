from PyQt5.QtCore import Qt 
from PyQt5.OtWidget import(
    QApplication, QWidget, QTableWidget, QListWidget, 
    QLineEdit, QFormLoyout, QHBoxLayout, 
    QVBoxLayout, QGroupBox, QButtonGroup, 
    QPushButton, QLabel, QRadioButton, QSpinBox)
from memo_card import*

list_question= QListView()
widget_ans= QWidget()
widget.ansLayout(layout_form)
btn_add= QPushButton('new question')
btn_del= QPushButton('del question')
btn_start=QPushButton('Початок тесту')

qst_col= QVBoxLayout()#Qst collume(стовпчик з пиитаннями)
qst_col.addWidget(list_question)
qst_col.addWidget(btn_add)

ans_col = QVBoxLayout()
ans_col.addWidget(widget_ans)
ans_col.addWidget(btn_del)

btn_line= QHBoxLayout()
btn_line.addLayout(qst_col)
btn_line.addLayout(ans_col)

test_line= QHBoxLayout
test_line.addStretch(1)
test_line.addWidget(btn_start, stretch= 2)
test_line.addWidget(1)

layout_screen= QVBoxLayout()
layout_screen.addLayout(btn_line)
layout_screen.addLayout(test_line)