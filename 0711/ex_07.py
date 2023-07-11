import sys
import csv
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QGroupBox, QLabel, QLineEdit, QPushButton, QListWidget, QMessageBox

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("복잡한 UI 응용")
        self.resize(500, 250)

        # 그룹 상자 설정
        group_box1 = QGroupBox("info")
        group_box2 = QGroupBox("입력 내용 보기")
        group_box3 = QGroupBox("저장 및 불러오기")

        # 레이어 설정
        self.label_id = QLabel("id : ")
        self.label_age = QLabel("나이 : ")
        self.label_gender = QLabel("성별 : ")
        self.label_country = QLabel("국가 : ")

        # input label 설정
        self.id_line_edit = QLineEdit()
        self.age_line_edit = QLineEdit()
        self.gender_line_edit = QLineEdit()
        self.country_line_edit = QLineEdit()

        # push box 설정
        self.view_button = QPushButton("보기")
        self.view_button.clicked.connect(self.show_info)
        self.close_button = QPushButton("닫기")

        # 저장 및 불러오기 버튼 설정
        self.save_button = QPushButton("저장")
        self.save_button.clicked.connect(self.save_info)
        self.load_button = QPushButton("불러오기")
        self.load_button.clicked.connect(self.load_info)

        # 리스트 박스 설정
        self.list_widget = QListWidget()

        # 1 그룹 상자
        layout1 = QVBoxLayout()
        layout1.addWidget(self.label_id)
        layout1.addWidget(self.id_line_edit)
        layout1.addWidget(self.label_age)
        layout1.addWidget(self.age_line_edit)
        layout1.addWidget(self.label_gender)
        layout1.addWidget(self.gender_line_edit)
        layout1.addWidget(self.label_country)
        layout1.addWidget(self.country_line_edit)

        group_box1.setLayout(layout1)

        # 2 그룹 상자
        self.info_label = QLabel()
        layout2 = QVBoxLayout()
        layout2.addWidget(self.info_label)
        layout2.addWidget(self.view_button)
        layout2.addWidget(self.close_button)
        layout2.setContentsMargins(10, 10, 10, 10)
        group_box2.setLayout(layout2)

        # 3 그룹 상자
        layout3 = QVBoxLayout()
        layout3.addWidget(self.save_button)
        layout3.addWidget(self.load_button)
        layout3.addWidget(self.list_widget)
        layout3.setContentsMargins(10, 10, 10, 10)
        group_box3.setLayout(layout3)

        # 전체 레이아웃
        main_layout = QVBoxLayout()
        main_layout.addWidget(group_box1)
        main_layout.addWidget(group_box2)
        main_layout.addWidget(group_box3)

        self.setLayout(main_layout)

    def show_info(self):
        id = self.id_line_edit.text()
        age = self.age_line_edit.text()
        gender = self.gender_line_edit.text()
        country = self.country_line_edit.text()

        info_text = f"아이디 : {id} \n 나이: {age} \n 성별: {gender} \n 국가: {country}"
        self.info_label.setText(info_text)

    def close_info(self):
        self.age_line_edit.clear()
        self.gender_line_edit.clear()
        self.country_line_edit.clear()
        self.info_label.clear()

    def save_info(self):
        id = self.id_line_edit.text()
        age = self.age_line_edit.text()
        gender = self.gender_line_edit.text()
        country = self.country_line_edit.text()

        data = [id, age, gender, country]

        try:
            with open('data.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(data)
            QMessageBox.information(self, "저장 완료" , "입력 내용이 성공적으로 저장되었습니다.")
        except Exception as e:
            QMessageBox.critical(self, "저장 실패", f"입력 내용 저장 중 오류가 발생했습니다. \n {str(e)}")


    def load_info(self):
        self.list_widget.clear()

        try:
            with open('data.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    data_text = f"id:{row[0]}, 나이: {row[1]}, 성별:{row[2]}, 국가: {row[3]}"
                    self.list_widget.addItem(data_text)
        except Exception as e:
            QMessageBox.critical(self, "불러오기 실패", f"데이터 불러오기 중 오류가 발생했습니다:\n{str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
