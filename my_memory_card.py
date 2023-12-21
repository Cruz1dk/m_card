#создай приложение для запоминания информации#запрограммируй сложный тест
#подключение библиотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import  QApplication, QLabel, QWidget, QHBoxLayout, QPushButton, QRadioButton, QVBoxLayout, QMessageBox, QGroupBox, QButtonGroup
from random import shuffle
from random import randint
app = QApplication([])# создание приложения

class Question():
    def __init__(self, vopros, right_answer, wrong1, wrong2, wrong3):
        self.vopros = vopros
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
#создание виджетов главного окна
main_win = QWidget()# создание главного окна
main_win.show()# показать окно
main_win.resize(400,300)# размер окна
main_win.setWindowTitle('Memory Card')# название окна

main_win.score = 0
main_win.total = 0

text = QLabel('Какой национальности не существует?')#  создание надписи

button = QPushButton()# создание кнопки
button.setText('Ответить')# текст кнопки

question_list =[]

r_burron1 = QRadioButton('Энцы')# создание  переключателя
r_burron2 = QRadioButton('Смурфы')# создание  переключателя
r_burron3 = QRadioButton('Чулымцы')# создание  переключателя
r_burron4 = QRadioButton('Алеуты')# создание  переключателя
line_hG = QHBoxLayout()# создание горизонтальной линии для первойгруппы
line_vg1 = QVBoxLayout()# создание 1вертикальной линии для первой группы
line_vg2 = QVBoxLayout()# создание 2вертикальной линии для первой группы
line_V = QVBoxLayout()# создание главной вертикальной линии

line_vg1.addWidget(r_burron1, alignment =  Qt.AlignVCenter)# добавление 1переключателя к 1вертикальной линии 
line_vg1.addWidget(r_burron2, alignment =  Qt.AlignVCenter)# добавление 2переключателя к 1вертикальной линии 
line_vg2.addWidget(r_burron3, alignment =  Qt.AlignVCenter)# добавление 3переключателя к 2вертикальной линии 
line_vg2.addWidget(r_burron4, alignment =  Qt.AlignVCenter)# добавление 4переключателя к 2вертикальной линии 

line_hG.addLayout(line_vg1)# добавление 1вертикальной линии к горизонтальной линии для первой группы
line_hG.addLayout(line_vg2)# добавление 2вертикальной линии к горизонтальной линии для первой группы
line_hG.setSpacing(40)
# группа 1
r_groupBox = QGroupBox('Варианты ответов')# создание группы с надписью
r_groupBox.setLayout(line_hG)# задать групе горизонтальную линию



layout_line1 = QHBoxLayout() # создание гор линиии для вопрос
layout_line2 = QHBoxLayout() # создании гор линии для варианты ответов или результат теста
layout_line3 = QHBoxLayout() # создание гор линии длякнопка "Ответить"

#layout_line1.addStretch(4)
layout_line1.addWidget(text, alignment =  Qt.AlignCenter)# добавление к горизонт линии текст
#layout_line1.addStretch(4)
#layout_line2.addStretch(60)
layout_line2.addWidget(r_groupBox)# добавление к горизонт линии группу
#layout_line2.addStretch(4)
layout_line3.addStretch(4)
layout_line3.addWidget(button,stretch=6)# добавление к линии кнопку
layout_line3.addStretch(4)

button_exit = QPushButton()# создание кнопки выхода
button_exit.setText('Выход')# текст кнопки
layout_line3.addWidget(button_exit, alignment = Qt.AlignRight)# добавление к линии кнопку

#Группа ответов
ot_groupBox = QGroupBox('Результат теста')#Создание группы
text_pr_nepr = QLabel('Правильно или не правильно')#Создание текста
text_pr = QLabel('Правильный ответ')#Создание текста

line_Vgroup= QVBoxLayout()#Создание вертикальной линии для группы ответов
#line_Vgroup.addStretch(40)
line_Vgroup.addWidget(text_pr_nepr)#добавление к линии текст
line_Vgroup.addWidget(text_pr,alignment = Qt.AlignCenter)#добавление к линии текст
line_Vgroup.addStretch(50)
#line_Vgroup.setSpacing(40)
ot_groupBox.setLayout(line_Vgroup)#добавление к группе вертикальную линию

layout_line2.addWidget(ot_groupBox)#добавление к линии2 группу ответов


