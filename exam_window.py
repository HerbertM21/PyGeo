from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QLabel, QProgressBar, QMessageBox)
from PyQt6.QtCore import Qt, QTimer, pyqtSignal
from PyQt6.QtGui import QPixmap, QFont
import random


class ExamWindow(QMainWindow):
    exam_completed = pyqtSignal(dict)  # Señal para comunicar los resultados

    def __init__(self, exam_data):
        super().__init__()
        self.exam_data = exam_data
        self.current_question = 0
        self.correct_answers = 0
        self.questions = exam_data['questions']
        random.shuffle(self.questions)

        self.setWindowTitle(exam_data['title'])
        self.setFixedSize(600, 800)

        # Centrar la ventana en la pantalla
        screen = QApplication.primaryScreen().geometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)

        self.setup_ui()
        self.show_question()

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Barra de progreso
        self.progress = QProgressBar()
        self.progress.setRange(0, len(self.questions))
        self.progress.setValue(0)
        layout.addWidget(self.progress)

        # Área de la pregunta
        self.question_label = QLabel()
        self.question_label.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        self.question_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.question_label.setStyleSheet("""
            QLabel {
                color: #2c3e50;
                background-color: white;
                padding: 15px;
                border: 2px solid #3498db;
                border-radius: 10px;
                margin: 10px 0;
            }
        """)
        layout.addWidget(self.question_label)

        # Imagen
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.image_label)

        # Contenedor para los botones de opciones
        self.options_widget = QWidget()
        self.options_layout = QVBoxLayout(self.options_widget)
        layout.addWidget(self.options_widget)

        # Estilo general
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f5f6fa;
            }
            QPushButton {
                padding: 15px;
                border-radius: 25px;
                font-size: 16px;
                font-weight: bold;
                margin: 5px;
            }
            QProgressBar {
                border: none;
                background-color: #ddd;
                text-align: center;
                border-radius: 15px;
                height: 30px;
            }
            QProgressBar::chunk {
                background-color: #3498db;
                border-radius: 15px;
            }
        """)

    def show_question(self):
        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]

            # Actualizar progreso
            self.progress.setValue(self.current_question + 1)

            # Mostrar pregunta
            self.question_label.setText(question['question'])

            # Mostrar imagen
            pixmap = QPixmap(question['image'])
            if not pixmap.isNull():
                pixmap = pixmap.scaled(300, 300, Qt.AspectRatioMode.KeepAspectRatio)
                self.image_label.setPixmap(pixmap)

            # Limpiar opciones anteriores
            while self.options_layout.count():
                child = self.options_layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()

            # Añadir nuevas opciones
            options = question['options'].copy()
            random.shuffle(options)

            for option in options:
                button = QPushButton(option)
                button.clicked.connect(lambda checked, opt=option: self.check_answer(opt))
                button.setStyleSheet("""
                    QPushButton {
                        background-color: white;
                        border: 2px solid #3498db;
                        color: #3498db;
                    }
                    QPushButton:hover {
                        background-color: #3498db;
                        color: white;
                    }
                """)
                self.options_layout.addWidget(button)
        else:
            self.show_results()

    def show_results(self):
        score = (self.correct_answers / len(self.questions)) * 100
        xp_earned = int((score / 100) * self.exam_data['xp'])

        result_message = f"""
        ¡Examen completado!

        Respuestas correctas: {self.correct_answers}/{len(self.questions)}
        Puntuación: {score:.1f}%
        XP ganada: {xp_earned}

        {'¡Excelente trabajo! 🌟' if score >= 80 else
         '¡Buen intento! 👍' if score >= 60 else
         'Sigue practicando 💪'}
        """

        results = QMessageBox(self)
        results.setWindowTitle("Resultados del Examen")
        results.setText(result_message)
        results.setIcon(QMessageBox.Icon.Information)

        # Botón para volver al menú principal
        results.addButton("Volver al Menú", QMessageBox.ButtonRole.AcceptRole)

        # Botón para reintentar
        retry_button = results.addButton("Reintentar", QMessageBox.ButtonRole.RejectRole)

        # Preparar datos del resultado
        exam_results = {
            'category': self.exam_data['category'],
            'title': self.exam_data['title'],
            'score': score,
            'xp_earned': xp_earned,
            'correct_answers': self.correct_answers,
            'total_questions': len(self.questions)
        }

        result = results.exec()

        if result == 0:  # Volver al menú
            self.exam_completed.emit(exam_results)  # Emitir resultados
            self.close()
        else:  # Reintentar
            self.reset_exam()

    def check_answer(self, selected_option):
        current_question = self.questions[self.current_question]
        correct_answer = current_question['correct']

        # Deshabilitar todos los botones temporalmente
        for i in range(self.options_layout.count()):
            self.options_layout.itemAt(i).widget().setEnabled(False)

        if selected_option == correct_answer:
            self.correct_answers += 1
            self.show_feedback(True, current_question['explanation'])
        else:
            self.show_feedback(False, current_question['explanation'])

    def show_feedback(self, is_correct, explanation):
        # Cambiar color del botón seleccionado
        for i in range(self.options_layout.count()):
            button = self.options_layout.itemAt(i).widget()
            if button.text() == self.questions[self.current_question]['correct']:
                button.setStyleSheet("""
                    QPushButton {
                        background-color: #2ecc71;
                        color: white;
                        border: none;
                    }
                """)
            elif not is_correct and button.isEnabled() == False:
                button.setStyleSheet("""
                    QPushButton {
                        background-color: #e74c3c;
                        color: white;
                        border: none;
                    }
                """)

        # Mostrar explicación
        feedback = QMessageBox(self)
        feedback.setWindowTitle("Resultado")
        if is_correct:
            feedback.setText("¡Correcto! 🎉\n\n" + explanation)
            feedback.setIcon(QMessageBox.Icon.Information)
        else:
            feedback.setText("Incorrecto 😔\n\n" + explanation)
            feedback.setIcon(QMessageBox.Icon.Warning)

        # Cerrar automáticamente después de 2 segundos
        QTimer.singleShot(2000, feedback.close)
        feedback.show()

        # Esperar un momento y mostrar la siguiente pregunta
        QTimer.singleShot(2500, self.next_question)

    def next_question(self):
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.show_question()
        else:
            self.show_results()

    def show_results(self):
        score = (self.correct_answers / len(self.questions)) * 100
        xp_earned = int((score / 100) * self.exam_data['xp'])

        result_message = f"""
        ¡Examen completado!

        Respuestas correctas: {self.correct_answers}/{len(self.questions)}
        Puntuación: {score:.1f}%
        XP ganada: {xp_earned}

        {'¡Excelente trabajo! 🌟' if score >= 80 else
        '¡Buen intento! 👍' if score >= 60 else
        'Sigue practicando 💪'}
        """

        results = QMessageBox(self)
        results.setWindowTitle("Resultados del Examen")
        results.setText(result_message)
        results.setIcon(QMessageBox.Icon.Information)

        # Botón para volver al menú principal
        menu_button = results.addButton("Volver al Menú", QMessageBox.ButtonRole.AcceptRole)

        # Botón para reintentar
        retry_button = results.addButton("Reintentar", QMessageBox.ButtonRole.RejectRole)

        # Preparar datos del resultado para emitir la señal
        exam_results = {
            'category': self.exam_data.get('category', ''),
            'title': self.exam_data['title'],
            'score': score,
            'xp_earned': xp_earned,
            'correct_answers': self.correct_answers,
            'total_questions': len(self.questions)
        }

        result = results.exec()
        clicked_button = results.clickedButton()

        if clicked_button == menu_button:  # Si se eligio volver al menú
            self.exam_completed.emit(exam_results)  # Emitir resultados
            self.close()  # Cerrar la ventana del examen
        elif clicked_button == retry_button:  # Si se eligió reintentar
            self.reset_exam()  # Reiniciar el examen

    def reset_exam(self):
        self.current_question = 0
        self.correct_answers = 0
        random.shuffle(self.questions)
        self.progress.setValue(0)
        self.show_question()

    def closeEvent(self, event):
        # CIERRA VENTANA
        # implementar para actualizar el progreso en la ventana principal cuando se cierre ventana
        event.accept()