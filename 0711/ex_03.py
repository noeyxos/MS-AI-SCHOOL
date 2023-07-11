import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("메시지 박스 예제")
        self.resize(500, 400)

        layout = QVBoxLayout()

        info_button = QPushButton("정보 메시지")
        info_button.clicked.connect(self.show_info_message)
        layout.addWidget(info_button)

        warning_button = QPushButton("경고 메시지")
        warning_button.clicked.connect(self.show_warning_message)
        layout.addWidget(warning_button)

        question_button = QPushButton("질문 메시지")
        question_button.clicked.connect(self.show_question_message)
        layout.addWidget(question_button)

        self.setLayout(layout)

    def show_info_message(self):
        QMessageBox.information(self, "정보", "이것은 정보 메시지 입니다.", QMessageBox.Ok)

    def show_warning_message(self):
        QMessageBox.information(self, "경고", "이것은 경고 메시지 입니다.", QMessageBox.Ok)

    def show_question_message(self):
        result = QMessageBox.question(self, "질문", "계속 진행하겠습니까?", QMessageBox.Yes | QMessageBox.No)
        if result == QMessageBox.Yes:
            QMessageBox.information(self, "응답", "사용자가 '예'를 선택했습니다.", QMessageBox.Ok)
        else:
            QMessageBox.information(self, "응답", "사용자가 '아니오'를 선택했습니다.", QMessageBox.Ok)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())