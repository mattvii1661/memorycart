from PyQt5.QtCore import Qt 
from PyQt5.OtWidget import(
    QApplication, QWidget, QTableWidget, QListWidget, 
    QLineEdit, QFormLoyout, QHBoxLayout, 
    QVBoxLayout, QGroupBox, QButtonGroup, 
    QPushButton, QLabel, QRadioButton, QSpinBox) 
app= QApplication([]) 
btn_Menu= QPushButton('Меню') 
btn_Relax= QPushButton('Відпочити') 
btn_Answer= QPushButton('Відповісти') 
box_Minutes= QSpinBox() 
box_Minutes.setValue(30) 
lb_Question= QLabel('') 
 
radio_Group = QGroupBox('Варіанти відповідей') 
radio_Answer = QButtonGroup() 
 
rbtn_1= QRadioButton('') 
rbtn_2= QRadioButton('') 
rbtn_3= QRadioButton('') 
rbtn_4= QRadioButton('') 
 
RadioGroup.addButton(rbtn_1) 
RadioGroup.addButton(rbtn_2) 
RadioGroup.addButton(rbtn_3) 
RadioGroup.addButton(rbtn_4) 
 
ans_Group_Box =QGroupBox('Результат тесту') 
lb_Result = QLabel('')#ця части коду віддповідає за відповідь вірно або ні 
lb_Corect = QLabel('')#ця частина показує лише правильну відповідь 
 
layout_ans1= QHBoxLayout() 
layout_ans2= QVBoxLayout()
layout_ans3= QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout()

layout_line1= QHBoxLayout() 
layout_line2= QHBoxLayout()
layout_line3= QHBoxLayout()
layout_line3= QHBoxLayout()

layout_line1.addWidget(btn_Menu)
layout_line1.addStretch(1)
layout_line1.addWidget(btn_Relax)
layout_line1.addWidget(box_Minutes)
layout_line1.addWidget(QLabel("minutes"))

layout_line2.addwidget(lb_Question, alignment= (Qt.AlignHCenter | Qt.AlignVCenter))
layout_line3.addWidget(radio_Group)
layout_line3.addWidget(ans_Group_Box)
layout_line4.addwidget(btn_Answer, alignment= (Qt.AlignHCenter | Qt.AlignVCenter))

def show_result():
    radio_Group.hide()
    ans_Group_Box.show()
    btn_Answer.setText("Next")
def show_question():
    radio_Group.show()
    ans_Group_Box.hide()
    btn_Answer.setText("Answer")