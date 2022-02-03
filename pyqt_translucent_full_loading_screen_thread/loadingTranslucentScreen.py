import os, inspect, sys

from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QGraphicsOpacityEffect
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QMovie, QPalette, QColor


class LoadingTranslucentScreen(QWidget):
    def __init__(self, parent: QWidget, parent_thread, description_text: str = ''):
        super().__init__(parent)
        self.__parent = parent
        self.__parent.installEventFilter(self)

        self.__thread = parent_thread

        self.__parent.resizeEvent = self.resizeEvent
        self.__initUi(description_text)

    def __initUi(self, description_text):
        self.setAttribute(Qt.WA_TransparentForMouseEvents, True)

        self.__movieLbl = QLabel(self.__parent)

        caller_path = os.path.dirname(inspect.getframeinfo(sys._getframe(1)).filename)
        loading_screen_ico_filename = os.path.join(caller_path, 'ico/Loading.gif')

        self.__loading_mv = QMovie(loading_screen_ico_filename)
        self.__loading_mv.setScaledSize(QSize(45, 45))
        self.__movieLbl.setMovie(self.__loading_mv)
        self.__movieLbl.setStyleSheet('QLabel { background: transparent; }')
        self.__movieLbl.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)

        self.__descriptionLbl = QLabel()
        if description_text.strip() != '':
            self.__descriptionLbl.setText(description_text)
            self.__descriptionLbl.setVisible(False)
            self.__descriptionLbl.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)

        lay = QVBoxLayout()
        lay.addWidget(self.__movieLbl)
        lay.addWidget(self.__descriptionLbl)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)

        self.setLayout(lay)

        self.setMinimumSize(self.__parent.width(), self.__parent.height())

        self.setVisible(False)

    def start(self):
        self.__loading_mv.start()
        self.__descriptionLbl.setVisible(True)
        self.raise_()

        self.setVisible(True)
        opacity_effect = QGraphicsOpacityEffect(opacity=0.75)
        self.setGraphicsEffect(opacity_effect)

    def stop(self):
        self.__loading_mv.stop()
        self.__descriptionLbl.setVisible(False)
        self.lower()

        self.setVisible(False)

    def makeParentDisabledDuringLoading(self):
        if self.__thread.isRunning():
            self.__parent.setEnabled(False)
        else:
            self.__parent.setEnabled(True)

    def paintEvent(self, e):
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(255, 255, 255))
        self.setAutoFillBackground(True)
        self.setPalette(palette)
        return super().paintEvent(e)

    def eventFilter(self, obj, e):
        if isinstance(obj, QWidget):
            if e.type() == 14:
                self.setFixedSize(e.size())
        return super(LoadingTranslucentScreen, self).eventFilter(obj, e)

