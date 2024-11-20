from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWebEngineWidgets import QWebEngineView

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("PyPlanets")
        MainWindow.resize(1500, 900)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_3 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.header_widget = QtWidgets.QWidget(parent=self.widget_3)
        self.header_widget.setEnabled(True)
        self.header_widget.setMinimumSize(QtCore.QSize(0, 45))
        self.header_widget.setObjectName("header_widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.header_widget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.change_btn = QtWidgets.QPushButton(parent=self.header_widget)
        self.change_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/icon/menu-4-32.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.change_btn.setIcon(icon)
        self.change_btn.setIconSize(QtCore.QSize(14, 14))
        self.change_btn.setCheckable(True)
        self.change_btn.setObjectName("change_btn")
        self.horizontalLayout_4.addWidget(self.change_btn)
        spacerItem = QtWidgets.QSpacerItem(202, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.search_input = QtWidgets.QLineEdit(parent=self.header_widget)
        self.search_input.setMinimumSize(QtCore.QSize(0, 0))
        self.search_input.setFrame(True)
        self.search_input.setObjectName("search_input")
        self.horizontalLayout.addWidget(self.search_input)
        self.search_btn = QtWidgets.QPushButton(parent=self.header_widget)
        self.search_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resources/icon/search-13-48.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.search_btn.setIcon(icon1)
        self.search_btn.setObjectName("search_btn")
        self.horizontalLayout.addWidget(self.search_btn)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(400, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.user_btn = QtWidgets.QPushButton(parent=self.header_widget)
        self.user_btn.setText("")
        icon2 = QtGui.QIcon()
        #icon2.addPixmap(QtGui.QPixmap("resources/icon/logo2.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.user_btn.setIcon(icon2)
        self.user_btn.setCheckable(False)
        self.user_btn.setObjectName("user_btn")
        self.horizontalLayout_4.addWidget(self.user_btn)
        self.verticalLayout_5.addWidget(self.header_widget)
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.widget_3)
        self.stackedWidget.setObjectName("stackedWidget")


        # Configurar la página con QWebEngineView
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.page_layout = QtWidgets.QVBoxLayout(self.page)  # Layout para la página
        self.page_layout.setContentsMargins(0, 0, 0, 0)
        self.page_layout.setSpacing(0)

        # Crear el widget QWebEngineView y cargar el HTML
        self.web_view = QWebEngineView()
        self.web_view.setHtml(self.get_galaxy_html())  # Cargar el HTML de la galaxia
        self.page_layout.addWidget(self.web_view)

        # Añadir la página al stackedWidget
        self.stackedWidget.addWidget(self.page)

        self.gridLayout_3 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_4 = QtWidgets.QLabel(parent=self.page)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_5 = QtWidgets.QLabel(parent=self.page_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_6 = QtWidgets.QLabel(parent=self.page_3)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_7 = QtWidgets.QLabel(parent=self.page_4)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.page_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_8 = QtWidgets.QLabel(parent=self.page_5)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_6.addWidget(self.label_8, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.page_6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_9 = QtWidgets.QLabel(parent=self.page_6)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_7.addWidget(self.label_9, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.page_7)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_10 = QtWidgets.QLabel(parent=self.page_7)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_8.addWidget(self.label_10, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_7)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.gridLayout.addWidget(self.widget_3, 0, 2, 1, 1)
        self.full_menu_widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.full_menu_widget.setObjectName("full_menu_widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.full_menu_widget)
        self.verticalLayout_4.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.logo_label_2 = QtWidgets.QLabel(parent=self.full_menu_widget)
        self.logo_label_2.setMinimumSize(QtCore.QSize(50, 50))
        self.logo_label_2.setMaximumSize(QtCore.QSize(50, 50))
        self.logo_label_2.setText("")
        self.logo_label_2.setPixmap(QtGui.QPixmap("resources/icon/logo2_preview.png"))
        self.logo_label_2.setScaledContents(True)
        self.logo_label_2.setObjectName("logo_label_2")
        self.horizontalLayout_2.addWidget(self.logo_label_2)
        self.logo_label_3 = QtWidgets.QLabel(parent=self.full_menu_widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.logo_label_3.setFont(font)
        self.logo_label_3.setObjectName("logo_label_3")
        self.horizontalLayout_2.addWidget(self.logo_label_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.home_btn_2 = QtWidgets.QPushButton(parent=self.full_menu_widget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("resources/icon/home-4-32.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon3.addPixmap(QtGui.QPixmap("resources/icon/home-4-48.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.home_btn_2.setIcon(icon3)
        self.home_btn_2.setIconSize(QtCore.QSize(20, 20))
        self.home_btn_2.setCheckable(True)
        self.home_btn_2.setAutoExclusive(True)
        self.home_btn_2.setObjectName("home_btn_2")
        self.verticalLayout_2.addWidget(self.home_btn_2)
        self.dashboard_btn_2 = QtWidgets.QPushButton(parent=self.full_menu_widget)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("resources/icon/dashboard-5-32.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon4.addPixmap(QtGui.QPixmap("resources/icon/dashboard-5-48.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.dashboard_btn_2.setIcon(icon4)
        self.dashboard_btn_2.setIconSize(QtCore.QSize(20, 20))
        self.dashboard_btn_2.setCheckable(True)
        self.dashboard_btn_2.setAutoExclusive(True)
        self.dashboard_btn_2.setObjectName("dashboard_btn_2")
        self.verticalLayout_2.addWidget(self.dashboard_btn_2)
        self.questions_btn_2 = QtWidgets.QPushButton(parent=self.full_menu_widget)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("resources/icon/activity-feed-32.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon5.addPixmap(QtGui.QPixmap("resources/icon/activity-feed-48.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.questions_btn_2.setIcon(icon5)
        self.questions_btn_2.setIconSize(QtCore.QSize(20, 20))
        self.questions_btn_2.setCheckable(True)
        self.questions_btn_2.setAutoExclusive(True)
        self.questions_btn_2.setObjectName("questions_btn_2")
        self.verticalLayout_2.addWidget(self.questions_btn_2)
        self.chat_btn_2 = QtWidgets.QPushButton(parent=self.full_menu_widget)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("resources/icon/product-32.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon6.addPixmap(QtGui.QPixmap("resources/icon/product-48.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.chat_btn_2.setIcon(icon6)
        self.chat_btn_2.setIconSize(QtCore.QSize(20, 20))
        self.chat_btn_2.setCheckable(True)
        self.chat_btn_2.setAutoExclusive(True)
        self.chat_btn_2.setObjectName("chat_btn_2")
        self.verticalLayout_2.addWidget(self.chat_btn_2)
        self.credits_btn_2 = QtWidgets.QPushButton(parent=self.full_menu_widget)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("resources/icon/group-32.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon7.addPixmap(QtGui.QPixmap("resources/icon/group-48.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.credits_btn_2.setIcon(icon7)
        self.credits_btn_2.setIconSize(QtCore.QSize(20, 20))
        self.credits_btn_2.setCheckable(True)
        self.credits_btn_2.setAutoExclusive(True)
        self.credits_btn_2.setObjectName("credits_btn_2")
        self.verticalLayout_2.addWidget(self.credits_btn_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 358, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.exit_btn_2 = QtWidgets.QPushButton(parent=self.full_menu_widget)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("resources/icon/close-window-64.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.exit_btn_2.setIcon(icon8)
        self.exit_btn_2.setIconSize(QtCore.QSize(20, 20))
        self.exit_btn_2.setObjectName("exit_btn_2")
        self.verticalLayout_4.addWidget(self.exit_btn_2)
        self.gridLayout.addWidget(self.full_menu_widget, 0, 1, 1, 1)
        self.icon_only_widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.icon_only_widget.setObjectName("icon_only_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.logo_label_1 = QtWidgets.QLabel(parent=self.icon_only_widget)
        self.logo_label_1.setMinimumSize(QtCore.QSize(50, 50))
        self.logo_label_1.setMaximumSize(QtCore.QSize(50, 50))
        self.logo_label_1.setText("")
        self.logo_label_1.setPixmap(QtGui.QPixmap("resources/icon/logo2_preview.png"))
        self.logo_label_1.setScaledContents(True)
        self.logo_label_1.setObjectName("logo_label_1")
        self.horizontalLayout_3.addWidget(self.logo_label_1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.home_btn_1 = QtWidgets.QPushButton(parent=self.icon_only_widget)
        self.home_btn_1.setText("")
        self.home_btn_1.setIcon(icon3)
        self.home_btn_1.setIconSize(QtCore.QSize(20, 20))
        self.home_btn_1.setCheckable(True)
        self.home_btn_1.setAutoExclusive(True)
        self.home_btn_1.setObjectName("home_btn_1")
        self.verticalLayout.addWidget(self.home_btn_1)
        self.dashboard_btn_1 = QtWidgets.QPushButton(parent=self.icon_only_widget)
        self.dashboard_btn_1.setText("")
        self.dashboard_btn_1.setIcon(icon4)
        self.dashboard_btn_1.setIconSize(QtCore.QSize(20, 20))
        self.dashboard_btn_1.setCheckable(True)
        self.dashboard_btn_1.setAutoExclusive(True)
        self.dashboard_btn_1.setObjectName("dashboard_btn_1")
        self.verticalLayout.addWidget(self.dashboard_btn_1)
        self.questions_btn_1 = QtWidgets.QPushButton(parent=self.icon_only_widget)
        self.questions_btn_1.setText("")
        self.questions_btn_1.setIcon(icon5)
        self.questions_btn_1.setIconSize(QtCore.QSize(20, 20))
        self.questions_btn_1.setCheckable(True)
        self.questions_btn_1.setAutoExclusive(True)
        self.questions_btn_1.setObjectName("questions_btn_1")
        self.verticalLayout.addWidget(self.questions_btn_1)
        self.chat_btn_1 = QtWidgets.QPushButton(parent=self.icon_only_widget)
        self.chat_btn_1.setText("")
        self.chat_btn_1.setIcon(icon6)
        self.chat_btn_1.setIconSize(QtCore.QSize(20, 20))
        self.chat_btn_1.setCheckable(True)
        self.chat_btn_1.setAutoExclusive(True)
        self.chat_btn_1.setObjectName("chat_btn_1")
        self.verticalLayout.addWidget(self.chat_btn_1)
        self.credits_btn_1 = QtWidgets.QPushButton(parent=self.icon_only_widget)
        self.credits_btn_1.setText("")
        self.credits_btn_1.setIcon(icon7)
        self.credits_btn_1.setIconSize(QtCore.QSize(20, 20))
        self.credits_btn_1.setCheckable(True)
        self.credits_btn_1.setAutoExclusive(True)
        self.credits_btn_1.setObjectName("credits_btn_1")
        self.verticalLayout.addWidget(self.credits_btn_1)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 360, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.exit_btn_1 = QtWidgets.QPushButton(parent=self.icon_only_widget)
        self.exit_btn_1.setText("")
        self.exit_btn_1.setIcon(icon8)
        self.exit_btn_1.setIconSize(QtCore.QSize(20, 20))
        self.exit_btn_1.setObjectName("exit_btn_1")
        self.verticalLayout_3.addWidget(self.exit_btn_1)
        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(5)
        self.change_btn.toggled['bool'].connect(self.icon_only_widget.setVisible) # type: ignore
        self.change_btn.toggled['bool'].connect(self.full_menu_widget.setHidden) # type: ignore
        self.home_btn_1.toggled['bool'].connect(self.home_btn_2.setChecked) # type: ignore
        self.dashboard_btn_1.toggled['bool'].connect(self.dashboard_btn_2.setChecked) # type: ignore
        self.questions_btn_1.toggled['bool'].connect(self.questions_btn_2.setChecked) # type: ignore
        self.chat_btn_1.toggled['bool'].connect(self.chat_btn_2.setChecked) # type: ignore
        self.credits_btn_1.toggled['bool'].connect(self.credits_btn_2.setChecked) # type: ignore
        self.home_btn_2.toggled['bool'].connect(self.home_btn_1.setChecked) # type: ignore
        self.dashboard_btn_2.toggled['bool'].connect(self.dashboard_btn_1.setChecked) # type: ignore
        self.questions_btn_2.toggled['bool'].connect(self.questions_btn_1.setChecked) # type: ignore
        self.chat_btn_2.toggled['bool'].connect(self.chat_btn_1.setChecked) # type: ignore
        self.credits_btn_2.toggled['bool'].connect(self.credits_btn_1.setChecked) # type: ignore
        self.exit_btn_2.clicked.connect(MainWindow.close) # type: ignore
        self.exit_btn_1.clicked.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyPlanets"))
        self.search_input.setPlaceholderText(_translate("MainWindow", "Buscar..."))
        self.label_4.setText(_translate("MainWindow", ""))
        self.label_5.setText(_translate("MainWindow", "Estadisticas"))
        self.label_6.setText(_translate("MainWindow", "Preguntas"))
        self.label_7.setText(_translate("MainWindow", "ChatBOT"))
        self.label_8.setText(_translate("MainWindow", "Creditos"))
        self.label_9.setText(_translate("MainWindow", "Search Page"))
        self.label_10.setText(_translate("MainWindow", "User Page"))
        self.logo_label_3.setText(_translate("MainWindow", "PyPlanets"))
        self.home_btn_2.setText(_translate("MainWindow", "Planets"))
        self.dashboard_btn_2.setText(_translate("MainWindow", "Estadisticas"))
        self.questions_btn_2.setText(_translate("MainWindow", "Preguntas"))
        self.chat_btn_2.setText(_translate("MainWindow", "ChatGPT"))
        self.credits_btn_2.setText(_translate("MainWindow", "Creditos"))
        self.exit_btn_2.setText(_translate("MainWindow", "Salir"))

    def get_galaxy_html(self):
        return """
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body, html {
                    margin: 0;
                    padding: 0;
                    width: 100%;
                    height: 100%;
                    overflow: hidden;
                }
                .galaxy-bg {
                    width: 100%;
                    height: 100%;
                    background-color: #000;
                    background: 
                        radial-gradient(2px 2px at 20% 30%, #fff, rgba(0,0,0,0)),
                        radial-gradient(2px 2px at 40% 70%, #fff, rgba(0,0,0,0)),
                        radial-gradient(2px 2px at 60% 20%, #fff, rgba(0,0,0,0)),
                        radial-gradient(2px 2px at 80% 40%, #fff, rgba(0,0,0,0)),
                        radial-gradient(circle at 20% 30%, rgba(138,76,173,0.5), transparent 50%),
                        radial-gradient(circle at 70% 80%, rgba(77,121,255,0.5), transparent 80%),
                        radial-gradient(circle at 40% 60%, rgba(255,177,77,0.5), transparent 40%),
                        radial-gradient(circle at 80% 20%, rgba(179,77,255,0.5), transparent 40%),
                        linear-gradient(to bottom, #000000, #1a0330);
                    animation: twinkle 5s infinite;
                }
                
                @keyframes twinkle {
                    0%, 100% { opacity: 0.95; }
                    50% { opacity: 1; }
                }
                
                /* Agregar estrellas que parpadean */
                .stars {
                    position: fixed;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    pointer-events: none;
                }
                
                .star {
                    position: absolute;
                    width: 2px;
                    height: 2px;
                    background: white;
                    border-radius: 50%;
                }
                
                .star.medium {
                    width: 3px;
                    height: 3px;
                }
                
                .star.big {
                    width: 4px;
                    height: 4px;
                }
            </style>
        </head>
        <body>
            <div class="galaxy-bg"></div>
            <div class="stars" id="stars"></div>
            
            <script>
                // estrellas
                const starsContainer = document.getElementById('stars');
                const numStars = 200;
                
                for (let i = 0; i < numStars; i++) {
                    const star = document.createElement('div');
                    star.className = `star ${Math.random() > 0.8 ? 'big' : Math.random() > 0.6 ? 'medium' : ''}`;
                    star.style.left = `${Math.random() * 100}%`;
                    star.style.top = `${Math.random() * 100}%`;
                    star.style.animation = `twinkle ${2 + Math.random() * 3}s infinite ${Math.random() * 2}s`;
                    starsContainer.appendChild(star);
                }
            </script>
        </body>
        </html>
        """

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
