from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton, QLabel, QVBoxLayout,QHBoxLayout,QMessageBox,QRadioButton,QButtonGroup
def show_result(correct):
    result_win=QMessageBox()
    if correct:
        result_win.setText('Вірно!\nВи виграли гіроскутер')
    else:
        result_win.setText('Ні, це неправильна відповідь. \nВи виграли фірмовий плакат')
    result_win.exec_()
def check_answer():
    global current_question
    selected_btn=btn_group.checkedButton()
    if selected_btn:
        answer=selected_btn.text()
        correct_answer=questions[current_question] ['correct']
        show_result(answer==correct_answer)
        current_question += 1
    if current_question < len(questions):
        load_question()
    else:
        final_win=QMessageBox()
        final_win.setText('Вікторина завершена!')
        final_win.exec_()
        app.quit()
def load_question():
    question_data=questions [current_question]
    question.setText(question_data['question'])
    btn_answer1.setText(question_data['options'][0])
    btn_answer2.setText(question_data['options'][1]) 
    btn_answer3.setText(question_data['options'][2])
    btn_answer4.setText(question_data['options'][3])
    btn_group.setExclusive (False)
    btn_answer1.setChecked (False)
    btn_answer2.setChecked (False)
    btn_answer3.setChecked (False)
    btn_answer4.setChecked (False)
    btn_group.setExclusive(True)
app = QApplication([])
questions = [
    {
        'question': 'В якому році україна стала незалежною?',
        'options': ['2005', '1991', '2015', '1985'],
        'correct': '1991'
    },
    {
        'question': 'В якому році хрестили русь?',
        'options': ['988', '1001', '956', '983'],
        'correct': '988'
    },
    {
        'question': 'Скільки днів має 1 рік?',
        'options': ['365', '370', '412', '354'],
        'correct': '365'
    }
]
current_question = 0
main_win = QWidget()
main_win.setWindowTitle('Конкурс від Crazy People')
main_win.resize(400, 200)
question = QLabel()
btn_answer1 = QRadioButton()
btn_answer2 = QRadioButton()
btn_answer3 = QRadioButton()
btn_answer4 = QRadioButton()
btn_group = QButtonGroup() 
btn_group.addButton(btn_answer1)
btn_group.addButton(btn_answer2)
btn_group.addButton(btn_answer3)
btn_group.addButton(btn_answer4)
layout_main = QVBoxLayout()
layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()
layoutH1.addWidget (question, alignment=Qt.AlignCenter)
layoutH2.addWidget (btn_answer1, alignment=Qt.AlignCenter)
layoutH2.addWidget (btn_answer2, alignment=Qt.AlignCenter)
layoutH3.addWidget (btn_answer3, alignment=Qt.AlignCenter)
layoutH3.addWidget (btn_answer4, alignment=Qt.AlignCenter)
layout_main.addLayout(layoutH1)
layout_main.addLayout(layoutH2)
layout_main.addLayout(layoutH3)
main_win.setLayout (layout_main)
btn_answer1.clicked.connect(check_answer)
btn_answer2.clicked.connect(check_answer)
btn_answer3.clicked.connect(check_answer)
btn_answer4.clicked.connect(check_answer)
load_question()
main_win.show()
app.exec_()