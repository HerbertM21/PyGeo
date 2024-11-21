import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt6 import QtCore
from sidebar_ui import Ui_MainWindow
from exams_page import ExamsPage


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Inicializar página de exámenes
        self.exams_page = ExamsPage()
        self.ui.page_3_layout.addWidget(self.exams_page)

        self.ui.icon_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.home_btn_2.setChecked(True)

        # Conectar navegación del sidebar
        self.ui.home_btn_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.dashboard_btn_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.questions_btn_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.chat_btn_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))
        self.ui.credits_btn_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(4))

        # Conectar botones del menú reducido
        self.ui.home_btn_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.dashboard_btn_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.questions_btn_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.chat_btn_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))
        self.ui.credits_btn_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(4))

        # Otras conexiones
        self.ui.search_btn.clicked.connect(self.on_search_btn_clicked)
        self.ui.stackedWidget.currentChanged.connect(self.on_stackWidget_currentChanged)

    def on_search_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(5)
        search_text = self.ui.search_input.text().strip()
        if search_text:
            self.ui.label_9.setText(search_text)

    def on_stackWidget_currentChanged(self, index):
        btn_list = self.ui.icon_only_widget.findChildren(QPushButton) \
                   + self.ui.full_menu_widget.findChildren(QPushButton)
        for btn in btn_list:
            if index in [5, 6]:
                btn.setAutoExclusive(False)
                btn.setCheckable(False)
            else:
                btn.setAutoExclusive(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    with open("style.qss", "r") as style_file:
        style_str = style_file.read()
    app.setStyleSheet(style_str)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())