line_V.addLayout(layout_line1, stretch=3)#добавление к главной вертикальн линии - линию с текстом
line_V.addLayout(layout_line2, stretch=3)#добавление к главной вертикальн линии - линию с группами
#line_V.addStretch(1)
line_V.addLayout(layout_line3)#добавление к главной вертикальн линии - линию с кнопками
line_V.addStretch(1)
#line_V.setSpacing(5)

ot_groupBox.hide()

# объединяем все переключатели в специальную группу
RadioGroup = QButtonGroup() 
RadioGroup.addButton(r_burron1)
RadioGroup.addButton(r_burron2)
RadioGroup.addButton(r_burron3)
RadioGroup.addButton(r_burron4)


def show_question(): # функция отображающая форму вопроса
    ot_groupBox.hide()
    r_groupBox.show()
    button.setText('Ответить')
    RadioGroup.setExclusive(False) # снимаем ограничение для сброса выбора
    r_burron1.setChecked(False)# снимаем выбор всех переключателей
    r_burron2.setChecked(False)
    r_burron3.setChecked(False)
    r_burron4.setChecked(False)
    RadioGroup.setExclusive(True)# возвращаем ограничения


def show_result(res):# функция отображающая форму ответа
    r_groupBox.hide()
    ot_groupBox.show()
    text_pr_nepr.setText(res)
    button.setText('Следующий вопрос')


def start_test():
    if 'Ответить' == button.text():
        show_result()
    else:
        show_question()

answers = [r_burron1, r_burron2, r_burron3, r_burron4]# создаём список переключателей



def ask(q: Question):# функция записывает значения вопроса и ответов в соответствующие виджеты, 
    #при этом варианты ответов распределяются случайным образом
    shuffle(answers) # перемешиваем элементы списка перключателей
    answers[0].setText(q.right_answer)# задаём случайной кнопке правильный ответ
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    text.setText(q.vopros)
    text_pr.setText(q.right_answer)
    show_question()
q = Question('Государственный язык Бразилии?','Португальский','Испанский', 'Бразильский', 'Итальянский')    
#ask(q)

question_list.append(q)
question_list.append(Question('Какого цвета нет на флаге?','Зелёного', 'Красного', 'Синоего', 'Белого'))
question_list.append(Question('Скоклько будет 5х5?','25.', '100.', '5.', '50.'))

main_win.cur = 0 # по-хорошему такие переменные должны быть свойствами, 
                 # только надо писать класс, экземпляры которого получат такие свойства, 
                 # но python позволяет создать свойство у отдельно взятого экземпляра
'''def next_question():
    # задает следующий вопрос из списка
    # этой функции нужна переменная, в которой будет указываться номер текущего вопроса
    # эту переменную можно сделать глобальной, либо же сделать свойством "глобального объекта" (app или window)
    main_win.cur +=1
    if main_win.cur == len(question_list):
        main_win.cur = 0
    ask(question_list[main_win.cur])'''
    
def next_question():
    main_win.total += 1
    cur = randint(0, len(question_list)-1)
    ask(question_list[cur])

    

next_question()

def click_ok(): #определяет, надо ли показывать другой вопрос либо проверить ответ на этот
    if 'Следующий вопрос' == button.text():
        next_question()
    if 'Ответить' == button.text():
        check_answer()

'''def ask(vopros, right_answer, wrong1, wrong2, wrong3):#функция, задающая (отображающая) указанный вопрос.
    shuffle(answers) # перемешиваем элементы списка перключателей
    answers[0].setText(right_answer)# задаём случайной кнопке правильный ответ
    answers[1].setText(wrong1)
    answers[2].setText(wrong2)
    answers[3].setText(wrong3)
    text.setText(vopros)
    text_pr.setText(right_answer)
    show_question()    
ask('Государственный язык Бразилии?','Португальский','Испанский', 'Бразильский', 'Итальянский')'''

def check_answer(): # функция проверяющая ответы
    #if 'Следующий вопрос' == button.text():
        #show_question()
    if answers[0].isChecked():
        show_result('Правильно!')
        main_win.score += 1
        print('Статистика')
        print('-Всего вопросов:', main_win.total)
        print('-Правильных ответов:', main_win.score)
        print('Рейтинг:', (main_win.score/main_win.total)*100, '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
                show_result('Неверно!')
                print('Статистика')
                print('-Всего вопросов:', main_win.total)
                print('-Правильных ответов:', main_win.score)
                print('Рейтинг:', (main_win.score/main_win.total)*100, '%')

#
def show_correct(res):
    text_pr_nepr.setText(res)
    show_result()



button.clicked.connect(click_ok)
#button_exit.clicked.connect(exit)

main_win.setLayout(line_V)
app.exec_()
