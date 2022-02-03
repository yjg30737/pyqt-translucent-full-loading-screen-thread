import time

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QWidget

from pyqt_translucent_full_loading_screen_thread.loadingTranslucentScreen import LoadingTranslucentScreen


class LoadingThread(QThread):
    loadingSignal = pyqtSignal()

    def __init__(self, parent: QWidget, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__parent = parent

        self.__loadingTranslucentScreen = LoadingTranslucentScreen(parent=self.__parent, parent_thread=self,
                                                                   description_text='Waiting...')
        self.started.connect(self.__loadingTranslucentScreen.start)
        self.finished.connect(self.__loadingTranslucentScreen.stop)
        self.started.connect(self.__loadingTranslucentScreen.makeParentDisabledDuringLoading)
        self.finished.connect(self.__loadingTranslucentScreen.makeParentDisabledDuringLoading)

    def run(self):
        time.sleep(5)