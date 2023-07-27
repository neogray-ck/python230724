# DemoForm.py
# DemoForm.ui(화면) + DemoForm.py(로직)
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

# 디자인된 문서 로딩
form_class = uic.loadUiType("DemoForm.ui")[0]

# 폼 클래스 정의
class DemoForm(QDialog, form_class):
    # 초기화 Method
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 화면")

# 직접 모듈을 실행했는지 체크(진입점)
# __name__은 미리 정의된 변수인데, 본 프로그램이 사용자에 의해 단독으로 실행되면
# __name__은 자동으로 __main__으로 세팅된다. 이를 확인해서 직접 실행 여부를 판단
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_()