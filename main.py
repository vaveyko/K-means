from PyQt6.QtWidgets import QMainWindow
import KMean as kmn

from UiMainWindow import Ui_MainWindow
from PyQt6 import QtWidgets

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.km = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.button_calculate_first.clicked.connect(self.click_first)

    def click_first(self):
        if self.ui.edit_dot_count.text() != '' and self.ui.edit_class_count.text() != '':
            self.km = kmn.KMean(int(self.ui.edit_dot_count.text()),
                                int(self.ui.edit_class_count.text()),
                                self.ui.CheckBoxNormalGeneration.isChecked(),
                                self.ui.CheckBoxMaxiMin.isChecked())
            self.km.show_plot("Начальное состояние")
            self.km.k_mean()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    main_window = MainWindow()
    main_window.show()

    app.exec()
