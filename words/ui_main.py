from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QSlider
from PyQt5.QtCore import Qt


class Ui_MainWindow(object):
    window_height = 720
    window_width = 450

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Words")

        MainWindow.resize(self.window_width, self.window_height)

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(204, 204, 204))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)

        self.vvod = QtWidgets.QLabel(MainWindow)
        self.vvod.setGeometry(QtCore.QRect(40, 80, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.vvod.setFont(font)
        self.vvod.setObjectName("vvod")

        self.your_word = QtWidgets.QLineEdit(MainWindow)
        self.your_word.setGeometry(QtCore.QRect(50, 140, 113, 20))
        self.your_word.setObjectName("your_word")

        self.down = QtWidgets.QPushButton(MainWindow)
        self.down.setGeometry(QtCore.QRect(170, 140, 30, 30))
        self.down.setStyleSheet("QPushButton {background-color: #F08080}")
        font = QtGui.QFont()
        font.setPointSize(15)
        self.down.setFont(font)
        self.down.setObjectName("down")

        self.story = QtWidgets.QListWidget(MainWindow)
        self.story.setGeometry(QtCore.QRect(30, 210, 220, 270))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.story.setFont(font)
        self.story.setObjectName("story")

        self.verticalLayoutWidget = QtWidgets.QWidget(MainWindow)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(280, 90, 150, 100))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.help = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.help.setFont(font)
        self.help.setObjectName("help")
        self.help.setStyleSheet("QPushButton {background-color: #00FA9A}")
        self.verticalLayout.addWidget(self.help)
        self.help_word = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.help_word.setFont(font)
        self.help_word.setObjectName("help_word")
        self.help_word.setStyleSheet("QLabel {background-color: #00FA9A}")
        self.verticalLayout.addWidget(self.help_word)

        self.start_over = QtWidgets.QPushButton(MainWindow)
        self.start_over.setGeometry(QtCore.QRect(120, 10, 100, 40))
        self.start_over.setStyleSheet("QPushButton {background-color: #FF7F50}")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.start_over.setFont(font)
        self.start_over.setObjectName("start_over")

        self.open_game = QtWidgets.QPushButton(MainWindow)
        self.open_game.setGeometry(QtCore.QRect(10, 10, 100, 40))
        self.open_game.setStyleSheet("QPushButton {background-color: #FF7F50}")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.open_game.setFont(font)
        self.open_game.setObjectName("open_game")

        self.save_game = QtWidgets.QPushButton(MainWindow)
        self.save_game.setGeometry(QtCore.QRect(230, 10, 100, 40))
        self.save_game.setStyleSheet("QPushButton {background-color: #FF7F50}")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.save_game.setFont(font)
        self.save_game.setObjectName("save_game")

        self.close_game = QtWidgets.QPushButton(MainWindow)
        self.close_game.setGeometry(QtCore.QRect(340, 10, 100, 40))
        self.close_game.setStyleSheet("QPushButton {background-color: #FF7F50}")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.close_game.setFont(font)
        self.close_game.setObjectName("close_game")

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(MainWindow)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(300, 220, 130, 260))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.show_stat = QtWidgets.QPushButton(MainWindow)
        self.show_stat.setGeometry(QtCore.QRect(30, 500, 220, 40))
        self.show_stat.setStyleSheet("QPushButton {background-color: #6A5ACD}")
        font = QtGui.QFont()
        font.setPointSize(15)
        self.show_stat.setFont(font)
        self.show_stat.setObjectName("show_stat")

        self.help_doc = QtWidgets.QPushButton(MainWindow)
        self.help_doc.setGeometry(QtCore.QRect(300, 500, 130, 40))
        self.help_doc.setStyleSheet("QPushButton {background-color: #7FFFD4}")
        font = QtGui.QFont()
        font.setPointSize(15)
        self.help_doc.setFont(font)
        self.help_doc.setObjectName("help_doc")

        self.count = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.count.setStyleSheet("QLabel {background-color: #1E90FF}")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.count.setFont(font)
        self.count.setObjectName("count")
        self.verticalLayout_2.addWidget(self.count)

        self.number_count = QtWidgets.QLCDNumber(self.verticalLayoutWidget_2)
        self.number_count.setObjectName("number_count")
        self.number_count.setStyleSheet("QLCDNumber {background-color: #1E90FF}")
        self.verticalLayout_2.addWidget(self.number_count)

        self.record = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.record.setFont(font)
        self.record.setObjectName("record")
        self.record.setStyleSheet("QLabel {background-color: #EE82EE}")
        self.verticalLayout_2.addWidget(self.record)

        self.number_record = QtWidgets.QLCDNumber(self.verticalLayoutWidget_2)
        self.number_record.setObjectName("number_record")
        self.number_record.setStyleSheet("QLCDNumber {background-color: #EE82EE}")
        self.verticalLayout_2.addWidget(self.number_record)

        self.mistake = QtWidgets.QLabel(MainWindow)
        self.mistake.setGeometry(QtCore.QRect(30, 170, 250, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.mistake.setFont(font)
        self.mistake.setObjectName("mistake")

        self.tableWidget = QtWidgets.QTableWidget(MainWindow)
        self.tableWidget.setGeometry(QtCore.QRect(30, 570, 400, 100))
        self.tableWidget.setAutoFillBackground(True)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.slider = QSlider(MainWindow)
        self.slider.setGeometry(QtCore.QRect(30, 680, 400, 30))
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setFocusPolicy(Qt.NoFocus)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, Words):
        _translate = QtCore.QCoreApplication.translate
        Words.setWindowTitle(_translate("Words", "Слова"))
        self.vvod.setText(_translate("Words", "Введите слово"))
        self.down.setText(_translate("Words", "↓"))
        self.help.setText(_translate("Words", "3 подсказки"))
        self.help_word.setText(_translate("Words", ""))
        self.start_over.setText(_translate("Words", "Новая игра"))
        self.save_game.setText(_translate("Words", "Сохранить игру"))
        self.close_game.setText(_translate("Words", "Завершить игру"))
        self.open_game.setText(_translate("Words", "Открыть игру"))
        self.show_stat.setText(_translate("Words", "Показать статистику"))
        self.help_doc.setText(_translate("Words", "Помощь"))
        self.count.setText(_translate("Words", "Кол-во слов:"))
        self.record.setText(_translate("Words", "Рекорд:"))
        self.mistake.setText(_translate("Words", ""))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
