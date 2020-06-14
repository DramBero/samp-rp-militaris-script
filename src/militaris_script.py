# -*- coding: utf-8 -*-

'''
@author: Teodoro_Bagwell
'''

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QCoreApplication, QPoint
from py_samp_api import *
import bkg_rc
import re
import sys
import threading
import time


used_indexes = []
yaxis = 0.0
numb = -1
stop = True
sqstop = True
rkstop = True
terminate = False


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(600, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(600, 400))
        Form.setMaximumSize(QtCore.QSize(600, 400))
        Form.setMouseTracking(False)
        Form.setWindowOpacity(0.96)
        self.label = QtWidgets.QLabel(Form)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(0, 0, 600, 400))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(600, 400))
        self.label.setMaximumSize(QtCore.QSize(600, 400))
        self.label.setBaseSize(QtCore.QSize(600, 400))
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setStyleSheet("background-image: url(:/newPrefix/ui-bkg.png);")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(225, 270, 150, 41))
        self.pushButton.setMaximumSize(QtCore.QSize(200, 200))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(100, 199, 93, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(100, 199, 93, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(100, 199, 93, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(100, 199, 93, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(100, 199, 93, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(100, 199, 93, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(100, 199, 93, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(100, 199, 93, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(100, 199, 93, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButton.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("background-color: rgba(100, 199, 93, 200);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(560, 10, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(232, 89, 60);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(520, 10, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(100, 100, 100);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(90, 10, 421, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.label_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 191, 121))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("background-color: rgba(255, 255, 255, 150);\n"
"gridline-color: rgb(0, 0, 0);")
        self.label_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_3.setLineWidth(1)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setIndent(0)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(200, 380, 401, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255, 100);")
        self.label_4.setObjectName("label_4")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(225, 320, 150, 41))
        self.pushButton_4.setMaximumSize(QtCore.QSize(200, 200))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(232, 142, 115, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(232, 142, 115, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(232, 142, 115, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(232, 142, 115, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(232, 142, 115, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(232, 142, 115, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(232, 142, 115, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(232, 142, 115, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(232, 142, 115, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButton_4.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setAutoFillBackground(False)
        self.pushButton_4.setStyleSheet("background-color: rgb(232, 142, 115, 200);")
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ordo Militaris LVA Script"))
        self.pushButton.setText(_translate("Form", "Запустить"))
        self.pushButton_2.setText(_translate("Form", "X"))
        self.pushButton_3.setText(_translate("Form", "_"))
        self.label_2.setText(_translate("Form", "Ordo Militaris LVA Script"))
        self.label_3.setText(_translate("Form", "Текущие функции:\n"
"- Замена сквад списка\n"
"- Ранги над головой\n"))
        self.label_4.setText(_translate("Form", " Автор: Teodoro_Bagwell."))
        self.pushButton_4.setText(_translate("Form", "Остановить"))


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        ui = Ui_Form()
        ui.setupUi(self)
        ui.pushButton_3.clicked.connect(self.minimize)
        ui.pushButton_2.clicked.connect(self.close_win)
        ui.pushButton.clicked.connect(self.sc_launch)
        ui.pushButton_4.clicked.connect(self.sc_stop)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl = QtWidgets.QLabel(self)
        self.lbl.setGeometry(15, 15, 200, 20)
        self.lbl.setStyleSheet("color: rgb(232, 142, 115);")
        self.lbl.setText('Скрипт не активен')
        self.lbl.setFont(font)
        self.sqbox = QtWidgets.QCheckBox(self)
        self.sqbox.setGeometry(180, 76, 15, 15)
        self.sqbox.setText('')
        self.sqbox.setChecked(True)
        self.rkbox = QtWidgets.QCheckBox(self)
        self.rkbox.setGeometry(180, 92, 15, 15)
        self.rkbox.setText('')
        self.rkbox.setChecked(True)
        
    def sc_launch(self, Form):
        global stop
        global sqstop
        global rkstop
        if self.lbl.text() == 'Скрипт не активен':
            print('Started script')
            _translate = QtCore.QCoreApplication.translate
            self.lbl.setStyleSheet("color: rgb(100, 199, 93);")
            self.lbl.setText(_translate('Form', 'Скрипт активен'))
            stop = False
            sqstop = not self.sqbox.isChecked()
            rkstop = not self.rkbox.isChecked()
        
    def sc_stop(self, Form):
        global stop
        if self.lbl.text() == 'Скрипт активен':
            print('Stopped script')
            _translate = QtCore.QCoreApplication.translate
            self.lbl.setStyleSheet("color: rgb(232, 142, 115);")
            self.lbl.setText(_translate('Form', 'Скрипт не активен'))
            stop = True
        
    def minimize(self):
        self.showMinimized()
        
    def close_win(self):
        global terminate
        terminate = True
        self.showMinimized()
        time.sleep(2)
        self.close()
        
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        #print(delta)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()


def squad_script(txwidth = 0.18, maxdraws = 18, move_y = -10):
    textold = ''
    must_create = True
    must_delete = False
    log_text = ''
    colordict = {}
    listo = []
    global numb
    global used_indexes
    global yaxis
    
    def update_color(plid, plcol):
        global used_indexes
        plcolo = plcol
        color = int('0xFF' + plcol, 16)
        used_index = create_text_draw(colordict[plid][3], 5.0,                \
            colordict[plid][1], font = 1, letterWidth = txwidth,              \
            letterHeight = 1, letterColor = color, left = 1, center = 0)
        log_text = 'UPDATING COLOR, CREATING TEXTDRAW:' + colordict[plid][3]  \
                    + str(hex(color))
        print(log_text)
        delete_text_draw(colordict[plid][0])
        log_text = 'UPDATING COLOR, DELETING PREVIOUS TEXTDRAW'
        print(log_text)
        colordict[plid][2] = plcol
        colordict[plid][0] = used_index
        used_indexes.append(used_index)
        return used_index
    
    def delete_txtdraws():
        global used_indexes
        for index in used_indexes:
            delete_text_draw(index)
        used_indexes = []
        colordict = {}
        log_text = 'CLEARED ALL TEXTDRAWS'
        print(log_text)
        return True
    
    def get_text_draw_by_text():
        for i in text_draws:
            if text_draws[i]['Text'].find('SQUAD') != -1:
                return i
        return False
    
    while True:
        if terminate:
            for index in used_indexes:
                delete_txtdraws()
            if numb:
                set_text_draw_pos(numb, 1.0, yaxis)
            return True
        if stop or sqstop:
            textold = ''
            textnew = ''
            listo = []
            for index in used_indexes:
                delete_txtdraws()
            if numb:
                set_text_draw_pos(numb, 1.0, yaxis)
            continue
        if not check_handles():
            must_create = False
            colordict = {}
            used_indexes = []
            textold = ''
            textnew = ''
            text_draws = {}
            if log_text != 'SAMP NOT RUNNING':
                log_text = 'SAMP NOT RUNNING'
                print(log_text)
            continue
        text_draws = update_text_draws()
        numb = get_text_draw_by_text()
        if not numb:
            if used_indexes:
                delete_txtdraws()
            must_create = False
            textold = ''
            textnew = ''
            if log_text != 'TEXTDRAW NOT FOUND':
                log_text = 'TEXTDRAW NOT FOUND'
                print(log_text)
        else:
            textnew = text_draws[numb]['Text']
            if textnew == '':
                must_delete = True
            yaxis = get_text_draw_pos(numb)[1]
        if textnew != textold:
            log_text = 'FOUND TEXTDRAW: ' + textnew
            print(log_text)
            regexp = re.compile("~n~(.*)$")
            try:
                listo = regexp.search(textnew).group(1).split('~n~')
            except:
                continue
            if used_indexes:
                delete_txtdraws()
            must_create = True
        for i in range(len(listo)):
            plid = get_id_by_name(listo[i])
            plcol = get_player_color(plid)
            plcol = plcol[4:6] + plcol[2:4] + plcol[:2]
            if plcol == '000000':
                plcol = 'FFFFFF'
            if plid in colordict:
                if plcol != colordict[plid][2]:
                    update_color(plid, plcol)
        if must_create and not used_indexes:
            set_text_draw_pos(numb, -200.0, get_text_draw_pos(numb)[1])
        if must_create:
            used_index = create_text_draw('SQUAD:', 5.0, yaxis + move_y - 1.0,\
                font = 1, letterWidth = 0.2, letterHeight = 1.1, left = 1,    \
                center = 0, letterColor = 0xFFFFFFFF)
            log_text = 'CREATED TEXT DRAW FOR: SQUAD LINE'
            print(log_text)
            used_indexes.append(used_index)
            yaxisl = yaxis + move_y
            for i in range(len(listo)):
                if i > maxdraws:
                    break
                yaxisl += 9.0
                plid = get_id_by_name(listo[i])
                plcolo = get_player_color(plid)
                plcol = plcolo[4:6] + plcolo[2:4] + plcolo[:2]
                name = '_-_' + listo[i] + '_[' + str(plid) + ']'
                color = int('0xFF' + plcol, 16)
                used_index = create_text_draw(name, 5.0, yaxisl, font = 1,    \
                    letterWidth = txwidth, letterHeight = 1,                  \
                    letterColor = color, left = 1, center = 0)
                colordict.update({plid : [used_index, yaxisl, plcolo, name]})
                used_indexes.append(used_index)
                log_text = 'CREATED TEXT DRAW FOR: ' + str(listo[i])
                print(log_text)
            textold = textnew
            must_create = False
            

def ranks_on_heads(unwork = False):
    lbls = {}
    # {plid : {'lblid' : lblid, 'text' : text}}
    rnks = {}
    # {plid : rank}
    while True:
        if terminate:
            for i in lbls:
                delete_text_label(lbls[i]['lblid'])
            return True
        if stop or rkstop:
            for i in lbls:
                delete_text_label(lbls[i]['lblid'])
            lbls = {}
            rnks = {}
            continue
        if not check_handles():
            lbls = {}
            rnks = {}
            continue
        else:
            if get_dialog_caption() == 'Состав онлайн':
                membtext = get_dialog_text()
                lines = membtext.split('\n')
                for line in lines[1:]:
                    if line == '':
                        continue
                    if line.find('ыходн') != -1:
                        if unwork:
                            continue
                        else:
                            break
                    rankobj = re.search(r'^\[\d+\] \[(\d+)\] \w+_\w+\s+(\D+)\[\d+\].*?', line, re.M|re.I)
                    try:
                        mmbid = int(rankobj.group(1))
                        rnkid = rankobj.group(2)
                    except:
                        continue
                    if not rnkid:
                        rnkid = ''
                    if mmbid not in rnks:
                        print('CREATED IN RANK DICT: ID', mmbid, 'RANK', rnkid)
                        rnks.update({mmbid : rnkid})
                        continue
                    else:
                        if rnks[mmbid] != rnkid:
                            print('UPDATED IN RANK DICT: ID', mmbid, 'RANK', rnkid)
                            rnks[mmbid] = rnkid
        for i in get_stream_ids():
            text = ''
            col = get_player_color(i)
            if col == '' or col == 0 or col == -1:
                col == 'FFFFFF'
            color = color_to_clist(col)
            text += clist_to_means(color)
            rank = ''
            if i in rnks:
                rank = rnks[i]
            else:
                if i in lbls:
                    print('DELETING:', lbls[i])
                    delete_text_label(lbls[i]['lblid'])
                    del lbls[i]
            if text == '' and rank == '':
                if i in lbls:
                    print('DELETING:', lbls[i])
                    delete_text_label(lbls[i]['lblid'])
                    del lbls[i]
                continue
            text = '{BBBB3A}' + rank + '\n{' + col + '}' + text
            if i in lbls:
                if text != lbls[i]['text']:
                    print('UPDATING:', text)
                    update_text_label(lbls[i]['lblid'], text)
                    lbls[i]['text'] = text
            else:
                print('CREATING:', text)
                lblid = create_text_label(text, 0xFFFFFFFF, 0.0, 0.0, 0.5, 12.0, 1, i)
                lbls.update({i : {'lblid' : lblid, 'text' : text}})


def color_to_clist(color):
#    color = color.lower
    if color == '000000':
        return 0
    if color == 'ffffff':
        return 0
    if color == '089401':
        return 1
    if color == '56fb4r':
        return 2
    if color == '49r789':
        return 3
    if color == '2a9170':
        return 4
    if color == '9ed201':
        return 5
    if color == '279b1e':
        return 6
    if color == '59a655':
        return 7
    if color == 'ff0606':
        return 8
    if color == 'ff6600':
        return 9
    if color == 'f45000':
        return 10
    if color == 'be8a01':
        return 11
    if color == 'b30000':
        return 12
    if color == '954f4f':
        return 13
    if color == 'e7961d':
        return 14
    if color == 'e6284e':
        return 15
    if color == 'ff9db6':
        return 16
    if color == '110ce7':
        return 17
    if color == '0cd7e7':
        return 18
    if color == '139bec':
        return 19
    if color == '2c9197':
        return 20
    if color == '114d71':
        return 21
    if color == '8813e7':
        return 22
    if color == 'b313e7':
        return 23
    if color == '758c9d':
        return 24
    if color == 'ffde24':
        return 25
    if color == 'ffee8a':
        return 26
    if color == 'ddb201':
        return 27
    if color == 'dda701':
        return 28
    if color == 'b0b000':
        return 29
    if color == '868484':
        return 30
    if color == 'b8b6b6':
        return 31
    if color == '383838':
        return 32
    if color == 'FAFAFA':
        return 33
    else:
        return 0


def clist_to_means(color):  # Указанные значения клиста и надписей будут   
                            # отображаться под рангами цветом клиста
    '''
    if color == 12:
        return '[Повязка руководства]'
    elif color == 7:
        return '[Военная кепка]'
    elif color == 8:
        return '[Повязка старших офицеров]'
    elif color == 21:
        return '[Повязка ОСН Рысь]'
    elif color == 32:
        return '[Повязка СОБР]'
    else:
        return ''
        '''
    return ''


if __name__ == "__main__":
    sq_thr = threading.Thread(target=squad_script, args=())
    sq_thr.start()
    rk_thr = threading.Thread(target=ranks_on_heads, args=())
    rk_thr.start()
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    w.show()
    sys.exit(app.exec_())

