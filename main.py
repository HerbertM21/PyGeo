import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton
from sidebar_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.icon_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.home_btn_2.setChecked(True)

        # Conectar otras funcionalidades
        self.ui.search_btn.clicked.connect(self.on_search_btn_clicked)
        self.ui.user_btn.clicked.connect(self.on_user_btn_clicked)
        self.ui.stackedWidget.currentChanged.connect(self.on_stackWidget_currentChanged)

    # Función para el botón de búsqueda
    def on_search_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(5)
        search_text = self.ui.search_input.text().strip()
        if search_text:
            self.ui.label_9.setText(search_text)

    # Función para cambiar a la página de usuario
    def on_user_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(6)

    # Cambiar estado de los botones Checkable según la página actual
    def on_stackWidget_currentChanged(self, index):
        btn_list = self.ui.icon_only_widget.findChildren(QPushButton) + self.ui.full_menu_widget.findChildren(QPushButton)
        for btn in btn_list:
            if index in [5, 6]:  # Páginas específicas donde no debe ser exclusivo
                btn.setAutoExclusive(False)
                btn.setCheckable(False)
            else:
                btn.setAutoExclusive(True)

    # Funciones para cambiar páginas desde botones del menú
    def on_home_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_home_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_dashboard_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_dashboard_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_question_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_questions_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_chat_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_chat_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_credits_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def on_credits_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Cargar archivo de estilos
    with open("style.qss", "r") as style_file:
        style_str = style_file.read()
    app.setStyleSheet(style_str)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
