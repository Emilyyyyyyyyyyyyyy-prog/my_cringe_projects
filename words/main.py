from ui_main import Ui_MainWindow
import sqlite3
import sys
import random
import pymorphy2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QDialog, QFileDialog, QWidget, qApp


class Help_window(QDialog):  # класс, открывающий документацию к игре
    def __init__(self, parent=None):
        super(Help_window, self).__init__()
        self.resize(600, 500)
        self.setWindowTitle("О программе")
        self.textBrowser = QtWidgets.QTextBrowser(self)  # textBrowser - неизменяемый текст
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 600, 500))
        self.textBrowser.setObjectName("textBrowser")

        with open("help_doc.txt") as file_text:  # открытие файла, в котором написана документация
            text_data = file_text.read()
            self.textBrowser.setText(text_data)


class MyMainWindow(QWidget, Ui_MainWindow):
    morph = pymorphy2.MorphAnalyzer()
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя'  # русский алфавит
    words = []  # список существительных русского языка
    with open('word_rus.txt', encoding="windows-1251") as file:
        list_of_words = file.readlines()
        list_of_words = [i.strip() for i in list_of_words]
        for i in alphabet:
            words_letter = []
            for j in list_of_words:
                if j[0] == i:
                    words_letter.append(j)
            words.append(words_letter)

    first_step = True
    last_letter = ''
    amount = 0
    fix_record = 0
    fix_word = ''
    fix_count = 0
    chosen_words = []
    five = []
    table_flag = False
    hint_count = 3

    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        qApp.installEventFilter(self)
        self.setupUi(self)
        self.show()
        self.open_record()  # загрузка последнего рекорда

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 228, 225))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        self.setPalette(palette)

        # нажатие кнопок:
        self.down.clicked.connect(self.enter_word)
        self.help.clicked.connect(self.give_help)
        self.start_over.clicked.connect(self.again)
        self.save_game.clicked.connect(self.save)
        self.close_game.clicked.connect(self.close)
        self.help_doc.clicked.connect(self.give_doc)
        self.open_game.clicked.connect(self.open)
        self.show_stat.clicked.connect(self.give_stat)
        self.slider.valueChanged[int].connect(self.changeValue)

    def enter_word(self):  # функция, которая вводит слово пользователя
        if self.your_word.text():  # проверяет наличие слова
            input_word = self.your_word.text().lower()  # перевод в нижний регистр
            if input_word[0] != self.last_letter and not self.first_step:  # проверка на первую букву
                self.mistake.setText('Первая буква: ' + self.last_letter)
            elif input_word in self.chosen_words:  # проверка на повтор
                self.mistake.setText('Такое слово уже было!')
            elif input_word in self.list_of_words:  # проверка наличия в словаре
                self.story.insertItem(0, input_word)
                self.chosen_words.append(input_word)
                self.first_step = False
                self.last_letter = input_word[-1]
                # проверка есть ли слова на данную букву
                if len(self.words[self.alphabet.index(self.last_letter)]) == 0:
                    self.last_letter = input_word[-2]
                self.mistake.clear()
                self.help_word.clear()
                self.fix_count = 0
                self.fix_word = ''
                self.amount += 1
                self.number_count.display(self.amount)
            elif self.morph.parse(input_word)[0].tag.POS != 'NOUN':  # проверка на существительное
                self.mistake.setText('Не существительное!')
            # проверка на именительный падеж
            elif self.morph.parse(input_word)[0].tag.case != 'nomn':
                self.mistake.setText('Не именительный падеж!')
            else:
                self.mistake.setText('Нет такого слова!')
            self.your_word.clear()  # очистка поля для ввода

    def give_help(self):  # функция, выдающая подсказку
        if self.hint_count > 0 or self.help_word.text() != '':
            hint = random.choice(self.words[self.alphabet.index(self.last_letter)])
            # случайный выбор слова на нужную букву, которого еще не было
            while hint in self.chosen_words:
                hint = random.choice(self.words[self.alphabet.index(self.last_letter)])
            if self.help_word.text() == '':
                self.hint_count -= 1
                hint_word = ['нет подсказок', '1 подсказка', '2 подсказки', '3 подсказки']
                self.help.setText(hint_word[self.hint_count])
            # проверка полностью выданного слова
            if not self.fix_word:
                self.fix_word = hint
                # если слова вообще нет, выводим первую букву
                self.help_word.setText(self.fix_word[0])
            elif self.fix_count + 1 == len(self.fix_word):
                self.mistake.setText('Слово открыто, тупич!')
            else:
                self.fix_count += 1
                self.help_word.setText(self.fix_word[:self.fix_count + 1])

    def again(self):  # функция для кнопки "начать заново"
        # очистка всего
        self.mistake.clear()
        self.story.clear()
        self.your_word.clear()
        self.help_word.clear()
        # проверка на рекорд
        if self.amount > self.fix_record:
            self.fix_record = self.amount
            self.save_record()
        self.amount = 0
        self.number_count.display(self.amount)
        self.number_record.display(self.fix_record)
        self.fix_count = 0
        self.fix_word = ''
        self.chosen_words = []
        self.last_letter = ''
        self.first_step = True
        self.hint_count = 3
        self.help.setText('3 подсказки')

    def average_letters(self):  # подсчет среднего количества букв в слове
        sum_letters = sum([len(i) for i in self.chosen_words])
        return sum_letters / len(self.chosen_words)

    def five_letters(self):  # функция находит 5 самых частых букв
        letters = {}
        for i in self.chosen_words:
            for j in i:
                if j in letters.keys():
                    letters[j] += 1
                else:
                    letters[j] = 1
        # сортировка словаря по самым частым появлениям букв
        letters = sorted(letters.items(), reverse=True, key=lambda x: x[1])
        counter = 0
        for i in letters:
            if counter == 5:
                break
            self.five.append(i[0])
            counter += 1
        while len(self.five) < 5:
            self.five.append('')
        return self.five

    def save_statistics(self):  # сохранение статистики в sqlite3
        self.five_letters()
        number_used_words = len(self.chosen_words)
        number_help = 3 - self.hint_count
        average = round(self.average_letters(), 1)  # округление до 1 знака после запятой
        five1, five2, five3, five4, five5 = [i for i in self.five]
        entities = [number_used_words, number_help, average,
                    five1, five2, five3, five4, five5]
        con = sqlite3.connect('stat.db')  # подключение базы данных
        cur = con.cursor()
        # добавление в таблицу значений
        cur.execute("""
            INSERT INTO statistics 
            values(?, ?, ?, ?, ?, ?, ?, ?)
                    """, entities)
        con.commit()
        con.close()

    def keyPressEvent(self, event):  # горячие клавиши

        if int(event.modifiers()) == Qt.CTRL:
            if event.key() == Qt.Key_S:
                self.save()

        if event.key() == Qt.Key_Enter:
            self.enter_word()

        if int(event.modifiers()) == Qt.CTRL:
            if event.key() == Qt.Key_H:
                self.give_help()

        if int(event.modifiers()) == Qt.CTRL:
            if event.key() == Qt.Key_N:
                self.close()
                self.again()

        if int(event.modifiers()) == Qt.CTRL:
            if event.key() == Qt.Key_O:
                self.close()
                self.open()

        if int(event.modifiers()) == Qt.CTRL:
            if event.key() == Qt.Key_T:
                self.give_stat()

        if event.key() == Qt.Key_F1:
            self.give_doc()

        if event.key() == Qt.Key_Return:
            self.enter_word()

    def save(self):  # сохрание игры
        if self.chosen_words:
            file_name = QFileDialog.getSaveFileName(self, 'Сохранить игру',
                                                    'game.words', 'Игра (*.words)')[0]
            if file_name != '' and len(file_name[0]) > 0:
                sf = file_name.split('.')
                if sf[1] != "words":
                    file_name = sf[0] + ".words"
                file = open(file_name, 'w', encoding='utf8')
                text = '\n'.join(i for i in self.chosen_words)
                file.write(text)
                file.close()

    def close(self):  # закрытие игры
        if self.story.count():
            self.save_statistics()  # сохранение статистики
            self.again()  # начало новой игры

    def open(self):  # открытие ранее сохраненной игры
        file_name = QFileDialog.getOpenFileName(self, 'Выбрать сохранённую игру',
                                                '', "Игра(*.words)")[0]
        if file_name != '' and len(file_name[0]) > 0:
            self.again()
            file = open(file_name, 'r', encoding='utf8')
            data = list(file.read().split('\n'))
            self.chosen_words = data
            for i in self.chosen_words:
                self.story.insertItem(0, i)
            last_word = self.chosen_words[-1]
            self.last_letter = last_word[-1]
            if len(self.words[self.alphabet.index(self.last_letter)]) == 0:
                self.last_letter = last_word[-2]
            self.first_step = False

    def give_doc(self):  # функция, выдающая документацию
        help_text = Help_window(self)
        help_text.exec_()

    def give_stat(self):  # функция, выдающая статистику
        if self.table_flag:  # если уже была статистика
            self.tableWidget.setColumnCount(0)
            self.tableWidget.setRowCount(0)
            self.table_flag = False
            self.show_stat.setText('Показать статистику')
        else:  # если не было статистики
            con = sqlite3.connect('stat.db')
            cur = con.cursor()
            cur.execute("select * from statistics")
            rows = cur.fetchall()  # выгрузка данных в норм список
            # заголовки столбцов таблицы
            header = ['кол-во слов', 'кол. подсказок', 'ср. длина слов',
                      'буква 1', 'буква 2', 'буква 3', 'буква 4', 'буква 5']
            self.tableWidget.setColumnCount(8)
            self.tableWidget.setHorizontalHeaderLabels(header)
            for k in range(8):  # крутимся по столбцам
                self.tableWidget.horizontalHeaderItem(k).setTextAlignment(Qt.AlignHCenter)
            self.tableWidget.setRowCount(0)
            # загрузка данных в табличный виджет
            for i, row in enumerate(rows):
                self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
                for j, elem in enumerate(row):
                    item = QTableWidgetItem(str(elem))
                    self.tableWidget.setItem(i, j, item)
                    item.setTextAlignment(Qt.AlignHCenter)
            con.close()
            self.table_flag = True
            self.show_stat.setText('Убрать статистику')

    def changeValue(self, value):  # функция, меняющая фон экрана от слайдера
        colors = [(255, 228, 225),
                  (255, 255, 224),
                  (216, 191, 216),
                  (152, 251, 152),
                  (173, 216, 230),
                  (127, 255, 212),
                  (189, 183, 107),
                  (176, 196, 222),
                  (135, 206, 235),
                  (245, 245, 220),
                  (255, 240, 245),
                  (211, 211, 211)]
        num_color = round(value / 10)
        palette = QtGui.QPalette()
        color_1, color_2, color_3 = colors[num_color]
        brush = QtGui.QBrush(QtGui.QColor(color_1, color_2, color_3))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        self.setPalette(palette)

    def save_record(self):  # сохранение рекорда
        file_record = open('record.f', 'w', encoding='utf8')
        text = str(self.fix_record)
        file_record.write(text)
        file_record.close()

    def open_record(self):  # загрузка рекорда при запуске программы
        file_record = open('record.f', 'r', encoding='utf8')
        text = file_record.read().strip()
        if text == '':
            text = '0'
        file_record.close()
        self.fix_record = int(text)
        self.number_record.display(self.fix_record)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyMainWindow()
    sys.exit(app.exec_())
