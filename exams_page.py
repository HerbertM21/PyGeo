from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
                             QLabel, QScrollArea, QProgressBar, QGridLayout)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap
from exam_data import get_exams_by_category
from exam_window import ExamWindow


class ExamButton(QPushButton):
    def __init__(self, exam_data):
        super().__init__()
        self.exam_data = exam_data
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        image_label = QLabel()
        pixmap = QPixmap(self.exam_data['icon'])
        if not pixmap.isNull():
            pixmap = pixmap.scaled(120, 120, Qt.AspectRatioMode.KeepAspectRatio)
            image_label.setPixmap(pixmap)

        title_label = QLabel(self.exam_data['title'])
        title_label.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        title_label.setStyleSheet("color: #2c3e50;")

        difficulty_label = QLabel(f"Dificultad: {self.exam_data['difficulty']}")
        difficulty_label.setStyleSheet("color: #7f8c8d;")

        xp_label = QLabel(f"XP: {self.exam_data['xp']}")
        xp_label.setStyleSheet("color: #27ae60;")

        for label in [image_label, title_label, difficulty_label, xp_label]:
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(label)

        self.setFixedSize(200, 250)
        self.setStyleSheet("""
            ExamButton {
                background-color: #f5f6fa;
                border: 2px solid #ddd;
                border-radius: 10px;
                padding: 10px;
            }
            ExamButton:hover {
                border-color: #3498db;
                background-color: #f0f8ff;
            }
        """)


class ExamsPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Inicializar variables antes de setup_ui
        self.nivel = 1
        self.exp = 0
        self.exp_necesaria = 100

        # Ahora llamar a setup_ui
        self.setup_ui()

    def setup_ui(self):
        self.layout = QVBoxLayout(self)

        # Crear secciones
        self.create_categories_section()
        self.create_exams_section()
        self.create_level_section()

        self.update_level_display()

    def create_categories_section(self):
        categories_widget = QWidget()
        categories_layout = QVBoxLayout(categories_widget)
        buttons_layout = QHBoxLayout()
        icons_layout = QHBoxLayout()

        icons_layout.setSpacing(0)
        buttons_layout.setSpacing(0)

        self.categories = [
            ("PAÍSES", "paises", "#3498db", "resources/icon/paises-preview.png"),
            ("CAPITALES", "capitales", "#e74c3c", "resources/icon/capitals-preview.png"),
            ("FLORA", "flora", "#2ecc71", "resources/icon/flora-preview.png"),
            ("FAUNA", "fauna", "#f1c40f", "resources/icon/fauna.png")
        ]

        for _, _, _, icon_path in self.categories:
            icon_container = QWidget()
            icon_container.setFixedWidth(150)  # Mismo ancho que los botones
            icon_layout = QHBoxLayout(icon_container)

            icon_label = QLabel()
            pixmap = QPixmap(icon_path)
            if not pixmap.isNull():
                pixmap = pixmap.scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio)
                icon_label.setPixmap(pixmap)
            icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            icon_layout.addWidget(icon_label)
            icons_layout.addWidget(icon_container)

        for texto, categoria, color, _ in self.categories:
            btn = QPushButton(texto)
            btn.setFixedSize(150, 50)
            btn.clicked.connect(lambda c, cat=categoria: self.load_exams(cat))
            btn.setStyleSheet(self.get_category_button_style(color))
            buttons_layout.addWidget(btn)

        categories_layout.addLayout(icons_layout)
        categories_layout.addLayout(buttons_layout)
        self.layout.addWidget(categories_widget)

    def create_exams_section(self):
        self.exams_scroll = QScrollArea()
        self.exams_scroll.setWidgetResizable(True)
        self.exams_scroll.setFixedHeight(500)

        self.exams_container = QWidget()
        self.exams_layout = QHBoxLayout(self.exams_container)
        self.exams_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.exams_scroll.setWidget(self.exams_container)
        self.exams_scroll.setStyleSheet("""
            QScrollArea {
                background-color: #f5f6fa;
                border: none;
            }
        """)
        self.layout.addWidget(self.exams_scroll)

    def create_level_section(self):
        level_widget = QWidget()
        level_layout = QVBoxLayout(level_widget)

        level_info = QGridLayout()
        level_info.setColumnStretch(0, 1)
        level_info.setColumnStretch(1, 1)
        level_info.setColumnStretch(2, 1)

        self.level_label = QLabel(f"Nivel {self.nivel}")
        self.level_label.setStyleSheet("color: #2c3e50;")
        self.level_label.setFont(QFont("Arial", 14, QFont.Weight.Bold))

        self.exp_label = QLabel(f"EXP: {self.exp}/{self.exp_necesaria}")
        self.exp_label.setStyleSheet("color: #27ae60;")
        self.exp_label.setFont(QFont("Arial", 10, QFont.Weight.Bold))

        # centrar el level
        level_info.addWidget(self.level_label, 0, 1, alignment=Qt.AlignmentFlag.AlignCenter)

        level_info.addWidget(self.exp_label, 0, 2, alignment=Qt.AlignmentFlag.AlignRight)

        self.progress_bar = QProgressBar()
        self.progress_bar.setFixedHeight(20)
        self.progress_bar.setRange(0, self.exp_necesaria)
        self.progress_bar.setValue(self.exp)
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                border: none;
                border-radius: 10px;
                background-color: #ddd;
                text-align: center;
            }
            QProgressBar::chunk {
                background-color: #3498db;
                border-radius: 10px;
            }
        """)

        level_layout.addLayout(level_info)
        level_layout.addWidget(self.progress_bar)
        self.layout.addWidget(level_widget)

    def load_exams(self, category):
        while self.exams_layout.count():
            item = self.exams_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        exams = get_exams_by_category(category)
        for exam_data in exams:
            exam_button = ExamButton(exam_data)
            exam_button.clicked.connect(lambda c, data=exam_data: self.start_exam(data))
            self.exams_layout.addWidget(exam_button)

    def start_exam(self, exam_data):
        self.exam_window = ExamWindow(exam_data)
        self.exam_window.exam_completed.connect(self.on_exam_completed)
        self.exam_window.show()

    def on_exam_completed(self, result):
        self.exp += result['xp_earned']

        while self.exp >= self.exp_necesaria:
            self.nivel += 1
            self.exp -= self.exp_necesaria
            self.exp_necesaria = int(self.exp_necesaria * 1.5)

        self.update_level_display()

    def update_level_display(self):
        self.level_label.setText(f"Nivel {self.nivel}")
        self.exp_label.setText(f"EXP: {self.exp}/{self.exp_necesaria}")
        self.progress_bar.setRange(0, self.exp_necesaria)
        self.progress_bar.setValue(self.exp)

    @staticmethod
    def get_category_button_style(color):
        return f"""
            QPushButton {{
                background-color: {color};
                color: white;
                border: none;
                border-radius: 5px;
                font-weight: bold;
                font-size: 14px;
                padding: 10px;
            }}
            QPushButton:hover {{
                background-color: {color}dd;
            }}
        """